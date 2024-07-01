import time
import subprocess

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

def flash_morse_code(display_name, morse_code):
    for symbol in morse_code:
        if symbol == '-':
            subprocess.run(['xrandr', '--output', display_name, '--brightness', '0.1'])
            time.sleep(0.5)  # Dash duration
            subprocess.run(['xrandr', '--output', display_name, '--brightness', '1.0'])
            time.sleep(0.5)  # Gap between symbols
        elif symbol == '.':
            subprocess.run(['xrandr', '--output', display_name, '--brightness', '0.1'])
            time.sleep(0.2)  # Dot duration
            subprocess.run(['xrandr', '--output', display_name, '--brightness', '1.0'])
            time.sleep(0.5)  # Gap between symbols
        else:
            time.sleep(1)  # Gap between words

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        elif char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()

if __name__ == "__main__":
    display_name = "VGA-0"  # Replace with your display name, e.g., "HDMI-1", "DP-1", etc.

    word = input("Enter a word to convert to Morse code: ")
    print(word)
    morse_code = text_to_morse(word)

    flash_morse_code(display_name, morse_code)
