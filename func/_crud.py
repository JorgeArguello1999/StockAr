"""
Create, Read, Update and Delete
I will get CSV file 
"""

# Modules 
from func import logger

# Database dir
file_path = "./database/"

# Read database
def read(file:str) -> list:
    try:
        with open(f'{file_path}/{file}.txt', 'r', encoding='utf-8') as file:
            data = [ line.strip().split(',') for line in file ]
        return data 
    
    except Exception as e:
        data = logger.log_error(e)
        print(data)
        return []
    
# Add record
def add(file:str, data:list) -> bool:
    try:
        data_row = ','.join(map(str, data)) + '\n'
        with open(f'{file_path}/{file}.txt', 'a', encoding='utf-8') as file:
            file.write(data_row)
        return True
    
    except Exception as e:
        data = logger.log_error(e)
        print(data)
        return False