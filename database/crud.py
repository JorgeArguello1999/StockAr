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
    
# Delete record
def delete(file:str, value:str, colum:int) -> bool:
    try:
        # Read file
        with open(f'{file_path}/{file}.txt', 'r', encoding='utf-8') as file_read:
            rows = [line.strip().split(',') for line in file_read]

        update_rows = []
        for i in rows:
            if i[colum] != value:
                update_rows.append(i)

        # Have a change?
        if len(rows) == len(update_rows): # No changes
            data = logger.log_warning(f"Your item doesn't exist, {value} and {colum}")
            print(data)
            return False
        
        # Save the change
        with open(f"{file_path}/{file}.txt", 'w', encoding='utf-8') as file_write:
            for row in update_rows:
                file_write.write(','.join(row) + '\n')

        data = logger.log_info(f"Your item {value} deleted in colum {colum}")
        print(data)
        return True

    except Exception as e:
        data = logger.log_error(e)
        print(data)
        return False 