"""
LogIn View
"""
# Modules
from func import security
from database import crud
from func import logger

# Data
data = crud.read('cashier')

# [id, user, password]

def check_user(user: str) -> bool:
    "Check if user exists"
    for i in data:
        if i[1] == user:
            return True
    return False

def login(user: str, password: str) -> bool:
    "Enter session"

    for i in data:
        if i[1] == user and security.check_password(password, i[2]):
            response = logger.log_access(f'{user} Access')
            print(response)
            return True

    data = logger.log_forbidden(f'{user} try access...')
    print(data)
    return False

def register(user: str, password: str, data: list=data) -> bool:
    "Register a new cashier"

    try:
        if check_user(user): 
            data = logger.log_error(f'{user} already exists')
            print(data)
            return False

        hashed_password = security.hash_password(password)
        user_id = security.get_uuid()
        crud.add('cashier', [user_id, user, hashed_password])
        data = logger.log_info(f'User: {user}... Added')
        print(data)
        return True

    except Exception as e:
        data = logger.log_error(e)
        print(data)
        return False 

def delete(user: str, password: str, data:list=data) -> bool:
    "Delete a user with user and password"
    pass