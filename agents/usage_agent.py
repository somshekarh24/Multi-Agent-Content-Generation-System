"""Agent responsible for generating usage content blocks."""

from typing import Dict, Any
from models.product_model import ProductModel


class UsageAgent:
    """Generates structured usage instructions from product data."""
    
    def __init__(self):
        """Initialize the usage agent."""
        pass
    
    def generate(self, product: ProductModel) -> Dict[str, Any]:
        """
        Generate usage content block.
        
        Args:
            product: ProductModel instance
            
        Returns:
            Structured usage content block
        """
        return {
            "instructions": product.how_to_use,
            "frequency": self._extract_frequency(product.how_to_use),
            "time_of_day": self._extract_time_of_day(product.how_to_use),
            "application_steps": self._parse_application_steps(product.how_to_use),
            "precautions": [
                "Apply to clean, dry skin",
                "Follow with sunscreen during daytime",
                "Start with lower frequency if you have sensitive skin"
            ],
            "compatible_skin_types": product.skin_type
        }
    
    def _extract_frequency(self, instructions: str) -> str:
        """Extract frequency information from instructions."""
        instructions_lower = instructions.lower()
        if "morning" in instructions_lower:
            return "Once daily (morning)"
        elif "night" in instructions_lower or "evening" in instructions_lower:
            return "Once daily (evening)"
        else:
            return "As directed"
    
    def _extract_time_of_day(self, instructions: str) -> str:
        """Extract time of day from instructions."""
        instructions_lower = instructions.lower()
        if "morning" in instructions_lower:
            return "morning"
        elif "night" in instructions_lower or "evening" in instructions_lower:
            return "evening"
        else:
            return "flexible"
    
    def _parse_application_steps(self, instructions: str) -> list:
        """Parse application steps from instructions."""
        steps = []
        if "drops" in instructions.lower():
            steps.append("Dispense 2-3 drops")
        steps.append("Apply to face and neck")
        if "sunscreen" in instructions.lower():
            steps.append("Follow with sunscreen")
        return steps


