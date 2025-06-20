#!/bin/bash

# Detect OS type and adjust volume mount path
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Likely Git Bash on Windows
    VOLUME_PATH="/$(pwd | sed 's|\\|/|g' | sed 's|C:|c|')/data:/app/data"
else
    # Linux/macOS/WSL/Unix
    VOLUME_PATH="$(pwd)/data:/app/data"
fi

# NOTE: PowerShell users may experience volume path issues. "data;C"
# This script is optimized for Git Bash and Unix-like shells.
# A PowerShell-specific script may be added in the future.

# Create logs directory if it doesn't exist
mkdir -p logs

# Run Docker container and pipe output to log
docker run --rm \
    -e DOCKER_TEST=1 \
    -v "$VOLUME_PATH" \
    recipe-app python -c "
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

# Display contents of the recipes.json file
echo -e "\n📄 Current recipes.json content:"
cat ./data/recipes.json
