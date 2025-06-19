#!/bin/bash

# Create log folder if it doesn't exist
mkdir -p logs

# Log file
LOG_FILE=logs/test.log

# Run test recipe inside container
docker run --rm -v "$(pwd)/data:/app/data" recipe-app python -c "
from classes.recipe import Recipe
from classes.recipe_book import RecipeBook
from path import RECIPE_FILE
import json

try:
    book = RecipeBook(RECIPE_FILE)
    existing_titles = [r.title for r in book.get_all()]
    if 'Test Recipe' not in existing_titles:
        r = Recipe('Test Recipe', ['egg', 'milk'], 'Mix well.', 'Test')
        book.add(r)
        print('✅ Test recipe added.')
    else:
        print('ℹ️  Test recipe already exists.')
except Exception as e:
    print(f'❌ Error: {e}')
" | tee $LOG_FILE

# Show current content of recipes.json
echo -e "\n📄 Current recipes.json content:" | tee -a $LOG_FILE
cat ./data/recipes.json | tee -a $LOG_FILE
