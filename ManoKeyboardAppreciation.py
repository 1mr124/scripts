#!/usr/bin/env python3
import os
import argparse
import time


# Function to count the number of times the key remap script runs
def countRuns():
    countFile = "/home/mr124/Documents/logs/ManoKeyboardCount.txt"
    if not os.path.exists(countFile):
        with open(countFile, "w") as file:
            file.write("0")

    with open(countFile, "r+") as file:
        count = int(file.read())
        count += 1
        file.seek(0)
        file.write(str(count))
    return count

def recordRun():
    with open("/home/mr124/Documents/logs/ManoKeybardLastRun.txt", 'w') as f:
        f.write(str(int(time.time())))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mano's Keyboard thanks scrpt ")
    parser.add_argument('-t', '--tweet', help='this will make the script tweet the thanks message')
    parser.add_argument('-c', '--count', help='this will make the script count the number')



    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the arguments
    tweet = args.tweet 
    doCount = args.count

    # Your script logic goes here
    if doCount:
        count = countRuns()
    elif tweet:
        count = countRuns()
        recordRun()
        print(f"Thank You Mano {count} 🥹")
    else:
        print('ManoKeyboardAppreciation.py [-h] [-t TWEET] [-c COUNT]')
