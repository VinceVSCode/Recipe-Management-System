"""
v1.7.0 - Utility functions for UI improvements
- clear_screen(): Clears terminal for better UX
- print_banner(): Displays app title
"""

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("📘 Welcome to Recipe Manager v1.7")
    print("-" * 35)
