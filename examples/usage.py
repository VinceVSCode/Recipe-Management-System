"""
Example usage of the RecipeBook and Recipe classes.
Feel free to edit or expand this file.
"""

from classes.recipe import Recipe
from classes.recipe_book import RecipeBook
from path import RECIPE_FILE

# Initialize the recipe book
book = RecipeBook(RECIPE_FILE)

# Add a recipe
new_recipe = Recipe(
    title="Toast & Jam",
    ingredients=["Bread", "Jam"],
    steps="1. Toast the bread\n2. Spread jam\n3. Serve.",
    category="Breakfast"
)
book.add(new_recipe)
print("✅ Recipe added.")

# Search by title
title_matches = book.search_by_title("toast")
print("\n🔍 Title search results:")
for r in title_matches:
    print(f" - {r.title}")

# Search by ingredient
ingredient_matches = book.search_by_ingredient("bread")
print("\n🔍 Ingredient search results:")
for r in ingredient_matches:
    print(f" - {r.title}")

# List all recipes
print("\n📘 All recipes:")
for r in book.get_all():
    print(f" - {r.title}")

# Delete recipe
if book.delete("Toast & Jam"):
    print("\n🗑️  'Toast & Jam' deleted.")
else:
    print("\n⚠️  Could not find 'Toast & Jam' to delete.")
