from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from .readKey import getPublic
import base64

def encrypt(message):
    public_key = getPublic()

    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(encrypted).decode('utf-8')

if __name__ == "__main__":
    i = input().encode('utf-8')
    print(encrypt(i))