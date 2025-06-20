"""
Example usage of the RecipeManager class.
Feel free to edit or expand this file.
"""

from modules.recipe_manager import RecipeManager
from classes.recipe import Recipe

manager = RecipeManager()

# Add a recipe
new_recipe = Recipe("Toast & Jam", ["Bread", "Jam"], "1. Toast bread\n2. Spread jam\n3. Serve.", "Breakfast")
manager.add_recipe(new_recipe.title, new_recipe.ingredients, new_recipe.steps, new_recipe.category)
print("✅ Recipe added via RecipeManager.")

# Search by title
title_matches = manager.search_by_title("toast")
print("\n🔍 Title search results:")
for r in title_matches:
    print(f" - {r.title}")

# Search by ingredient
ingredient_matches = manager.search_by_ingredient("bread")
print("\n🔍 Ingredient search results:")
for r in ingredient_matches:
    print(f" - {r.title}")

# List all recipes
print("\n📘 All recipes:")
for r in manager.list_all():
    print(f" - {r.title}")

# Delete recipe
if manager.delete_recipe("Toast & Jam"):
    print("\n🗑️  'Toast & Jam' deleted.")
else:
    print("\n⚠️  Could not find 'Toast & Jam' to delete.")
