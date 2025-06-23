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
    recipe-app python -c "
from modules.recipe_manager import RecipeManager
from path import RECIPE_FILE

try:
    manager = RecipeManager()
    all_titles = [r.title for r in manager.list_all()]
    if 'Manager Test Recipe' not in all_titles:
        manager.add_recipe('Manager Test Recipe', ['flour', 'water'], 'Mix and bake.', 'Test')
        print('✅ Manager test recipe added.')
    else:
        print('ℹ️  Manager test recipe already exists.')
except Exception as e:
    print(f'❌ Error: {e}')
" | tee logs/test-manager.log

echo -e "\n📄 Current recipes.json content:"
cat ./data/recipes.json
