#!/usr/bin/env python3

from gtts import gTTS
import subprocess
from sys import argv

print('hello')
def text_to_speech(text, language='en', speed=False, output_file='/tmp/output.mp3'):
    tts = gTTS(text=text, lang=language, slow=speed)
    tts.save(output_file)
    return output_file

def play_sound(file_path):
    command = f'play {file_path} tempo 1.4 2>&1 > /dev/null'
    result = subprocess.check_output(command, shell=True)

if __name__ == "__main__":
    text_to_speak = argv[1]
    language_code = 'en-GB'
    output_file_path = text_to_speech(text_to_speak, language=language_code)
    play_sound(output_file_path)
#    cleanUp = subprocess.run([f"rm {output_file_path}"], shell=True)
