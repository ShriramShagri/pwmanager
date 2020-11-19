from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from .readKey import getPrivate
import base64

def decrypt(
    encrypted
    ):

    private_key = getPrivate()

    original_message = private_key.decrypt(
        base64.b64decode(encrypted.encode('utf-8')),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message

if __name__ == "__main__":
    print(decrypt(input()))