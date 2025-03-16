#!/usr/bin/env python3
import os
import argparse
import time
import subprocess  # Import subprocess to call the tweet script

# Function to count the number of times the script has been run
def countRuns():
    countFile = "/home/mr124/Documents/logs/ManoKeyboardCount.txt"
    if not os.path.exists(countFile):
        with open(countFile, "w") as file:
            file.write("0")
    with open(countFile, "r+") as file:
        try:
            count = int(file.read().strip())
        except ValueError:
            count = 0
        count += 1
        file.seek(0)
        file.write(str(count))
    return count

# Function to record the current run time
def recordRun():
    with open("/home/mr124/Documents/logs/ManoKeybardLastRun.txt", 'w') as f:
        f.write(str(int(time.time())))

# Function to check if more than one week has passed since the last tweet
def shouldTweet():
    lastRunFile = "/home/mr124/Documents/logs/ManoKeybardLastRun.txt"
    one_week_seconds = 604800  # one week in seconds
    if not os.path.exists(lastRunFile):
        return True  # No record means we should tweet
    try:
        with open(lastRunFile, "r") as f:
            lastRun = int(f.read().strip())
    except ValueError:
        return True
    now = int(time.time())
    return (now - lastRun) > one_week_seconds

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mano's Keyboard thanks script")
    parser.add_argument('-t', '--tweet', action='store_true',
                        help='Force tweet the thanks message regardless of time gap')
    parser.add_argument('-c', '--count', action='store_true',
                        help='Increment the count without tweeting')
    parser.add_argument('-p', '--passcode', help='Passcode for tweet authentication (if needed)')

    args = parser.parse_args()

    # Set your tweet script path.
    tweet_script_path = "/home/mr124/scripts/Tweet.py"  # update to your actual tweet script file name

    # If -t is provided, force tweet
    if args.tweet:
        count = countRuns()
        recordRun()
        tweet_message = f"Thank You Mano {count} 🥹"
        command = [
            "/home/mr124/PyEnv/Tweet/bin/python3",
            tweet_script_path,
            "-s", tweet_message
        ]
        # Only add the -p flag if a passcode was provided.
        if args.passcode:
            command.extend(["-p", args.passcode])
        subprocess.run(command)

    # If -c is provided, only update the count.
    elif args.count:
        count = countRuns()
        print(f"Count updated to {count}")

    else:
        # Automatic mode: check if a week has passed.
        if shouldTweet():
            count = countRuns()
            recordRun()
            tweet_message = f"Thank You Mano {count} 🥹"
            command = [
                "/home/mr124/PyEnv/Tweet/bin/python3",
                tweet_script_path,
                "-s", tweet_message
            ]
            if args.passcode:
                command.extend(["-p", args.passcode])
            subprocess.run(command)
        else:
            print("Not enough time has passed since the last tweet.")
