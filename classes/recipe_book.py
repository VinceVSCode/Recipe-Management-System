"""
recipe_book.py - v1
Functionality:
- Loads and saves recipes to JSON
- Can add, retrieve, and list recipes
"""

import json
from pathlib import Path
from typing import Optional
from classes.recipe import Recipe

class RecipeBook:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.recipes = self.load()

    def load(self) -> list:
        if self.filepath.exists():
            with open(self.filepath, "r") as f:
                return [Recipe.from_dict(r) for r in json.load(f)]
        return []

    def save(self) -> None:
        with open(self.filepath, "w") as f:
            json.dump([r.to_dict() for r in self.recipes], f, indent=4)

    def add(self, recipe: Recipe) -> None:
        self.recipes.append(recipe)
        self.save()

    def list_all(self) -> None:
        if not self.recipes:
            print("No recipes found.")
        for i, r in enumerate(self.recipes, 1):
            print(f"{i}. {r.title} ({r.category})")

    def get_by_title(self, title: str) -> Optional[Recipe]:
        for r in self.recipes:
            if r.title.lower() == title.lower():
                return r
        return None
