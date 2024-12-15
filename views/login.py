"""
LogIn View
"""
# Modules
from func import security
from func import crud
from func import logger

# Data
data = crud.read('cashier')

def login(user: str, password: str) -> bool:
    "Enter session"

    for i in data:
        if i[1] == user and security.check_password(password, i[2]):
            logger.log_access(f'{user} Access')
            return True
    logger.log_forbidden(f'{user} try access...')
    return False

# [id, user, password]
def register(user: str, password: str) -> bool:
    "Register a new cashier"

    try:
        hashed_password = security.hash_password(password)
        user_id = security.get_uuid()
        crud.add('cashier', [user_id, user, hashed_password])
        logger.log_info(f'User: {user}... Added')

        return True

    except Exception as e:
        data = logger.log_error(e)
        print(data)
        return False 