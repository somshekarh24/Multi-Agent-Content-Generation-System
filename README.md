# Multi-Agent Content Generation System

A production-style, multi-agent system for generating structured JSON content from product data.

## 🚀 Quick Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Deploy to Railway](https://railway.app/button.svg)](https://railway.app/new)

## Overview

This system demonstrates true agentic architecture with:
- Clear agent boundaries and single responsibilities
- No shared global state
- Explicit data flow between agents
- Template-based page assembly
- Machine-readable JSON outputs only

## Project Structure

```
Multi-Agent/
├── agents/              # Individual agent implementations
├── models/              # Data models (ProductModel)
├── templates/           # Template definitions
├── orchestrator/        # Pipeline orchestration
├── data/               # Input data
├── outputs/            # Generated JSON files
└── docs/               # Documentation
```

## Quick Start

### Option 1: Web Interface (Recommended)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the web server:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   - Navigate to `http://localhost:5000`
   - Fill in the product information form
   - Click "Generate Content" to see the results
   - Download JSON files directly from the interface

### Option 2: Command Line

1. **Install Python 3.7+** (no external dependencies required for CLI)

2. **Run the system:**
   ```bash
   python main.py
   ```

3. **Check outputs:**
   - `outputs/faq.json` - FAQ page with categorized questions
   - `outputs/product_page.json` - Complete product information
   - `outputs/comparison_page.json` - Product comparison

## System Architecture

### Agents

- **ProductParserAgent**: Parses raw JSON → ProductModel
- **QuestionGeneratorAgent**: Generates 15+ categorized questions
- **BenefitsAgent**: Generates benefits content
- **UsageAgent**: Generates usage instructions
- **SafetyAgent**: Generates safety information
- **PriceAgent**: Generates price information
- **ComparisonAgent**: Compares Product A vs Product B
- **PageAssemblyAgent**: Assembles final JSON pages

### Data Flow

```
Raw JSON → ProductParserAgent → ProductModel
                                    ↓
        ┌───────────────────────────┼───────────────────────────┐
        ↓                           ↓                           ↓
QuestionGeneratorAgent    Content Logic Agents      ComparisonAgent
        ↓                           ↓                           ↓
        └───────────────────────────┼───────────────────────────┘
                                    ↓
                            PageAssemblyAgent
                                    ↓
                            JSON Output Files
```

## Input Data Format

The system expects product data in the following JSON format:

```json
{
  "product_name": "Product Name",
  "concentration": "Concentration details",
  "skin_type": ["Type1", "Type2"],
  "key_ingredients": ["Ingredient1", "Ingredient2"],
  "benefits": ["Benefit1", "Benefit2"],
  "how_to_use": "Usage instructions",
  "side_effects": "Side effects description",
  "price": 699
}
```

## Output Files

### FAQ Page (`outputs/faq.json`)
- Categorized questions (informational, safety, usage, purchase, comparison)
- Minimum 15 questions
- Structured JSON format

### Product Page (`outputs/product_page.json`)
- Benefits information
- Usage instructions
- Safety information
- Price details
- Complete product metadata

### Comparison Page (`outputs/comparison_page.json`)
- Product A vs Product B comparison
- Price, concentration, ingredients, skin type, benefits comparison
- Recommendation summary

## Key Features

✅ **True Multi-Agent Architecture**: Each agent has single responsibility  
✅ **No Shared State**: Explicit data flow, no global variables  
✅ **Template System**: Structure definitions separate from logic  
✅ **Validation**: All outputs validated against templates  
✅ **Deterministic**: Consistent outputs for same inputs  
✅ **Extensible**: Easy to add new agents or templates  

## Documentation

See `docs/projectdocumentation.md` for detailed architecture documentation.

## Requirements

- Python 3.7+
- Flask 3.0.0+ (for web interface)
- Standard library only (for CLI mode)

### Installation

```bash
pip install -r requirements.txt
```

## 🚀 Deployment

### Quick Deploy Options

**Render (Recommended - Free Tier):**
1. Go to [render.com](https://render.com)
2. New → Web Service → Connect GitHub
3. Deploy (auto-detects configuration)

**Railway (Fastest):**
1. Go to [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Done!

**Heroku:**
```bash
heroku create your-app-name
git push heroku main
```

**Docker:**
```bash
docker build -t multi-agent-app .
docker run -p 5000:5000 multi-agent-app
```

### Deployment Files Included

- ✅ `Procfile` (Heroku)
- ✅ `Dockerfile` (Docker)
- ✅ `render.yaml` (Render)
- ✅ `railway.json` (Railway)
- ✅ `fly.toml` (Fly.io)

**Deployment configurations are pre-configured. Connect your repository to any platform and deploy.**

## Testing the System

### Quick Test

Run the automated test suite to verify everything is working:

```bash
python test_system.py
```

This will test:
- ✓ ProductModel validation
- ✓ ProductParserAgent
- ✓ Individual agents (all 6 content agents)
- ✓ Full pipeline execution
- ✓ Output file structure and validation

### Manual Testing

#### Test 1: CLI Mode
```bash
python main.py
```
**Expected output:**
- Success message
- List of generated files
- Execution flow steps

**Verify:**
- Check `outputs/` directory has 3 JSON files
- Open files and verify they contain valid JSON

#### Test 2: Web Interface
```bash
python app.py
```
**Expected output:**
- Server starts on `http://localhost:5000`
- No error messages

**Verify:**
1. Open browser to `http://localhost:5000`
2. Click "Load Sample Data" - form should populate
3. Click "Generate Content" - should see loading, then results
4. Check all 3 tabs show JSON content
5. Try downloading each JSON file

#### Test 3: Verify Output Files

Check that output files exist and are valid JSON:

```bash
# Windows PowerShell
Get-ChildItem outputs\*.json | ForEach-Object { Write-Host "Checking $($_.Name)..."; python -m json.tool $_.FullName > $null; if ($?) { Write-Host "✓ Valid JSON" } else { Write-Host "✗ Invalid JSON" } }

# Linux/Mac
for file in outputs/*.json; do echo "Checking $file..."; python -m json.tool "$file" > /dev/null && echo "✓ Valid JSON" || echo "✗ Invalid JSON"; done
```

### Expected Test Results

When running `python test_system.py`, you should see:

```
============================================================
MULTI-AGENT SYSTEM TEST SUITE
============================================================
Testing ProductModel...
✓ ProductModel validation passed

Testing ProductParserAgent...
✓ ProductParserAgent working correctly

Testing Individual Agents...
✓ QuestionGeneratorAgent working correctly
✓ BenefitsAgent working correctly
✓ UsageAgent working correctly
✓ SafetyAgent working correctly
✓ PriceAgent working correctly
✓ ComparisonAgent working correctly

Testing Full Pipeline...
✓ Full pipeline executed successfully

Testing Output Files Structure...
✓ faq.json structure is valid
✓ product_page.json structure is valid
✓ comparison_page.json structure is valid

============================================================
TEST SUMMARY
============================================================
ProductModel: ✓ PASSED
ProductParserAgent: ✓ PASSED
Individual Agents: ✓ PASSED
Full Pipeline: ✓ PASSED
Output Files: ✓ PASSED

Total: 5/5 tests passed

🎉 All tests passed! System is working correctly.
```

## Troubleshooting

### Common Issues

**Issue: ModuleNotFoundError**
- Solution: Make sure you're in the project root directory
- Run: `cd Multi-Agent` then try again

**Issue: Flask not found**
- Solution: Install dependencies
- Run: `pip install -r requirements.txt`

**Issue: Port 5000 already in use**
- Solution: Change port in `app.py` (line with `app.run(port=5000)`)
- Or stop the process using port 5000

**Issue: Output files not generated**
- Solution: Check `outputs/` directory exists
- Run: `mkdir outputs` if needed

## License

This is a demonstration project for multi-agent system architecture.

