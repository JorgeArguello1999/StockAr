"""
Here create the files for the all program
"""

# Module 
from func import logger
from os.path import isfile
from os import makedirs

# Data directory
file_path = "./database/"
makedirs(file_path, exist_ok=True) # Exist?

# Files
files = [
    'cashier', # Cashier (User Data)
    'customers', # Customers (User Data)
    'data' # Data (Inventory Data)
]

# Create files
def create_files(file_name:str) -> bool:
    "Create your files if don't exist"

    try: 
        with open(f"{file_path}/{file_name}.txt", 'a') as file:
            file.close()
        return True 

    except Exception as e:
        print(f"Error: {e}")
        return False

# Start Files 
def start_files(files:list=files) -> None: 
    "Start all files for app"

    for i in files:
        if isfile(f'{file_path}/{i}.txt'):
            logger.log_info(f'{i}.txt Exist')
        else: 
            logger.log_warning(f'{i}.txt No exist, creating... ')
            create_files(i)