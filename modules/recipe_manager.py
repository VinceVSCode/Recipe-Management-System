"""
RecipeManager: coordinates high-level recipe actions.
Keeps main logic clean and centralizes recipe operations.
"""

from classes.recipe_book import RecipeBook
from classes.recipe import Recipe
from path import RECIPE_FILE


class RecipeManager:
    def __init__(self):
        self.book = RecipeBook(RECIPE_FILE)

    def add_recipe(self, title, ingredients, steps, category):
        recipe = Recipe(title, ingredients, steps, category)
        return self.book.add(recipe)

    def delete_recipe(self, title):
        return self.book.delete(title)

    def update_recipe(self, title, new_recipe):
        return self.book.update(title, new_recipe)

    def search_by_title(self, keyword):
        return self.book.search_by_title(keyword)

    def search_by_ingredient(self, keyword):
        return self.book.search_by_ingredient(keyword)

    def list_all(self):
        return self.book.get_all()
