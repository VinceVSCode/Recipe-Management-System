# paths.py
from pathlib import Path

# Root of the project
PROJECT_ROOT = Path(__file__).resolve().parent

# Standard directories
DATA_DIR = PROJECT_ROOT / "data"
CONFIG_DIR = PROJECT_ROOT / ".github" / "workflows"
SETTINGS_FILE = CONFIG_DIR / "actions_tut.yml"
VENV_DIR = PROJECT_ROOT / ".venv"
CLASSES_DIR = PROJECT_ROOT / "classes"
LOGS_DIR = PROJECT_ROOT / "logs"
# Print the paths for verification
def print_paths():
    print(f"\033[91mProject Root: {PROJECT_ROOT}\033[0m")
    print(f"\033[92mData Directory: {DATA_DIR}\033[0m")
    print(f"\033[34mConfig Directory: {CONFIG_DIR}\033[0m")
    print(f"\033[33mSettings File: {SETTINGS_FILE}\033[0m")
    print(f"\033[35mVirtual Environment Directory: {VENV_DIR}\033[0m")
    print(f"\033[36mClasses Directory: {CLASSES_DIR}\033[0m")
    print(f"\033[35mLogs Directory: {LOGS_DIR}\033[0m")

if __name__ == "__main__":
    print_paths()
    # Example usage
    if not DATA_DIR.exists():
        print(f"Data directory does not exist: {DATA_DIR}")
    if not SETTINGS_FILE.exists():
        print(f"Settings file does not exist: {SETTINGS_FILE}")
    if not VENV_DIR.exists():
        print(f"Virtual environment directory does not exist: {VENV_DIR}")
    if not CLASSES_DIR.exists():
        print(f"Classes directory does not exist: {CLASSES_DIR}")
    if not LOGS_DIR.exists():
        print(f"Logs directory does not exist: {LOGS_DIR}")
    else:
        print("\033[92mAll directories and files exist as expected.\033[0m")
    