#!/usr/bin/python3

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


parser = argparse.ArgumentParser(description='This is a Test',add_help=False)

parser.add_argument('-c', '--continuee', help='this will continuse sending tweets')
parser.add_argument('-s', '--send', help='this will send single tweet')
parser.add_argument('--help', '-h', action='help', help='-m for morese code \n-b for binary code')

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the arguments
continueeMode = args.continuee
send = args.send


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

def sendTweet(client, tweet):
    print("sending ",tweet)
    response = client.create_tweet(text=tweet)
    print("Tweet posted successfully!")

def continueeSendingTweet(client):
    Exitflag = False 
    while not(Exitflag):
        tweet = input("Tweet That: ")
        if tweet == "exit" or tweet == "break":
            Exitflag = True
        else:
            response = client.create_tweet(text=tweet)
            print("Tweet posted successfully!")



if __name__ == "__main__":
    # Set up your Twitter API credentials
    filename = "/home/mr124/Documents/.TwitterApi.bin"
    password = getpass.getpass("Enter Your Passkey: ")
    PassKey = generate_key(password)
    loadedData = loadData(filename)
    data = decrypt_data(loadedData,PassKey)
    data = json.loads(data)
    if data:
        client = tweepy.Client(consumer_key=data["Mr12ConsumerKey"], consumer_secret=data["Mr12ConsumerSecret"], access_token=data["Mr12AccessToken"], access_token_secret=data["Mr12AccessTokenSecret"])
        if send:
            sendTweet(client, args.send)
        elif continueeMode:
            continueeSendingTweet(client)         
    else:
        print("error on data")