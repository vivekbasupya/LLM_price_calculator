from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from pathlib import Path

from config.pricing import PRICING, get_providers, get_regions, get_models, get_rate
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
        'pricing': PRICING
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


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """
    Calculate pricing based on provider, region, model, and tokens
    Expects JSON: {provider, region, model, tokens}
    Returns: JSON with cost calculation details
    """
    data = request.get_json()
    
    # Validate input
    required_fields = ['provider', 'region', 'model', 'tokens']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    provider = data['provider']
    region = data['region']
    model = data['model']
    
    try:
        tokens = int(data['tokens'])
        if tokens < 1:
            return jsonify({'error': 'Tokens must be at least 1'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid token count'}), 400
    
    # Get rate
    rate = get_rate(provider, region, model)
    if rate is None:
        return jsonify({'error': 'Invalid provider/region/model combination'}), 400
    
    # Calculate cost
    cost = (tokens / 1000) * rate
    
    return jsonify({
        'cost_usd': round(cost, 6),
        'rate_per_1k': rate,
        'tokens': tokens,
        'provider': provider,
        'region': region,
        'model': model
    })


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 16MB'}), 413


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)