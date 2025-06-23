#!/bin/bash

cd "$(dirname "$0")/.."

# Detect OS type and adjust volume mount path
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    VOLUME_PATH="/$(pwd | sed 's|\\|/|g' | sed 's|C:|c|')/data:/app/data"
else
    VOLUME_PATH="$(pwd)/data:/app/data"
fi

mkdir -p logs

docker run --rm \
    -e DOCKER_TEST=1 \
    -v "$VOLUME_PATH" \
    recipe-app python -c "import platform; print('🐳 Docker Check — Running inside container:', platform.system());
from classes.recipe import Recipe
from classes.recipe_book import RecipeBook
from path import RECIPE_FILE
import json

try:
    book = RecipeBook(RECIPE_FILE)
    titles = [r.title for r in book.get_all()]
    if 'Test Recipe' not in titles:
        r = Recipe('Test Recipe', ['egg', 'milk'], 'Mix well.', 'Test')
        book.add(r)
        print('✅ Test recipe added.')
    else:
        print('ℹ️  Test recipe already exists.')
except Exception as e:
    print(f'❌ Error: {e}')
" | tee logs/test.log

echo -e "\n📄 Current recipes.json content:"
cat ./data/recipes.json
