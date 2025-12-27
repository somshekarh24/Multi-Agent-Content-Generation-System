"""Agent responsible for parsing raw JSON data into ProductModel."""

import json
from typing import Dict, Any
from models.product_model import ProductModel


class ProductParserAgent:
    """Parses raw JSON product data into validated ProductModel."""
    
    def __init__(self):
        """Initialize the parser agent."""
        pass
    
    def parse(self, raw_data: Dict[str, Any]) -> ProductModel:
        """
        Parse raw JSON data into ProductModel.
        
        Args:
            raw_data: Dictionary containing product data
            
        Returns:
            Validated ProductModel instance
            
        Raises:
            ValueError: If data is invalid or missing required fields
        """
        try:
            # Extract and validate required fields
            product = ProductModel(
                product_name=raw_data.get("product_name", ""),
                concentration=raw_data.get("concentration", ""),
                skin_type=raw_data.get("skin_type", []),
                key_ingredients=raw_data.get("key_ingredients", []),
                benefits=raw_data.get("benefits", []),
                how_to_use=raw_data.get("how_to_use", ""),
                side_effects=raw_data.get("side_effects", ""),
                price=float(raw_data.get("price", 0))
            )
            
            return product
            
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid product data: {e}")
    
    def parse_from_json_string(self, json_string: str) -> ProductModel:
        """
        Parse JSON string into ProductModel.
        
        Args:
            json_string: JSON string containing product data
            
        Returns:
            Validated ProductModel instance
        """
        raw_data = json.loads(json_string)
        return self.parse(raw_data)


