import os
import pandas as pd

# user creation module
# save recepies
# have categories, have reviews, have ratings
# exports to pdf or email

# sent recepies to other users, share with friends

# future
# -  Add some API functionality to fetch recipes from an external source





    
# A simple function to print "Hello, World!"
def Hello_World():
    print("Hello, World!")

def secret_function():
    my_api_key = os.getenv("MY_API_KEY")
    if my_api_key:
        print(f"Your API key is: {my_api_key[:7]}... (hidden for security)")
    else:
        print("No API key found.")

    # This function is not intended to be called directly
    print("This is a secret function!")

# This is the entry point of the script
if __name__ == "__main__":
    Hello_World()
    secret_function()
# Note: Ensure that the environment variable MY_API_KEY is set before running this script.
