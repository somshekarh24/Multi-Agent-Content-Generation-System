"""Pipeline orchestrator that controls multi-agent execution flow."""

from typing import Dict, Any
import json
from pathlib import Path

from models.product_model import ProductModel
from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.benefits_agent import BenefitsAgent
from agents.usage_agent import UsageAgent
from agents.safety_agent import SafetyAgent
from agents.price_agent import PriceAgent
from agents.comparison_agent import ComparisonAgent
from agents.page_assembly_agent import PageAssemblyAgent


class PipelineOrchestrator:
    """Orchestrates the multi-agent content generation pipeline."""
    
    def __init__(self):
        """Initialize the orchestrator with all agents."""
        self.parser_agent = ProductParserAgent()
        self.question_agent = QuestionGeneratorAgent()
        self.benefits_agent = BenefitsAgent()
        self.usage_agent = UsageAgent()
        self.safety_agent = SafetyAgent()
        self.price_agent = PriceAgent()
        self.comparison_agent = ComparisonAgent()
        self.assembly_agent = PageAssemblyAgent()
    
    def execute(self, raw_product_data: Dict[str, Any], output_dir: str = "outputs") -> Dict[str, str]:
        """
        Execute the complete pipeline.
        
        Args:
            raw_product_data: Raw JSON product data
            output_dir: Directory to save output files
            
        Returns:
            Dictionary with paths to generated output files
        """
        # Step 1: Parse raw data into ProductModel
        product = self.parser_agent.parse(raw_product_data)
        
        # Step 2: Generate questions
        questions = self.question_agent.generate(product)
        
        # Step 3: Generate content blocks
        benefits = self.benefits_agent.generate(product)
        usage = self.usage_agent.generate(product)
        safety = self.safety_agent.generate(product)
        price = self.price_agent.generate(product)
        
        # Step 4: Generate comparison
        comparison_data = self.comparison_agent.generate(product)
        
        # Step 5: Assemble pages
        faq_page = self.assembly_agent.assemble_faq_page(
            product.product_name,
            questions
        )
        
        product_page = self.assembly_agent.assemble_product_page(
            product.product_name,
            benefits,
            usage,
            safety,
            price
        )
        
        comparison_page = self.assembly_agent.assemble_comparison_page(
            comparison_data
        )
        
        # Step 6: Save outputs
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        faq_path = output_path / "faq.json"
        product_path = output_path / "product_page.json"
        comparison_path = output_path / "comparison_page.json"
        
        with open(faq_path, 'w', encoding='utf-8') as f:
            json.dump(faq_page, f, indent=2, ensure_ascii=False)
        
        with open(product_path, 'w', encoding='utf-8') as f:
            json.dump(product_page, f, indent=2, ensure_ascii=False)
        
        with open(comparison_path, 'w', encoding='utf-8') as f:
            json.dump(comparison_page, f, indent=2, ensure_ascii=False)
        
        return {
            "faq": str(faq_path),
            "product_page": str(product_path),
            "comparison_page": str(comparison_path)
        }
    
    def get_execution_flow(self) -> Dict[str, Any]:
        """
        Get the execution flow diagram.
        
        Returns:
            Dictionary describing the execution flow
        """
        return {
            "pipeline_steps": [
                {
                    "step": 1,
                    "agent": "ProductParserAgent",
                    "input": "raw_product_data (dict)",
                    "output": "ProductModel",
                    "description": "Parse and validate raw JSON data"
                },
                {
                    "step": 2,
                    "agent": "QuestionGeneratorAgent",
                    "input": "ProductModel",
                    "output": "structured_questions (dict)",
                    "description": "Generate categorized questions"
                },
                {
                    "step": 3,
                    "agents": [
                        "BenefitsAgent",
                        "UsageAgent",
                        "SafetyAgent",
                        "PriceAgent"
                    ],
                    "input": "ProductModel",
                    "output": "content_blocks (dict)",
                    "description": "Generate content blocks in parallel"
                },
                {
                    "step": 4,
                    "agent": "ComparisonAgent",
                    "input": "ProductModel",
                    "output": "comparison_data (dict)",
                    "description": "Compare Product A vs Product B"
                },
                {
                    "step": 5,
                    "agent": "PageAssemblyAgent",
                    "input": "templates + content_blocks",
                    "output": "complete_pages (dict)",
                    "description": "Assemble final JSON pages"
                },
                {
                    "step": 6,
                    "action": "Save outputs",
                    "input": "complete_pages",
                    "output": "JSON files",
                    "description": "Write JSON files to outputs/ directory"
                }
            ],
            "data_flow": {
                "raw_data": "ProductParserAgent",
                "ProductModel": [
                    "QuestionGeneratorAgent",
                    "BenefitsAgent",
                    "UsageAgent",
                    "SafetyAgent",
                    "PriceAgent",
                    "ComparisonAgent"
                ],
                "content_blocks": "PageAssemblyAgent",
                "final_pages": "outputs/"
            }
        }


