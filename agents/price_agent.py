"""Agent responsible for generating price-related content blocks."""

from typing import Dict, Any
from models.product_model import ProductModel


class PriceAgent:
    """Generates structured price information from product data."""
    
    def __init__(self):
        """Initialize the price agent."""
        pass
    
    def generate(self, product: ProductModel) -> Dict[str, Any]:
        """
        Generate price content block.
        
        Args:
            product: ProductModel instance
            
        Returns:
            Structured price content block
        """
        return {
            "price": product.price,
            "currency": "INR",
            "price_category": self._categorize_price(product.price),
            "value_assessment": self._assess_value(product),
            "price_per_ml": None,  # Would require volume information
            "comparison_note": self._generate_comparison_note(product.price)
        }
    
    def _categorize_price(self, price: float) -> str:
        """Categorize price range."""
        if price < 500:
            return "Budget-friendly"
        elif price < 1000:
            return "Mid-range"
        elif price < 2000:
            return "Premium"
        else:
            return "Luxury"
    
    def _assess_value(self, product: ProductModel) -> str:
        """Assess value proposition."""
        price = product.price
        ingredient_count = len(product.key_ingredients)
        benefit_count = len(product.benefits)
        
        if price < 1000 and ingredient_count >= 2 and benefit_count >= 2:
            return "Good value for money with multiple active ingredients"
        elif price >= 1000:
            return "Premium pricing justified by quality ingredients"
        else:
            return "Reasonable pricing for the benefits offered"
    
    def _generate_comparison_note(self, price: float) -> str:
        """Generate price comparison note."""
        if price < 500:
            return "Competitively priced in the budget segment"
        elif price < 1000:
            return "Positioned in the mid-range market segment"
        else:
            return "Positioned in the premium market segment"


