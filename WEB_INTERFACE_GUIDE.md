# Web Interface Guide

## Features

The web interface provides a user-friendly way to:
- Input product data through an intuitive form
- Generate content using the multi-agent system
- View generated JSON outputs in a readable format
- Download JSON files directly
- Load sample data for quick testing

## Running the Web Interface

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Start the Server

```bash
python app.py
```

### Step 3: Open in Browser

Navigate to: **http://localhost:5000**

## Using the Interface

### 1. Fill in Product Information

- **Product Name**: Name of your product (required)
- **Concentration**: Product concentration details (required)
- **Skin Type**: Comma-separated list (e.g., "Oily, Combination")
- **Key Ingredients**: Comma-separated list (e.g., "Vitamin C, Hyaluronic Acid")
- **Benefits**: Comma-separated list (e.g., "Brightening, Fades dark spots")
- **How to Use**: Usage instructions (required)
- **Side Effects**: Any side effects (optional)
- **Price**: Price in INR (required)

### 2. Generate Content

- Click **"Load Sample Data"** to pre-fill the form with example data
- Click **"Generate Content"** to run the multi-agent pipeline
- Wait for the generation to complete (you'll see a loading spinner)

### 3. View Results

The results are displayed in three tabs:
- **FAQ Page**: Categorized questions (22+ questions)
- **Product Page**: Complete product information
- **Comparison Page**: Product A vs Product B comparison

### 4. Download JSON Files

Click the **"Download"** button on any tab to download the corresponding JSON file.

## API Endpoints

The web interface exposes the following endpoints:

- `GET /` - Main form page
- `POST /generate` - Generate content from form data
- `GET /download/<page_type>` - Download JSON file (faq, product_page, comparison_page)
- `GET /load-sample` - Get sample product data

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
to a different port (e.g., `port=5001`).

### Flask Not Found

Make sure Flask is installed:
```bash
pip install Flask
```

### JSON Display Issues

The JSON viewer uses monospace font for readability. If JSON appears malformed, check the browser console for errors.

## Architecture

The web interface (`app.py`) acts as a thin wrapper around the multi-agent system:
- Receives form data
- Validates input
- Calls the PipelineOrchestrator
- Returns formatted JSON results
- Serves static files (CSS, templates)

The core multi-agent architecture remains unchanged - the web interface is just a presentation layer.


