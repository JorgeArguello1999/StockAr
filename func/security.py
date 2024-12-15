"""
Encrypt data
"""

# Modules 
import bcrypt

# Hash password
def hash_password(password:str) -> str:
    "Generate a hashed password"
    salt = bcrypt.gensalt() # Random salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)

# Check password
def check_password(password: str, hashed_password: str) -> bool:
    "Check if password is correct"
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)