
"""
main.py - v1.6
Functionality:
- CLI interface to manage recipes using RecipeManager
- Recipe class handles its own user input
"""

from classes.recipe import Recipe
from modules.recipe_manager import RecipeManager

def main():
    manager = RecipeManager()

    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. View Recipe by Name")
        print("4. Exit")

        choice = input("Select an option:")

        if choice == "1":
            recipe = Recipe.from_user_input()
            manager.add_recipe(recipe.title, recipe.ingredients, recipe.steps, recipe.category)
            print("✅ Recipe added.")

        elif choice == "2":
            all_recipes = manager.list_all()
            if all_recipes:
                print("\n📘 All Recipes:")
                for r in all_recipes:
                    print(f" - {r.title}")
            else:
                print("ℹ️  No recipes found.")

        elif choice == "3":
            title = input("Enter recipe title: ")
            matches = manager.search_by_title(title.strip())
            recipe = matches[0] if matches else None
            if recipe:
                print(f"\n📖 {recipe.title} ({recipe.category})")
                print(f"Ingredients: {', '.join(recipe.ingredients)}")
                print(f"Steps: {recipe.steps}")
            else:
                print("❌ Recipe not found.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
