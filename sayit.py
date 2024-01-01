#!/usr/bin/env python3

from gtts import gTTS
import subprocess
from sys import argv



def textToSpeech(text, language='en', speed=False, outputFile='/tmp/output.mp3'):
    tts = gTTS(text=text, lang=language, slow=speed)
    tts.save(outputFile)
    return outputFile

def playSound(filePath):
    command = f'play {filePath} tempo 1.4 2>&1 > /dev/null'
    result = subprocess.check_output(command, shell=True)

if __name__ == "__main__":
    text = argv[1]
    language_code = 'en-GB'
    outputFilePath = textToSpeech(text, language=language_code)
    playSound(outputFilePath)
    cleanUp = subprocess.run([f"rm {outputFilePath}"], shell=True)
