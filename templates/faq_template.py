"""FAQ page template definition."""

from typing import Dict, Any, List


class FAQTemplate:
    """Template structure for FAQ pages."""
    
    @staticmethod
    def get_structure() -> Dict[str, Any]:
        """
        Get the structure definition for FAQ pages.
        
        Returns:
            Template structure with fields, rules, and dependencies
        """
        return {
            "template_name": "faq_page",
            "required_fields": [
                "product_name",
                "questions",
                "metadata"
            ],
            "optional_fields": [
                "introduction",
                "categories"
            ],
            "field_rules": {
                "product_name": {
                    "type": "string",
                    "required": True,
                    "description": "Name of the product"
                },
                "questions": {
                    "type": "object",
                    "required": True,
                    "structure": {
                        "total_count": "integer",
                        "categories": "object with category names as keys"
                    }
                },
                "metadata": {
                    "type": "object",
                    "required": True,
                    "fields": ["generated_at", "version"]
                }
            },
            "dependencies": {
                "questions": {
                    "source": "QuestionGeneratorAgent",
                    "required": True
                }
            },
            "validation_rules": [
                "questions.total_count must be >= 15",
                "questions.categories must have at least 3 categories"
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
        structure = FAQTemplate.get_structure()
        
        # Check required fields
        for field in structure["required_fields"]:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate questions structure
        if "questions" in data:
            questions = data["questions"]
            if "total_count" not in questions:
                raise ValueError("questions must have total_count")
            if questions["total_count"] < 15:
                raise ValueError("questions.total_count must be >= 15")
            if "categories" not in questions:
                raise ValueError("questions must have categories")
            if len(questions["categories"]) < 3:
                raise ValueError("questions.categories must have at least 3 categories")
        
        return True


