from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import json
import getpass 



def generate_key(password):
    salt = b'HopeIsLife'  # Salt for key derivation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # You can adjust the number of iterations as needed
        salt=salt,
        length=32,  # Key length (32 bytes for Fernet)
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key



def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    data = json.dumps(data)
    return cipher_suite.encrypt(data.encode())

def storeEData(Edata, FilePath):
    with open(FilePath, 'wb') as file:
        file.write(Edata)

# Function to decrypt data with the provided key
def decrypt_data(data, key):
    try:
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(data).decode()
    except:
        print("invalid Key")
        return False

def loadData(filename):
    try:
        with open(filename,"rb") as file:
            loadedData = file.read()
        return loadedData
    except Exception as error:
        print("error in loading file")
        print(error)
        return False
    



def readEncryptedData(passwoard, filePath):
    getpass.getpass = lambda prompt='': passwoard
    PassKey = generate_key(passwoard)
    loadedData = loadData(filePath)
    data = decrypt_data(loadedData,PassKey)
    data = json.loads(data)
    if data:
        return data
