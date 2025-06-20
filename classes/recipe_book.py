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

    
    def get_all(self):
        """
        Returns a list of all Recipe objects in the recipe book.
        """
        return self.recipes

    def get_by_title(self, title: str) -> Optional[Recipe]:
            for r in self.recipes:
                if r.title.lower() == title.lower():
                    return r
            return None


    def delete(self, title: str) -> bool:
        """
        Deletes a recipe by title. Returns True if deleted, False if not found.
        """
        for i, recipe in enumerate(self.recipes):
            if recipe.title.lower() == title.lower():
                del self.recipes[i]
                self.save()
                return True
        return False

    def update(self, title: str, new_recipe: Recipe) -> bool:
        """
        Replaces an existing recipe with the same title.
        """
        for i, recipe in enumerate(self.recipes):
            if recipe.title.lower() == title.lower():
                self.recipes[i] = new_recipe
                self.save()
                return True
        return False

    def search_by_title(self, keyword: str) -> list:
        """
        Returns recipes whose titles contain the keyword.
        """
        keyword = keyword.lower()
        return [
            recipe for recipe in self.recipes
            if keyword in recipe.title.lower()
        ]

    def search_by_ingredient(self, keyword: str) -> list:
        """
        Returns recipes whose ingredients contain the keyword.
        """
        keyword = keyword.lower()
        return [
            recipe for recipe in self.recipes
            if any(keyword in ing.lower() for ing in recipe.ingredients)
        ]

