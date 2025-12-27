"""Flask web application for the multi-agent content generation system."""

from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from pathlib import Path
from orchestrator.pipeline_orchestrator import PipelineOrchestrator
from models.product_model import ProductModel

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main form page."""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """Generate content from product data."""
    try:
        # Get product data from form
        product_data = {
            "product_name": request.form.get('product_name', '').strip(),
            "concentration": request.form.get('concentration', '').strip(),
            "skin_type": [s.strip() for s in request.form.get('skin_type', '').split(',') if s.strip()],
            "key_ingredients": [i.strip() for i in request.form.get('key_ingredients', '').split(',') if i.strip()],
            "benefits": [b.strip() for b in request.form.get('benefits', '').split(',') if b.strip()],
            "how_to_use": request.form.get('how_to_use', '').strip(),
            "side_effects": request.form.get('side_effects', '').strip(),
            "price": float(request.form.get('price', 0))
        }
        
        # Validate required fields
        if not product_data["product_name"]:
            return jsonify({"error": "Product name is required"}), 400
        
        if not product_data["skin_type"]:
            return jsonify({"error": "At least one skin type is required"}), 400
        
        if not product_data["key_ingredients"]:
            return jsonify({"error": "At least one key ingredient is required"}), 400
        
        if not product_data["benefits"]:
            return jsonify({"error": "At least one benefit is required"}), 400
        
        # Initialize orchestrator and execute pipeline
        orchestrator = PipelineOrchestrator()
        output_files = orchestrator.execute(product_data, output_dir="outputs")
        
        # Read generated JSON files
        results = {}
        for page_type, file_path in output_files.items():
            with open(file_path, 'r', encoding='utf-8') as f:
                results[page_type] = json.load(f)
        
        return jsonify({
            "success": True,
            "message": "Content generated successfully!",
            "results": results,
            "output_files": output_files
        })
        
    except ValueError as e:
        return jsonify({"error": f"Validation error: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error generating content: {str(e)}"}), 500


@app.route('/download/<page_type>')
def download(page_type):
    """Download a specific JSON output file."""
    valid_types = ['faq', 'product_page', 'comparison_page']
    if page_type not in valid_types:
        return jsonify({"error": "Invalid page type"}), 400
    
    file_path = Path("outputs") / f"{page_type}.json"
    if not file_path.exists():
        return jsonify({"error": "File not found. Please generate content first."}), 404
    
    return send_file(file_path, as_attachment=True, download_name=f"{page_type}.json")


@app.route('/load-sample')
def load_sample():
    """Load sample product data."""
    sample_path = Path("data/product_data.json")
    if sample_path.exists():
        with open(sample_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({"error": "Sample data not found"}), 404


@app.route('/deployment-info')
def deployment_info():
    """Return deployment information."""
    return jsonify({
        "platforms": {
            "render": {
                "name": "Render",
                "url": "https://render.com",
                "free_tier": True,
                "config_file": "render.yaml",
                "steps": [
                    "Go to render.com",
                    "Sign up with GitHub",
                    "New → Web Service",
                    "Connect repository",
                    "Deploy automatically"
                ]
            },
            "railway": {
                "name": "Railway",
                "url": "https://railway.app",
                "free_tier": True,
                "config_file": "railway.json",
                "steps": [
                    "Go to railway.app",
                    "Sign up with GitHub",
                    "New Project → Deploy from GitHub",
                    "Select repository",
                    "Auto-deploys"
                ]
            },
            "heroku": {
                "name": "Heroku",
                "url": "https://heroku.com",
                "free_tier": "Limited",
                "config_file": "Procfile",
                "steps": [
                    "Install Heroku CLI",
                    "Run: heroku create",
                    "Run: git push heroku main",
                    "Run: heroku open"
                ]
            },
            "flyio": {
                "name": "Fly.io",
                "url": "https://fly.io",
                "free_tier": True,
                "config_file": "fly.toml",
                "steps": [
                    "Install Fly CLI",
                    "Run: fly auth login",
                    "Run: fly launch",
                    "Run: fly open"
                ]
            }
        },
        "documentation": "Deployment configurations are pre-configured in the project files"
    })


if __name__ == '__main__':
    # Ensure outputs directory exists
    Path("outputs").mkdir(exist_ok=True)
    
    # Get port from environment variable (for cloud deployment) or use default
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(debug=debug, host='0.0.0.0', port=port)


