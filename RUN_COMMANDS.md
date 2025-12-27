# Run Commands & Testing Guide

## 🚀 Quick Commands

### Install Dependencies (First Time)
```bash
pip install -r requirements.txt
```

### Run Web Interface
```bash
python app.py
```
Then open: **http://localhost:5000**

### Run CLI Mode
```bash
python main.py
```

### Run Tests
```bash
python test_system.py
```

---

## ✅ How to Test/Verify the System

### Method 1: Automated Test Suite (Recommended)

```bash
python test_system.py
```

**Expected Output:**
```
============================================================
MULTI-AGENT SYSTEM TEST SUITE
============================================================
Testing ProductModel...
[PASS] ProductModel validation passed

Testing ProductParserAgent...
[PASS] ProductParserAgent working correctly

Testing Individual Agents...
[PASS] QuestionGeneratorAgent working correctly
[PASS] BenefitsAgent working correctly
[PASS] UsageAgent working correctly
[PASS] SafetyAgent working correctly
[PASS] PriceAgent working correctly
[PASS] ComparisonAgent working correctly

Testing Full Pipeline...
[PASS] Full pipeline executed successfully

Testing Output Files Structure...
[PASS] faq.json structure is valid
[PASS] product_page.json structure is valid
[PASS] comparison_page.json structure is valid

============================================================
TEST SUMMARY
============================================================
ProductModel: [PASS]
ProductParserAgent: [PASS]
Individual Agents: [PASS]
Full Pipeline: [PASS]
Output Files: [PASS]

Total: 5/5 tests passed

[SUCCESS] All tests passed! System is working correctly.
```

**✅ Success Criteria:** All 5 tests show `[PASS]`

---

### Method 2: Manual Verification

#### Step 1: Check Output Files Exist

**Windows:**
```bash
dir outputs\*.json
```

**Linux/Mac:**
```bash
ls outputs/*.json
```

**Expected:** 3 files
- `faq.json`
- `product_page.json`
- `comparison_page.json`

#### Step 2: Validate JSON Format

**Windows:**
```bash
python -m json.tool outputs\faq.json
```

**Linux/Mac:**
```bash
python -m json.tool outputs/faq.json
```

**Expected:** JSON content displayed without errors

#### Step 3: Check File Contents

Open any output file and verify:
- ✅ Valid JSON structure
- ✅ Contains `product_name` field
- ✅ Contains `metadata` field
- ✅ Non-empty content

---

### Method 3: Test Web Interface

1. **Start the server:**
   ```bash
   python app.py
   ```

2. **Expected output:**
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

3. **Open browser:** http://localhost:5000

4. **Test steps:**
   - ✅ Page loads without errors
   - ✅ Click "Load Sample Data" - form populates
   - ✅ Click "Generate Content" - shows loading, then results
   - ✅ All 3 tabs (FAQ, Product Page, Comparison) show JSON
   - ✅ Download buttons work for each JSON file

---

## 📋 Complete Testing Checklist

Use this checklist to verify everything:

- [ ] **Dependencies installed**
  ```bash
  pip install -r requirements.txt
  ```

- [ ] **Test suite passes**
  ```bash
  python test_system.py
  ```
  Result: `[SUCCESS] All tests passed!`

- [ ] **CLI mode works**
  ```bash
  python main.py
  ```
  Result: Shows success message and file paths

- [ ] **Output files generated**
  - Check `outputs/` directory
  - Verify 3 JSON files exist

- [ ] **JSON files are valid**
  ```bash
  python -m json.tool outputs\faq.json
  ```
  Result: No errors, JSON displayed

- [ ] **Web interface starts**
  ```bash
  python app.py
  ```
  Result: Server starts on port 5000

- [ ] **Web interface functional**
  - Open http://localhost:5000
  - Form works
  - Content generation works
  - Downloads work

---

## 🔍 Troubleshooting

### Issue: ModuleNotFoundError

**Solution:**
```bash
# Make sure you're in the project directory
cd Multi-Agent

# Install dependencies
pip install -r requirements.txt
```

### Issue: Test fails

**Check:**
1. Are you in the project root directory?
2. Does `data/product_data.json` exist?
3. Does `outputs/` directory exist?

**Fix:**
```bash
# Create outputs directory if missing
mkdir outputs
```

### Issue: Port 5000 already in use

**Solution:** Edit `app.py`, change:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
to:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: Flask not found

**Solution:**
```bash
pip install Flask
```

---

## 📊 Expected Results

### CLI Output (`python main.py`)
```
Starting multi-agent content generation pipeline...

Pipeline execution completed successfully!

Generated output files:
  - faq: outputs\faq.json
  - product_page: outputs\product_page.json
  - comparison_page: outputs\comparison_page.json

Execution flow:
  Step 1: ProductParserAgent
  Step 2: QuestionGeneratorAgent
  Step 3: ['BenefitsAgent', 'UsageAgent', 'SafetyAgent', 'PriceAgent']
  Step 4: ComparisonAgent
  Step 5: PageAssemblyAgent
  Step 6: Save outputs
```

### Test Suite Output (`python test_system.py`)
```
Total: 5/5 tests passed
[SUCCESS] All tests passed! System is working correctly.
```

### Web Server Output (`python app.py`)
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🎯 Quick Test Commands

Copy-paste these to quickly verify:

```bash
# 1. Run test suite
python test_system.py

# 2. Run CLI
python main.py

# 3. Check outputs (Windows)
dir outputs\*.json

# 4. Validate JSON (Windows)
python -m json.tool outputs\faq.json
```

If all commands succeed → ✅ System is working correctly!

---

## 📝 Summary

**To run the system:**
- Web: `python app.py` → http://localhost:5000
- CLI: `python main.py`

**To test the system:**
- Automated: `python test_system.py`
- Manual: Check `outputs/` directory for 3 JSON files

**Success indicator:**
- All tests pass
- 3 JSON files generated
- No error messages


