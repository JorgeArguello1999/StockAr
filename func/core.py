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
files = {
    'cashier': "id, user, password", # Cashier (User Data)
    'customers': "id, name, item, date, price", # Customers (User Data)
    'data': "id, name, price, count, total_value" # Data (Inventory Data)
}

# Create files
def create_files(file_name:str, rows:str) -> bool:
    "Create your files if don't exist"

    try: 
        with open(f"{file_path}/{file_name}.txt", 'a') as file:
            file.write(f'{rows}\n')
            file.close()
        return True 

    except Exception as e:
        data = logger.log_error(e)
        print(data)
        return False

# Start Files 
def start_files(files:dict=files) -> None: 
    "Start all files for app"

    for i in files.keys():
        if isfile(f'{file_path}/{i}.txt'):
            logger.log_info(f'{i}.txt Exist')
        else: 
            logger.log_warning(f'{i}.txt No exist, creating... ')
            create_files(i, files[i])