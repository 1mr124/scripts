#!/home/mr124/PyEnv/Tweet/bin/python3

import tweepy
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import json
import getpass 
import argparse
import keyring

def get_passcode(args):
    """
    Retrieve the passcode in a safe manner:
    1. Use command-line argument if provided.
    2. Attempt to get it from the keyring.
    3. If not available, prompt the user.
    """
    service = "MyTweetApp"
    username = "mr124"
    if args.passCode:
        return args.passCode
    stored = keyring.get_password(service, username)
    if stored:
        return stored
    return getpass.getpass("Enter Your Passkey: ")

# Set up the argument parser.
parser = argparse.ArgumentParser(description='This is a Test', add_help=False)
parser.add_argument('-c', '--continuee', help='this will continuse sending tweets')
parser.add_argument('-s', '--send', help='this will send single tweet')
parser.add_argument('-p', '--passCode', help='The password for authentication.')
parser.add_argument('--help', '-h', action='help', help='-m for morese code \n-b for binary code')
args = parser.parse_args()

# Access the values of the arguments.
continueeMode = args.continuee
send = args.send

def generate_key(password):
    salt = b'HopeIsLife'  # Salt for key derivation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # Adjust iterations as needed
        salt=salt,
        length=32,  # Key length (32 bytes for Fernet)
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def decrypt_data(data, key):
    try:
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(data).decode()
    except Exception as e:
        print("Invalid Key:", e)
        return False

def loadData(filename):
    try:
        with open(filename, "rb") as file:
            loadedData = file.read()
        return loadedData
    except Exception as error:
        print("Error loading file:", error)
        return False

def sendTweet(client, tweet):
    print("Sending:", tweet)
    response = client.create_tweet(text=tweet)
    print("Tweet posted successfully!")

def continueeSendingTweet(client):
    exit_flag = False 
    while not exit_flag:
        tweet = input("Tweet That: ")
        if tweet in ("exit", "break"):
            exit_flag = True
        else:
            response = client.create_tweet(text=tweet)
            print("Tweet posted successfully!")

def main(passwoard):
    # Generate the encryption key and decrypt the data.
    pass_key = generate_key(passwoard)
    loadedData = loadData(filename)
    decrypted = decrypt_data(loadedData, pass_key)
    if not decrypted:
        print("Error decrypting data.")
        return
    try:
        data = json.loads(decrypted)
    except Exception as e:
        print("Error parsing JSON:", e)
        return

    if data:
        client = tweepy.Client(
            consumer_key=data["Mr12ConsumerKey"],
            consumer_secret=data["Mr12ConsumerSecret"],
            access_token=data["Mr12AccessToken"],
            access_token_secret=data["Mr12AccessTokenSecret"]
        )
        if send:
            sendTweet(client, args.send)
        elif continueeMode:
            continueeSendingTweet(client)
    else:
        print("Error: No data loaded.")

if __name__ == "__main__":
    filename = "/home/mr124/Documents/.NewTwitter.bin"
    passcode = get_passcode(args)
    main(passcode)
