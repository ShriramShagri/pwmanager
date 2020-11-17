from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os

def getPrivate(path = os.path.join(os.getcwd(), 'private_key.pem')):

    with open(path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    return private_key

def getPublic(path = os.path.join(os.getcwd(), 'public_key.pem')):

    with open(path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    
    return public_key