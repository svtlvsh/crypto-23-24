#!/usr/bin/python3

from collections import Counter
import sys

ALPHABET = "абвгдежзийклмнопрстуфхцчшщыьэюя"
M = len(ALPHABET)
ROUNDVAL = 3
KEYS = ["да", "зло", "крах", "месть", "денацификация", "самоуничтожение"]

# Read n characters of file fname.
def read_file(fname: str, n=0) -> str:
    with open(fname, "r") as f:
        if n:
            text = f.read(n)
        else:
            text = f.read()
    return text
 
# Filter and edit text.   
def format_text(text: str) -> str:
    # Remove uppercase letters.
    text = text.lower()
    # Replace some letters.
    text = text.replace("ё", "е")
    text = text.replace("ъ", "ь")
    # Remove other symbols.
    for i in range(len(text)):
        if text[i] not in ALPHABET:
            text = text.replace(text[i], " ")
    text = text.replace(" ", "")
    return text

# Calculate frequencies of letters in text.
def frequency(text: str) -> dict:
    letters = Counter(text)
    total = sum(letters.values())
    f = {l:round(c/total, ROUNDVAL) for l, c in letters.items()}
    return f
    
# Swap letters with their corresponding numbers.
def encode(text: str) -> list:
    return [ALPHABET.index(x) for x in text]

# Swap numbers with their corresponding letters.
def decode(nums: list) -> str:
    return ''.join([ALPHABET[x] for x in nums])
   
# Encrypt text with Vigenere cipher.
def encrypt(text: str, key: str) -> str:
    ct = encode(text)
    r = encode(key)
    sz = len(r)
    for i in range(len(text)):
        ct[i] = (ct[i] + r[i % sz]) % M
    return decode(ct)

# Decrypt text encrypted with Vigenere cipher.  
def decrypt():
    pass
    
# Visualize encryption.
def show_encryption(text: str, key: str) -> None:
    tsz = len(text)
    ksz = len(key)
    print(f"""M:\t{text}
r:\t{key * (tsz//ksz) + key[:tsz%ksz]}
C:\t{encrypt(text, key)}\n""")

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("""USAGE: ./cp2.py INPUTFILE [NUMOFBYTES]
[*] INPUTFILE\t- path to the input file
[*] NUMOFBYTES\t - number of bytes to read. (default is all)""")
    else:
        f = sys.argv[1]
        # Read and format russian text.
        text = format_text(read_file(f, 30))
        # Encrypt text with different keys.
        for r in KEYS:
            show_encryption(text, r)
        # Find I.
