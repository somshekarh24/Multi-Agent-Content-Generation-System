"""Test script to verify the multi-agent system is working correctly."""

import json
import sys
from pathlib import Path
from orchestrator.pipeline_orchestrator import PipelineOrchestrator
from models.product_model import ProductModel

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def test_product_model():
    """Test ProductModel validation."""
    print("Testing ProductModel...")
    try:
        product = ProductModel(
            product_name="Test Product",
            concentration="10%",
            skin_type=["Oily"],
            key_ingredients=["Ingredient1"],
            benefits=["Benefit1"],
            how_to_use="Use daily",
            side_effects="None",
            price=100
        )
        print("[PASS] ProductModel validation passed")
        return True
    except Exception as e:
        print(f"[FAIL] ProductModel validation failed: {e}")
        return False


def test_parser_agent():
    """Test ProductParserAgent."""
    print("\nTesting ProductParserAgent...")
    try:
        from agents.product_parser_agent import ProductParserAgent
        parser = ProductParserAgent()
        test_data = {
            "product_name": "Test Product",
            "concentration": "10%",
            "skin_type": ["Oily"],
            "key_ingredients": ["Ingredient1"],
            "benefits": ["Benefit1"],
            "how_to_use": "Use daily",
            "side_effects": "None",
            "price": 100
        }
        product = parser.parse(test_data)
        assert isinstance(product, ProductModel)
        print("[PASS] ProductParserAgent working correctly")
        return True
    except Exception as e:
        print(f"[FAIL] ProductParserAgent failed: {e}")
        return False


def test_full_pipeline():
    """Test the complete pipeline."""
    print("\nTesting Full Pipeline...")
    try:
        # Load sample data
        data_path = Path("data/product_data.json")
        if not data_path.exists():
            print("✗ Sample data file not found")
            return False
        
        with open(data_path, 'r', encoding='utf-8') as f:
            product_data = json.load(f)
        
        # Run pipeline
        orchestrator = PipelineOrchestrator()
        output_files = orchestrator.execute(product_data, output_dir="outputs")
        
        # Verify outputs exist
        for page_type, file_path in output_files.items():
            path = Path(file_path)
            if not path.exists():
                print(f"[FAIL] Output file not created: {file_path}")
                return False
            
            # Verify JSON is valid
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not data:
                    print(f"[FAIL] Output file is empty: {file_path}")
                    return False
        
        print("[PASS] Full pipeline executed successfully")
        print(f"  Generated files: {list(output_files.values())}")
        return True
        
    except Exception as e:
        print(f"✗ Pipeline test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_output_files():
    """Test that output files have correct structure."""
    print("\nTesting Output Files Structure...")
    try:
        required_files = ["faq.json", "product_page.json", "comparison_page.json"]
        all_valid = True
        
        for filename in required_files:
            file_path = Path("outputs") / filename
            if not file_path.exists():
                print(f"[FAIL] {filename} not found")
                all_valid = False
                continue
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Basic structure checks
                if filename == "faq.json":
                    if "questions" not in data or "product_name" not in data:
                        print(f"[FAIL] {filename} missing required fields")
                        all_valid = False
                        continue
                    if data["questions"]["total_count"] < 15:
                        print(f"[FAIL] {filename} has less than 15 questions")
                        all_valid = False
                        continue
                
                elif filename == "product_page.json":
                    required_fields = ["product_name", "benefits", "usage", "safety", "price"]
                    if not all(field in data for field in required_fields):
                        print(f"[FAIL] {filename} missing required fields")
                        all_valid = False
                        continue
                
                elif filename == "comparison_page.json":
                    required_fields = ["product_a", "product_b", "comparison_points", "recommendation"]
                    if not all(field in data for field in required_fields):
                        print(f"[FAIL] {filename} missing required fields")
                        all_valid = False
                        continue
            
            print(f"[PASS] {filename} structure is valid")
        
        return all_valid
        
    except Exception as e:
        print(f"[FAIL] Output file test failed: {e}")
        return False


def test_agents():
    """Test individual agents."""
    print("\nTesting Individual Agents...")
    try:
        from agents.product_parser_agent import ProductParserAgent
        from agents.question_generator_agent import QuestionGeneratorAgent
        from agents.benefits_agent import BenefitsAgent
        from agents.usage_agent import UsageAgent
        from agents.safety_agent import SafetyAgent
        from agents.price_agent import PriceAgent
        from agents.comparison_agent import ComparisonAgent
        
        # Load sample data
        data_path = Path("data/product_data.json")
        with open(data_path, 'r', encoding='utf-8') as f:
            product_data = json.load(f)
        
        parser = ProductParserAgent()
        product = parser.parse(product_data)
        
        # Test each agent
        agents_to_test = [
            ("QuestionGeneratorAgent", QuestionGeneratorAgent()),
            ("BenefitsAgent", BenefitsAgent()),
            ("UsageAgent", UsageAgent()),
            ("SafetyAgent", SafetyAgent()),
            ("PriceAgent", PriceAgent()),
            ("ComparisonAgent", ComparisonAgent())
        ]
        
        all_passed = True
        for name, agent in agents_to_test:
            try:
                result = agent.generate(product)
                if not result:
                    print(f"[FAIL] {name} returned empty result")
                    all_passed = False
                else:
                    print(f"[PASS] {name} working correctly")
            except Exception as e:
                print(f"[FAIL] {name} failed: {e}")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"[FAIL] Agent test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("MULTI-AGENT SYSTEM TEST SUITE")
    print("=" * 60)
    
    tests = [
        ("ProductModel", test_product_model),
        ("ProductParserAgent", test_parser_agent),
        ("Individual Agents", test_agents),
        ("Full Pipeline", test_full_pipeline),
        ("Output Files", test_output_files)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n[FAIL] {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n[SUCCESS] All tests passed! System is working correctly.")
        return 0
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    exit(main())

