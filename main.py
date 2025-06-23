"""
main.py - v1.7.0
Functionality:
- Enhanced CLI with menu interface
- Uses RecipeManager for core actions
- UI utilities: clear_screen, print_banner
- Basic argparse integration
"""

import argparse
from classes.recipe import Recipe
from modules.recipe_manager import RecipeManager
from utils.ui import clear_screen, print_banner

def main():
    parser = argparse.ArgumentParser(description="Run Recipe Manager CLI")
    parser.add_argument("--list", action="store_true", help="List all recipes and exit")
    args = parser.parse_args()

    manager = RecipeManager()

    if args.list:
        print_banner()
        for recipe in manager.list_all():
            print(" -", recipe.title)
        return

    while True:
        clear_screen()
        print_banner()

        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search by Title")
        print("4. Search by Ingredient")
        print("5. Delete Recipe")
        print("6. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            recipe = Recipe.from_user_input()
            manager.add_recipe(recipe.title, recipe.ingredients, recipe.steps, recipe.category)
            print("✅ Recipe added.")
        elif choice == "2":
            print("\n📘 All Recipes:")
            for recipe in manager.list_all():
                print(" -", recipe.title)
        elif choice == "3":
            title = input("Enter title keyword: ")
            matches = manager.search_by_title(title)
            for recipe in matches:
                print(" -", recipe.title)
        elif choice == "4":
            ing = input("Enter ingredient keyword: ")
            matches = manager.search_by_ingredient(ing)
            for recipe in matches:
                print(" -", recipe.title)
        elif choice == "5":
            title = input("Enter exact recipe title to delete: ")
            if manager.delete_recipe(title.strip()):
                print("🗑️  Recipe deleted.")
            else:
                print("❌ Recipe not found.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
