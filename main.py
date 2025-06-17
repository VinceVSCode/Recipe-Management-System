from modules.recipe_manager import add_recipe, view_all_recipes, view_recipe_by_name

def main():
    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. View Recipe by Name")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Recipe Title: ")
            ingredients = input("Ingredients (comma-separated): ").split(",")
            steps = input("Steps: ")
            category = input("Category: ")
            add_recipe(title.strip(), [i.strip() for i in ingredients], steps.strip(), category.strip())
            print("✅ Recipe added.")
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            title = input("Enter recipe title: ")
            view_recipe_by_name(title.strip())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
