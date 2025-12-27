"""Comparison page template definition."""

from typing import Dict, Any


class ComparisonPageTemplate:
    """Template structure for comparison pages."""
    
    @staticmethod
    def get_structure() -> Dict[str, Any]:
        """
        Get the structure definition for comparison pages.
        
        Returns:
            Template structure with fields, rules, and dependencies
        """
        return {
            "template_name": "comparison_page",
            "required_fields": [
                "product_a",
                "product_b",
                "comparison_points",
                "recommendation",
                "metadata"
            ],
            "optional_fields": [
                "introduction",
                "summary"
            ],
            "field_rules": {
                "product_a": {
                    "type": "object",
                    "required": True,
                    "fields": ["name", "concentration", "price", "key_ingredients", "benefits", "skin_type"]
                },
                "product_b": {
                    "type": "object",
                    "required": True,
                    "fields": ["name", "concentration", "price", "key_ingredients", "benefits", "skin_type"]
                },
                "comparison_points": {
                    "type": "object",
                    "required": True,
                    "must_include": ["price", "concentration", "ingredients", "skin_type_compatibility", "benefits"]
                },
                "recommendation": {
                    "type": "string",
                    "required": True
                },
                "metadata": {
                    "type": "object",
                    "required": True,
                    "fields": ["generated_at", "version"]
                }
            },
            "dependencies": {
                "comparison_data": {
                    "source": "ComparisonAgent",
                    "required": True
                }
            },
            "validation_rules": [
                "Both product_a and product_b must have all required fields",
                "comparison_points must include at least 3 comparison categories",
                "recommendation must be a non-empty string"
            ]
        }
    
    @staticmethod
    def validate(data: Dict[str, Any]) -> bool:
        """
        Validate data against template structure.
        
        Args:
            data: Data to validate
            
        Returns:
            True if valid, raises ValueError if invalid
        """
        structure = ComparisonPageTemplate.get_structure()
        
        # Check required fields
        for field in structure["required_fields"]:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate product objects
        for product_key in ["product_a", "product_b"]:
            if product_key in data:
                product = data[product_key]
                required_fields = ["name", "concentration", "price", "key_ingredients", "benefits", "skin_type"]
                for field in required_fields:
                    if field not in product:
                        raise ValueError(f"{product_key}.{field} is required")
        
        # Validate comparison_points
        if "comparison_points" in data:
            comparison_points = data["comparison_points"]
            if len(comparison_points) < 3:
                raise ValueError("comparison_points must include at least 3 comparison categories")
        
        # Validate recommendation
        if "recommendation" in data:
            if not isinstance(data["recommendation"], str) or not data["recommendation"].strip():
                raise ValueError("recommendation must be a non-empty string")
        
        return True


