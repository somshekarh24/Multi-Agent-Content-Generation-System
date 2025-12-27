"""Product data model with validation and normalization."""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class ProductModel:
    """Normalized product data model with validation."""
    
    product_name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: float
    
    def __post_init__(self):
        """Validate and normalize product data."""
        if not self.product_name or not self.product_name.strip():
            raise ValueError("product_name cannot be empty")
        
        if not self.concentration or not self.concentration.strip():
            raise ValueError("concentration cannot be empty")
        
        if not self.skin_type:
            raise ValueError("skin_type cannot be empty")
        
        if not self.key_ingredients:
            raise ValueError("key_ingredients cannot be empty")
        
        if not self.benefits:
            raise ValueError("benefits cannot be empty")
        
        if not self.how_to_use or not self.how_to_use.strip():
            raise ValueError("how_to_use cannot be empty")
        
        if self.price < 0:
            raise ValueError("price cannot be negative")
        
        # Normalize string fields
        self.product_name = self.product_name.strip()
        self.concentration = self.concentration.strip()
        self.how_to_use = self.how_to_use.strip()
        self.side_effects = self.side_effects.strip() if self.side_effects else ""
        
        # Normalize list fields
        self.skin_type = [s.strip() for s in self.skin_type if s.strip()]
        self.key_ingredients = [i.strip() for i in self.key_ingredients if i.strip()]
        self.benefits = [b.strip() for b in self.benefits if b.strip()]
    
    def to_dict(self) -> dict:
        """Convert model to dictionary."""
        return {
            "product_name": self.product_name,
            "concentration": self.concentration,
            "skin_type": self.skin_type,
            "key_ingredients": self.key_ingredients,
            "benefits": self.benefits,
            "how_to_use": self.how_to_use,
            "side_effects": self.side_effects,
            "price": self.price
        }


