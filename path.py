"""
path.py - v1.1.1
Functionality:
- Centralized path definitions for the project
- Uses pathlib for OS-independent paths
- Supports environment variable overrides for Docker/cloud scaling
- Colorized print_paths() for better readability
"""

from pathlib import Path
import os

# Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent

# Data directory and files
DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
RECIPE_FILE = Path(os.getenv("RECIPE_FILE", DATA_DIR / "recipes.json"))

# Other standard directories
CONFIG_DIR = BASE_DIR / ".github" / "workflows"
SETTINGS_FILE = CONFIG_DIR / "actions_tut.yml"
VENV_DIR = BASE_DIR / ".venv"
CLASSES_DIR = BASE_DIR / "classes"
LOGS_DIR = BASE_DIR / "logs"

# Optional: Print paths for debugging future purposes
def print_paths():
    print(f"\033[91mProject Root: {BASE_DIR}\033[0m")
    print(f"\033[92mData Directory: {DATA_DIR}\033[0m")
    print(f"\033[93mRecipe File: {RECIPE_FILE}\033[0m")
    print(f"\033[94mConfig Directory: {CONFIG_DIR}\033[0m")
    print(f"\033[95mSettings File: {SETTINGS_FILE}\033[0m")
    print(f"\033[96mVirtual Environment Directory: {VENV_DIR}\033[0m")
    print(f"\033[97mClasses Directory: {CLASSES_DIR}\033[0m")
    print(f"\033[90mLogs Directory: {LOGS_DIR}\033[0m")
