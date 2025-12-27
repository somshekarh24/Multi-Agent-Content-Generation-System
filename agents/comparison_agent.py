"""Agent responsible for comparing products."""

from typing import Dict, Any
from models.product_model import ProductModel


class ComparisonAgent:
    """Generates structured product comparison content."""
    
    def __init__(self):
        """Initialize the comparison agent."""
        # Define fictional Product B internally
        self.product_b = ProductModel(
            product_name="RadiantGlow Vitamin C Serum",
            concentration="15% Vitamin C",
            skin_type=["Dry", "Normal"],
            key_ingredients=["Vitamin C", "Niacinamide", "Vitamin E"],
            benefits=["Anti-aging", "Even skin tone", "Hydration"],
            how_to_use="Apply 3-4 drops in the evening after cleansing",
            side_effects="May cause dryness in some users",
            price=899
        )
    
    def generate(self, product_a: ProductModel) -> Dict[str, Any]:
        """
        Generate comparison between Product A and Product B.
        
        Args:
            product_a: ProductModel instance (Product A)
            
        Returns:
            Structured comparison content block
        """
        return {
            "product_a": {
                "name": product_a.product_name,
                "concentration": product_a.concentration,
                "price": product_a.price,
                "key_ingredients": product_a.key_ingredients,
                "benefits": product_a.benefits,
                "skin_type": product_a.skin_type
            },
            "product_b": {
                "name": self.product_b.product_name,
                "concentration": self.product_b.concentration,
                "price": self.product_b.price,
                "key_ingredients": self.product_b.key_ingredients,
                "benefits": self.product_b.benefits,
                "skin_type": self.product_b.skin_type
            },
            "comparison_points": {
                "price": {
                    "product_a": product_a.price,
                    "product_b": self.product_b.price,
                    "difference": abs(product_a.price - self.product_b.price),
                    "winner": "product_a" if product_a.price < self.product_b.price else "product_b"
                },
                "concentration": {
                    "product_a": product_a.concentration,
                    "product_b": self.product_b.concentration,
                    "analysis": self._compare_concentration(product_a, self.product_b)
                },
                "ingredients": {
                    "product_a_count": len(product_a.key_ingredients),
                    "product_b_count": len(self.product_b.key_ingredients),
                    "common_ingredients": self._find_common_ingredients(product_a, self.product_b),
                    "unique_to_a": self._find_unique_ingredients(product_a, self.product_b),
                    "unique_to_b": self._find_unique_ingredients(self.product_b, product_a)
                },
                "skin_type_compatibility": {
                    "product_a": product_a.skin_type,
                    "product_b": self.product_b.skin_type,
                    "overlap": list(set(product_a.skin_type) & set(self.product_b.skin_type)),
                    "unique_to_a": list(set(product_a.skin_type) - set(self.product_b.skin_type)),
                    "unique_to_b": list(set(self.product_b.skin_type) - set(product_a.skin_type))
                },
                "benefits": {
                    "product_a": product_a.benefits,
                    "product_b": self.product_b.benefits,
                    "common_benefits": list(set(product_a.benefits) & set(self.product_b.benefits)),
                    "unique_to_a": list(set(product_a.benefits) - set(self.product_b.benefits)),
                    "unique_to_b": list(set(self.product_b.benefits) - set(product_a.benefits))
                }
            },
            "recommendation": self._generate_recommendation(product_a, self.product_b)
        }
    
    def _compare_concentration(self, product_a: ProductModel, product_b: ProductModel) -> str:
        """Compare Vitamin C concentrations."""
        conc_a = self._extract_percentage(product_a.concentration)
        conc_b = self._extract_percentage(product_b.concentration)
        
        if conc_a and conc_b:
            if conc_a > conc_b:
                return f"{product_a.product_name} has higher concentration ({conc_a}% vs {conc_b}%)"
            elif conc_b > conc_a:
                return f"{product_b.product_name} has higher concentration ({conc_b}% vs {conc_a}%)"
            else:
                return "Both products have similar concentration"
        return "Concentration comparison requires detailed analysis"
    
    def _extract_percentage(self, concentration: str) -> float:
        """Extract percentage value from concentration string."""
        try:
            import re
            match = re.search(r'(\d+)%', concentration)
            if match:
                return float(match.group(1))
        except:
            pass
        return None
    
    def _find_common_ingredients(self, product_a: ProductModel, product_b: ProductModel) -> list:
        """Find common ingredients between products."""
        ingredients_a = {i.lower() for i in product_a.key_ingredients}
        ingredients_b = {i.lower() for i in product_b.key_ingredients}
        common = ingredients_a & ingredients_b
        return list(common)
    
    def _find_unique_ingredients(self, product: ProductModel, other: ProductModel) -> list:
        """Find ingredients unique to first product."""
        ingredients_product = {i.lower() for i in product.key_ingredients}
        ingredients_other = {i.lower() for i in other.key_ingredients}
        unique = ingredients_product - ingredients_other
        return list(unique)
    
    def _generate_recommendation(self, product_a: ProductModel, product_b: ProductModel) -> str:
        """Generate comparison recommendation."""
        recommendations = []
        
        if product_a.price < product_b.price:
            recommendations.append(f"{product_a.product_name} is more budget-friendly")
        
        if len(product_b.key_ingredients) > len(product_a.key_ingredients):
            recommendations.append(f"{product_b.product_name} offers more active ingredients")
        
        if "Oily" in product_a.skin_type and "Oily" not in product_b.skin_type:
            recommendations.append(f"{product_a.product_name} is better suited for oily skin")
        
        if "Dry" in product_b.skin_type and "Dry" not in product_a.skin_type:
            recommendations.append(f"{product_b.product_name} is better suited for dry skin")
        
        if not recommendations:
            return "Both products have their strengths; choose based on specific skin needs"
        
        return "; ".join(recommendations)


