"""Agent responsible for assembling pages from templates and content blocks."""

from typing import Dict, Any
from datetime import datetime
from templates.faq_template import FAQTemplate
from templates.product_page_template import ProductPageTemplate
from templates.comparison_page_template import ComparisonPageTemplate


class PageAssemblyAgent:
    """Assembles final JSON pages from templates and content blocks."""
    
    def __init__(self):
        """Initialize the page assembly agent."""
        self.version = "1.0.0"
    
    def assemble_faq_page(
        self,
        product_name: str,
        questions: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assemble FAQ page from questions.
        
        Args:
            product_name: Name of the product
            questions: Structured questions from QuestionGeneratorAgent
            
        Returns:
            Complete FAQ page JSON structure
        """
        page = {
            "product_name": product_name,
            "questions": questions,
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "version": self.version
            }
        }
        
        # Validate against template
        FAQTemplate.validate(page)
        
        return page
    
    def assemble_product_page(
        self,
        product_name: str,
        benefits: Dict[str, Any],
        usage: Dict[str, Any],
        safety: Dict[str, Any],
        price: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assemble product page from content blocks.
        
        Args:
            product_name: Name of the product
            benefits: Benefits content from BenefitsAgent
            usage: Usage content from UsageAgent
            safety: Safety content from SafetyAgent
            price: Price content from PriceAgent
            
        Returns:
            Complete product page JSON structure
        """
        page = {
            "product_name": product_name,
            "benefits": benefits,
            "usage": usage,
            "safety": safety,
            "price": price,
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "version": self.version
            }
        }
        
        # Validate against template
        ProductPageTemplate.validate(page)
        
        return page
    
    def assemble_comparison_page(
        self,
        comparison_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assemble comparison page from comparison data.
        
        Args:
            comparison_data: Comparison content from ComparisonAgent
            
        Returns:
            Complete comparison page JSON structure
        """
        page = {
            "product_a": comparison_data["product_a"],
            "product_b": comparison_data["product_b"],
            "comparison_points": comparison_data["comparison_points"],
            "recommendation": comparison_data["recommendation"],
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "version": self.version
            }
        }
        
        # Validate against template
        ComparisonPageTemplate.validate(page)
        
        return page


