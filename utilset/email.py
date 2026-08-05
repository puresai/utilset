import hashlib
import re

pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"

def is_valid(email):
    if re.search(pattern, email):
        return True
    else:
        return False

def get_domain(email):
    arr = email.split('@')
    return arr[1].lower()

def md5_email(email: str) -> str:
    email = email.strip().lower()
    name, domain = email.split('@')
    if domain in ('gmail.com', 'googlemail.com'):
        name = name.replace('.', '').replace('+', '')
        email = f"{name}@gmail.com"
    return hashlib.md5(email.encode()).hexdigest()