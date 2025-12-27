"""Agent responsible for generating categorized user questions."""

from typing import List, Dict, Any
from models.product_model import ProductModel


class QuestionGeneratorAgent:
    """Generates categorized questions based on product data."""
    
    def __init__(self):
        """Initialize the question generator agent."""
        pass
    
    def generate(self, product: ProductModel) -> Dict[str, Any]:
        """
        Generate categorized questions for the product.
        
        Args:
            product: ProductModel instance
            
        Returns:
            Dictionary with categorized questions in structured format
        """
        questions = {
            "informational": [
                f"What is {product.product_name}?",
                f"What is the concentration of Vitamin C in {product.product_name}?",
                f"Which skin types is {product.product_name} suitable for?",
                f"What are the key ingredients in {product.product_name}?",
                f"What are the main benefits of {product.product_name}?"
            ],
            "safety": [
                f"Are there any side effects of using {product.product_name}?",
                f"Is {product.product_name} safe for sensitive skin?",
                f"Can I use {product.product_name} if I have oily skin?",
                f"Should I do a patch test before using {product.product_name}?",
                f"What should I do if I experience tingling with {product.product_name}?"
            ],
            "usage": [
                f"How do I use {product.product_name}?",
                f"When should I apply {product.product_name}?",
                f"How many drops of {product.product_name} should I use?",
                f"Can I use {product.product_name} at night?",
                f"Should I apply sunscreen after using {product.product_name}?"
            ],
            "purchase": [
                f"What is the price of {product.product_name}?",
                f"Is {product.product_name} worth the price?",
                f"Where can I buy {product.product_name}?",
                f"Are there any discounts available for {product.product_name}?"
            ],
            "comparison": [
                f"How does {product.product_name} compare to other Vitamin C serums?",
                f"What makes {product.product_name} different from other products?",
                f"Is {product.product_name} better than Product B?"
            ]
        }
        
        # Structure the output
        structured_questions = {
            "total_count": sum(len(q_list) for q_list in questions.values()),
            "categories": {
                category: {
                    "count": len(q_list),
                    "questions": q_list
                }
                for category, q_list in questions.items()
            }
        }
        
        return structured_questions


