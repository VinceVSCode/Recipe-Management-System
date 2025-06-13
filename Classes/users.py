# user class 
import pandas as pd
# user class for a recipe application
# This module handles user creation and management for a recipe application.
path_to_user_data = "user_data.csv"

class User:
    """
    A class to represent a user in the recipe application.
    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        recipes (list): A list to store recipes created by the user.
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.password = None
        self.recipes = pd.empty.DataFrame(columns=['Recipe Name', 'Ingredients', 'Instructions'])

    def set_password(self, password):
        """
        Set the user's password.
        Args:
            password (str): The password to set for the user.
        """
        self.password = password

    def get_username(self):
        """
        Get the username of the user.
        Returns:
            str: The username of the user.
        """
        return self.username
    
    def get_email(self):
        """
        Get the email address of the user.
        Returns:
            str: The email address of the user.
        """
        return self.email
    
    def add_recipe(self, recipe):
        """
        Add a recipe to the user's recipe collection.
        Args:
            recipe (dict): A dictionary containing recipe details.
        """
        if isinstance(recipe, dict):
            # Ensure the recipe has the required keys
            required_keys = ['Recipe Name', 'Ingredients', 'Instructions']
            if not all(key in recipe for key in required_keys):
                raise ValueError(f"Recipe must contain the following keys: {required_keys}")
            
            # Convert the recipe dictionary to a DataFrame
            recipe_df = pd.DataFrame([recipe])
            self.recipes = self.recipes.append(recipe, ignore_index=True)
        
        else:
            raise ValueError("Recipe must be a dictionary.")
        
    def get_recipes(self):
        return self.recipes

# function to initialize a user
def create_user(username, email, password):
    """
    Create a new user with the given username, email, and password.
    Args:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password for the user.
    Returns:
        User: An instance of the User class.
    """
    user = User(username, email)
    user.set_password(password)
    # check if the user already exists
    if user_exists(username, password, []):  # Assuming an empty list for demonstration
        raise ValueError("User already exists with this username and password.")
    return user    

# funciton to check if a user/password combination exists. Assume you check the local database or a list of users.

def user_exists(username, password, user_list):
    """
    Check if a user exists with the given username and password.
    Args:
        username (str): The username to check.
        password (str): The password to check.
        user_list (list): A list of existing users.
    Returns:
        bool: True if the user exists, False otherwise.
    """
    for user in user_list:
        if user.get_username() == username and user.password == password:
            return True
    return False