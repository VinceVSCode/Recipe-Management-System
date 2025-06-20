#!/bin/bash

# Step 1: Add a test recipe using a temp container
docker run -e DOCKER_TEST=1 --rm -v "$(pwd)/data:/app/data" recipe-app python -c "
from classes.recipe import Recipe
from classes.recipe_book import RecipeBook
from path import RECIPE_FILE
r = Recipe('Test Recipe', ['egg', 'milk'], 'Mix well.', 'Test')
book = RecipeBook(RECIPE_FILE)
book.add(r)
print('✅ Test recipe added.')
"

# Step 2: Display contents of recipes.json
echo "📄 Current recipes.json content:"
cat ./data/recipes.json
