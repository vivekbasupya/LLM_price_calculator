# LLM Pricing Predictor

A clean and compact Flask application for calculating LLM pricing across different providers, regions, and models.

## 🚀 Features

- **Document Upload**: Upload PDF, TXT, or DOCX files for automatic token estimation
- **Prompt Text Estimation**: Paste the prompt that accompanies your documents and get instant token counts
- **Manual Token Input**: Override the auto-calculated input tokens at any time
- **Output Token Planning**: Capture expected completion tokens for full-funnel pricing
- **Multi-Provider Support**: OpenAI, Azure, AWS Bedrock, Google Cloud
- **Real-time Calculation**: Instant cost breakdown
- **Clean UI**: Modern, responsive interface
- **Drag & Drop**: Easy file uploads

## 📁 Project Structure

```
pricing-predictor/
├── app.py                 # Main Flask application
├── config/
│   ├── __init__.py
│   └── pricing.py        # Pricing data structure
├── utils/
│   ├── __init__.py
│   ├── text_extractor.py # Extract text from files
│   └── token_estimator.py # Estimate token counts
├── templates/
│   └── index.html        # Main UI template
├── static/
│   └── style.css         # Custom styles
├── uploads/              # Temporary file storage
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🛠️ Installation

1. **Clone or download the project**

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create required directories**
```bash
mkdir -p uploads config utils templates static
```

5. **Create `__init__.py` files**
```bash
touch config/__init__.py utils/__init__.py
```

## 🎯 Usage

1. **Start the server**
```bash
python app.py
```

2. **Open your browser**
```
http://localhost:5000
```

3. **Use the application**
   - Upload a document OR enter token count manually
   - Select Provider → Region → Model
   - Click "Calculate Pricing"
   - View cost breakdown

## 📊 Supported Formats

- **Documents**: PDF, TXT, DOCX (max 16MB)
- **Providers**: OpenAI, Azure, AWS Bedrock, Google Cloud
- **Tokens**: Automatic estimation or manual input

## 💵 Azure-style pricing

- All model rates are now stored in USD **per 1,000,000 tokens** to match the Azure OpenAI catalog.
- Each model has dedicated price points for **input**, **output**, and **cached prompt** tokens.
- Cached token costs are assumed to apply to document uploads (ideal for prompt caching workflows). Update `config/pricing.py` if your workload uses a different split.

## 🔧 API Endpoints

### `GET /api/providers`
Returns all available providers and pricing structure

### `POST /api/upload`
Upload a document for text extraction
- **Body**: multipart/form-data with 'file' field
- **Returns**: `{tokens_estimated, words, characters, filename}`

### `POST /api/calculate`
Calculate pricing
- **Body**: `{provider, region, model, tokens}`
- **Returns**: `{cost_usd, rate_per_1k, tokens, provider, region, model}`

## 📝 Adding New Pricing

Edit `config/pricing.py`:

```python
PRICING = {
    "YourProvider": {
        "YourRegion": {
            "model-name": 0.001  # Rate per 1K tokens
        }
    }
}
```

## 🎨 Customization

- **Styling**: Edit `static/style.css`
- **UI Layout**: Modify `templates/index.html`
- **Token Estimation**: Adjust ratio in `utils/token_estimator.py`

## 🔒 Security Notes

- Files are deleted after processing
- 16MB file size limit
- Only allowed extensions: .txt, .pdf, .docx
- Input validation on all endpoints

## 📦 Dependencies

- **Flask**: Web framework
- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX text extraction
- **Werkzeug**: File handling utilities

## 🐛 Troubleshooting

**Port already in use?**
```bash
python app.py --port 8000  # Use different port
```

**Module not found?**
```bash
pip install -r requirements.txt
```

**Upload fails?**
- Check file size (max 16MB)
- Verify file format (PDF, TXT, DOCX only)
- Ensure uploads/ directory exists

## 📄 License

Free to use and modify for personal and commercial projects.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

Made with ❤️ using Flask