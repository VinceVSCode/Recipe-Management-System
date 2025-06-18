"""
main.py - v1.2.1
Functionality:
- CLI interface to manage recipes
- Uses Recipe and RecipeBook classes
- Recipe class handles its own user input
"""

from classes.recipe import Recipe
from classes.recipe_book import RecipeBook
from path import RECIPE_FILE

def main():
    book = RecipeBook(RECIPE_FILE)

    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. View Recipe by Name")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            recipe = Recipe.from_user_input()
            book.add(recipe)
            print("✅ Recipe added.")

        elif choice == "2":
            book.list_all()

        elif choice == "3":
            title = input("Enter recipe title: ")
            recipe = book.get_by_title(title.strip())
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
