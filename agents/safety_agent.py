"""Agent responsible for generating safety content blocks."""

from typing import Dict, Any
from models.product_model import ProductModel


class SafetyAgent:
    """Generates structured safety information from product data."""
    
    def __init__(self):
        """Initialize the safety agent."""
        pass
    
    def generate(self, product: ProductModel) -> Dict[str, Any]:
        """
        Generate safety content block.
        
        Args:
            product: ProductModel instance
            
        Returns:
            Structured safety content block
        """
        return {
            "side_effects": product.side_effects,
            "safety_level": self._assess_safety_level(product),
            "skin_type_compatibility": {
                skin_type: self._assess_compatibility(skin_type, product)
                for skin_type in product.skin_type
            },
            "precautions": self._generate_precautions(product),
            "when_to_avoid": self._generate_avoidance_conditions(product)
        }
    
    def _assess_safety_level(self, product: ProductModel) -> str:
        """Assess overall safety level."""
        if "mild" in product.side_effects.lower() and "sensitive" in product.side_effects.lower():
            return "Generally safe, may cause mild reactions in sensitive skin"
        elif "tingling" in product.side_effects.lower():
            return "Safe with possible mild tingling sensation"
        else:
            return "Generally safe for indicated skin types"
    
    def _assess_compatibility(self, skin_type: str, product: ProductModel) -> str:
        """Assess compatibility for specific skin type."""
        skin_lower = skin_type.lower()
        if "sensitive" in skin_lower:
            return "Use with caution, perform patch test first"
        elif "oily" in skin_lower or "combination" in skin_lower:
            return "Well-suited for this skin type"
        else:
            return "Compatible with this skin type"
    
    def _generate_precautions(self, product: ProductModel) -> list:
        """Generate precautionary measures."""
        precautions = [
            "Perform a patch test before first use",
            "Avoid contact with eyes"
        ]
        
        if "sensitive" in product.side_effects.lower():
            precautions.append("Start with lower frequency if you have sensitive skin")
        
        if "vitamin c" in " ".join(product.key_ingredients).lower():
            precautions.append("Store in a cool, dark place to maintain efficacy")
        
        return precautions
    
    def _generate_avoidance_conditions(self, product: ProductModel) -> list:
        """Generate conditions when product should be avoided."""
        conditions = []
        
        if "sensitive" in product.side_effects.lower():
            conditions.append("Active skin irritation or open wounds")
        
        conditions.append("Known allergy to any ingredient")
        
        return conditions


