"""
recipe.py - v1
Functionality:
- Models a single recipe
- Stores title, ingredients, steps, category
- Can serialize itself to dict
"""

class Recipe:
    def __init__(self, title: str, ingredients: list, steps: str, category: str):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps
        self.category = category

    

    @classmethod
    def from_user_input(cls):
        title = input("Recipe Title: ").strip()
        ingredients = input("Ingredients (comma-separated): ").split(",")
        steps = input("Steps: ")  # don't strip because we want to preserve formatting
        category = input("Category: ").strip()
        return cls(
            title=title,
            ingredients=[i.strip() for i in ingredients],
            steps=steps,
            category=category
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "ingredients": self.ingredients,
            "steps": self.steps,
            "category": self.category
        }

    @staticmethod
    def from_dict(data: dict):
        return Recipe(
            title=data.get("title", ""),
            ingredients=data.get("ingredients", []),
            steps=data.get("steps", ""),
            category=data.get("category", "")
        )
