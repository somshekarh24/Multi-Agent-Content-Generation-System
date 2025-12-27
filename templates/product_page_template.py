"""Product page template definition."""

from typing import Dict, Any


class ProductPageTemplate:
    """Template structure for product pages."""
    
    @staticmethod
    def get_structure() -> Dict[str, Any]:
        """
        Get the structure definition for product pages.
        
        Returns:
            Template structure with fields, rules, and dependencies
        """
        return {
            "template_name": "product_page",
            "required_fields": [
                "product_name",
                "benefits",
                "usage",
                "safety",
                "price",
                "metadata"
            ],
            "optional_fields": [
                "introduction",
                "key_ingredients"
            ],
            "field_rules": {
                "product_name": {
                    "type": "string",
                    "required": True
                },
                "benefits": {
                    "type": "object",
                    "required": True,
                    "source": "BenefitsAgent"
                },
                "usage": {
                    "type": "object",
                    "required": True,
                    "source": "UsageAgent"
                },
                "safety": {
                    "type": "object",
                    "required": True,
                    "source": "SafetyAgent"
                },
                "price": {
                    "type": "object",
                    "required": True,
                    "source": "PriceAgent"
                },
                "metadata": {
                    "type": "object",
                    "required": True,
                    "fields": ["generated_at", "version"]
                }
            },
            "dependencies": {
                "benefits": {
                    "source": "BenefitsAgent",
                    "required": True
                },
                "usage": {
                    "source": "UsageAgent",
                    "required": True
                },
                "safety": {
                    "source": "SafetyAgent",
                    "required": True
                },
                "price": {
                    "source": "PriceAgent",
                    "required": True
                }
            },
            "validation_rules": [
                "All content blocks must be non-empty objects",
                "price.price must be a positive number"
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
        structure = ProductPageTemplate.get_structure()
        
        # Check required fields
        for field in structure["required_fields"]:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate content blocks
        content_blocks = ["benefits", "usage", "safety", "price"]
        for block in content_blocks:
            if not isinstance(data.get(block), dict) or not data[block]:
                raise ValueError(f"{block} must be a non-empty object")
        
        # Validate price
        if "price" in data and "price" in data["price"]:
            price_value = data["price"]["price"]
            if not isinstance(price_value, (int, float)) or price_value <= 0:
                raise ValueError("price.price must be a positive number")
        
        return True


