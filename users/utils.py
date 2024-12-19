from random import randint
from uuid import uuid4

def generate_random_code():
    return randint(100000, 999999)

def generate_uuid():
    return uuid4()
