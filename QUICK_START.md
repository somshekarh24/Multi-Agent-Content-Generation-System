# Quick Start Guide

## 🚀 Commands to Run

### 1. Install Dependencies (First Time Only)

```bash
pip install -r requirements.txt
```

### 2. Run the System

**Option A: Web Interface (Recommended)**
```bash
python app.py
```
Then open: **http://localhost:5000**

**Option B: Command Line**
```bash
python main.py
```

### 3. Test the System

```bash
python test_system.py
```

---

## ✅ How to Verify It's Working

### Quick Verification (30 seconds)

1. **Run the test suite:**
   ```bash
   python test_system.py
   ```
   
2. **Check the output:**
   - Should see: `🎉 All tests passed! System is working correctly.`
   - All 5 tests should show `✓ PASSED`

### Detailed Verification

#### Step 1: Check Output Files Exist

```bash
# Windows
dir outputs\*.json

# Linux/Mac
ls outputs/*.json
```

**Expected:** 3 files
- `faq.json`
- `product_page.json`
- `comparison_page.json`

#### Step 2: Verify JSON is Valid

```bash
# Windows PowerShell
python -m json.tool outputs\faq.json

# Linux/Mac
python -m json.tool outputs/faq.json
```

**Expected:** JSON content displayed without errors

#### Step 3: Check File Contents

Open any output file and verify it has:
- Valid JSON structure
- Required fields (product_name, metadata, etc.)
- Non-empty content

#### Step 4: Test Web Interface

1. Start server: `python app.py`
2. Open browser: `http://localhost:5000`
3. Click "Load Sample Data"
4. Click "Generate Content"
5. Verify all 3 tabs show JSON content

---

## 📋 Checklist

Use this checklist to verify everything works:

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Test suite passes (`python test_system.py`)
- [ ] CLI mode works (`python main.py`)
- [ ] Output files generated in `outputs/` directory
- [ ] All 3 JSON files are valid JSON
- [ ] Web interface starts (`python app.py`)
- [ ] Web interface loads in browser
- [ ] Can generate content via web form
- [ ] Can download JSON files from web interface

---

## 🔍 What to Look For

### ✅ Success Indicators

- Test suite shows all tests passed
- No error messages in terminal
- 3 JSON files in `outputs/` directory
- Web interface loads without errors
- JSON files contain structured data

### ❌ Failure Indicators

- Import errors (missing modules)
- File not found errors
- Invalid JSON in output files
- Web server won't start
- Empty output files

---

## 🆘 If Something Doesn't Work

1. **Check Python version:**
   ```bash
   python --version
   ```
   Should be 3.7 or higher

2. **Reinstall dependencies:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Check you're in the right directory:**
   ```bash
   # Should see files like main.py, app.py, agents/, etc.
   dir
   ```

4. **Run test suite for detailed errors:**
   ```bash
   python test_system.py
   ```

---

## 📊 Expected Outputs

### CLI Mode (`python main.py`)
```
Starting multi-agent content generation pipeline...

Pipeline execution completed successfully!

Generated output files:
  - faq: outputs\faq.json
  - product_page: outputs\product_page.json
  - comparison_page: outputs\comparison_page.json
```

### Test Suite (`python test_system.py`)
```
Total: 5/5 tests passed
🎉 All tests passed! System is working correctly.
```

### Web Interface (`python app.py`)
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🎯 Quick Test Commands

Copy-paste these commands to quickly verify everything:

```bash
# 1. Test the system
python test_system.py

# 2. Run CLI
python main.py

# 3. Check outputs exist
dir outputs\*.json  # Windows
ls outputs/*.json    # Linux/Mac

# 4. Validate JSON
python -m json.tool outputs\faq.json  # Windows
python -m json.tool outputs/faq.json  # Linux/Mac
```

If all commands succeed, your system is working correctly! ✅


