from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from pathlib import Path

from config.pricing import (
    PRICING,
    get_model_pricing
)
from utils.text_extractor import TextExtractor
from utils.token_estimator import TokenEstimator

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = Path('uploads')
UPLOAD_FOLDER.mkdir(exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')


@app.route('/api/providers')
def api_providers():
    """Get all pricing data structure"""
    return jsonify({
        'providers': list(PRICING.keys()),
        'pricing': PRICING,
        'unit': 'per_million_tokens'
    })


@app.route('/api/upload', methods=['POST'])
def api_upload():
    """
    Handle file upload and return text statistics
    Returns: JSON with tokens_estimated, words, characters
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Use: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
    
    try:
        # Save file
        filename = secure_filename(file.filename)
        filepath = app.config['UPLOAD_FOLDER'] / filename
        file.save(filepath)
        
        # Extract text
        text = TextExtractor.extract(filepath)
        stats = TextExtractor.get_stats(text)
        tokens = TokenEstimator.estimate_from_stats(stats)
        
        # Clean up uploaded file
        filepath.unlink()
        
        return jsonify({
            'tokens_estimated': tokens,
            'words': stats['word_count'],
            'characters': stats['character_count'],
            'filename': filename
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/tokens', methods=['POST'])
def api_tokens():
    """
    Estimate tokens for a block of text.
    Expects JSON: {text: "..."}
    Returns: {tokens_estimated: int, words: int}
    """
    data = request.get_json() or {}
    text = data.get('text', '')
    if not isinstance(text, str):
        return jsonify({'error': 'Text must be a string'}), 400

    word_count = len(text.split())
    tokens = TokenEstimator.estimate(text=text)

    return jsonify({
        'tokens_estimated': tokens,
        'words': word_count
    })


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """
    Calculate pricing based on provider, region, model, and tokens
    Expects JSON: {
        provider, region, model,
        input_tokens, output_tokens, cached_tokens,
        prompt_tokens?, document_tokens?
    }
    Returns: JSON with cost calculation details
    """
    data = request.get_json()
    
    # Validate input
    required_fields = ['provider', 'region', 'model', 'input_tokens', 'output_tokens', 'cached_tokens']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    provider = data['provider']
    region = data['region']
    model = data['model']
    
    def parse_tokens(value, field_name):
        try:
            tokens_value = int(value)
        except (ValueError, TypeError):
            raise ValueError(f'Invalid token count for {field_name}')
        if tokens_value < 0:
            raise ValueError(f'{field_name} must be zero or greater')
        return tokens_value
    
    try:
        input_tokens = parse_tokens(data['input_tokens'], 'input_tokens')
        output_tokens = parse_tokens(data['output_tokens'], 'output_tokens')
        cached_tokens = parse_tokens(data['cached_tokens'], 'cached_tokens')
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    
    model_pricing = get_model_pricing(provider, region, model)
    if model_pricing is None:
        return jsonify({'error': 'Invalid provider/region/model combination'}), 400
    
    TOKENS_PER_MILLION = 1_000_000
    input_rate = model_pricing.get('input_per_million', 0)
    output_rate = model_pricing.get('output_per_million', 0)
    cached_rate = model_pricing.get('cached_per_million', 0)

    def cost_component(token_count, rate):
        if token_count == 0 or rate == 0:
            return 0.0
        return (token_count / TOKENS_PER_MILLION) * rate

    input_cost = cost_component(input_tokens, input_rate)
    output_cost = cost_component(output_tokens, output_rate)
    cached_cost = cost_component(cached_tokens, cached_rate)
    total_cost = input_cost + output_cost + cached_cost

    prompt_tokens = parse_tokens(data.get('prompt_tokens', 0), 'prompt_tokens') if 'prompt_tokens' in data else 0
    document_tokens = parse_tokens(data.get('document_tokens', 0), 'document_tokens') if 'document_tokens' in data else 0
    
    return jsonify({
        'cost_usd': round(total_cost, 6),
        'provider': provider,
        'region': region,
        'model': model,
        'rates_per_million': {
            'input': input_rate,
            'output': output_rate,
            'cached': cached_rate
        },
        'tokens': {
            'input': input_tokens,
            'output': output_tokens,
            'cached': cached_tokens,
            'prompt': prompt_tokens,
            'documents': document_tokens
        },
        'breakdown': {
            'input_cost': round(input_cost, 6),
            'output_cost': round(output_cost, 6),
            'cached_cost': round(cached_cost, 6),
            'total_cost': round(total_cost, 6)
        }
    })


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 16MB'}), 413


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)