import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "recipes.json"

def load_recipes() -> List[Dict]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_recipes(recipes: List[Dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(recipes, f, indent=4)

def add_recipe(title: str, ingredients: List[str], steps: str, category: str) -> None:
    recipes = load_recipes()
    recipes.append({
        "title": title,
        "ingredients": ingredients,
        "steps": steps,
        "category": category
    })
    save_recipes(recipes)

def view_all_recipes() -> None:
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.")
        return
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe['title']} ({recipe['category']})")


def view_recipe_by_name(title: str) -> None:
    recipes = load_recipes()
    for recipe in recipes:
        if recipe['title'].lower() == title.lower():
            print(f"\n📖 {recipe['title']} ({recipe['category']})")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Steps: {recipe['steps']}")
            return
    print("❌ Recipe not found.")
