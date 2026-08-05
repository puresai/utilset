import hashlib
import re

def md5_phone(phone: str) -> str:
    phone = re.sub(r'[^0-9]', '', phone)
    return hashlib.md5(phone.encode()).hexdigest()
