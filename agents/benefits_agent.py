"""Agent responsible for generating benefits content blocks."""

from typing import Dict, Any
from models.product_model import ProductModel


class BenefitsAgent:
    """Generates structured benefits content from product data."""
    
    def __init__(self):
        """Initialize the benefits agent."""
        pass
    
    def generate(self, product: ProductModel) -> Dict[str, Any]:
        """
        Generate benefits content block.
        
        Args:
            product: ProductModel instance
            
        Returns:
            Structured benefits content block
        """
        return {
            "primary_benefits": product.benefits,
            "benefit_details": {
                benefit: self._get_benefit_description(benefit, product)
                for benefit in product.benefits
            },
            "key_ingredients_contributing": {
                ingredient: self._get_ingredient_benefit(ingredient)
                for ingredient in product.key_ingredients
            }
        }
    
    def _get_benefit_description(self, benefit: str, product: ProductModel) -> str:
        """Get description for a specific benefit."""
        benefit_lower = benefit.lower()
        if "brightening" in benefit_lower:
            return f"{product.concentration} helps reduce dullness and improve skin radiance"
        elif "dark spots" in benefit_lower or "fade" in benefit_lower:
            return f"Regular use helps fade dark spots and hyperpigmentation"
        else:
            return f"Provides {benefit.lower()} benefits for the skin"
    
    def _get_ingredient_benefit(self, ingredient: str) -> str:
        """Get benefit description for an ingredient."""
        ingredient_lower = ingredient.lower()
        if "vitamin c" in ingredient_lower:
            return "Antioxidant protection and brightening"
        elif "hyaluronic acid" in ingredient_lower:
            return "Hydration and moisture retention"
        else:
            return "Supports skin health"


