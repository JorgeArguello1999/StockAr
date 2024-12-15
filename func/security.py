"""
Encrypt data
"""

# Modules 
import bcrypt
import uuid

# Hash password
def hash_password(password:str) -> str:
    "Generate a hashed password"
    salt = bcrypt.gensalt() # Random salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Check password
def check_password(password: str, hashed_password: str) -> bool:
    "Check if password is correct"
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Get Unique ID
def get_uuid() -> str:
    return str(uuid.uuid4())