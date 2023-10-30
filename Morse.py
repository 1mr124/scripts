#!/usr/bin/python3

import argparse


parser = argparse.ArgumentParser(description='This is a Test',add_help=False)

parser.add_argument('-m', '--mores', help='this will convert text to morse code')
parser.add_argument('-b', '--binary', help='this will convert text to binary morse code')
parser.add_argument('-db', '--DecodeBinary', help='this will convert binary morse to text')
parser.add_argument('-dm', '--DecodMorse', help='this will convert morse to text')
parser.add_argument('--help', '-h', action='help', help='-m for morese code \n-b for binary code')

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the arguments
MoresOption = args.mores
BinaryOption = args.binary
DecodeBinary = args.DecodeBinary
DecodMorse = args.DecodMorse

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

MoresCodeBinary = {'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0', 'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111', 'K': '101', 'L': '0100', 'M': '11', 'N': '10', 'O': '111', 'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1', 'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011', 'Z': '1100', '0': '11111', '1': '01111', '2': '00111', '3': '00011', '4': '00001', '5': '00000', '6': '10000', '7': '11000', '8': '11100', '9': '11110', '.': '010101', ',': '110011', '?': '001100', "'": '011110', '!': '101011', '/': '10010', '(': '10110', ')': '101101', '&': '01000', ':': '111000', ';': '101010', '=': '10001', '+': '01010', '-': '100001', '_': '001101', '"': '010010', '$': '0001001', '@': '011010', ' ': '/'}

def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_code:
            morse += morse_code[char] + ' '
        else:
            morse += char + ' '
    return morse.strip()



def TextToBinarry(text):
    morse = ''
    for char in text.upper():
        if char in MoresCodeBinary:
            morse += MoresCodeBinary[char] + ' '
        else:
            morse += char + ' '
    return morse.strip()


def DecodeBinaryMorese(MorseBinary):
    text = ""
    for i in MorseBinary.split():
        text += list(MoresCodeBinary.keys())[list(MoresCodeBinary.values()).index(i)]
    return text

def DecodTextMorese(TextMorse):
    text = ""
    for i in TextMorse.split():
        text += list(morse_code.keys())[list(morse_code.values()).index(i)]
    return text


if __name__ == "__main__":
    if BinaryOption:
        print(TextToBinarry(BinaryOption))
    elif MoresOption:
        print(text_to_morse(MoresOption))
    elif DecodeBinary:
       print(DecodeBinaryMorese(DecodeBinary))
    elif DecodMorse:
        print(DecodTextMorese(DecodMorse))
    else:
        print("seek help -h --help")