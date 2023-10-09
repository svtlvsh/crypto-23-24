#!/usr/bin/python3

from collections import Counter
from random import randint
from math import log
import sys

ALPHABET = "абвгдежзийклмнопрстуфхцчшщыьэюя"
M = len(ALPHABET)
FREQS = {'о': 0.114, 'е': 0.086, 'а': 0.078, 'и': 0.068, 'н': 0.063, 'т': 0.061, 'с': 0.051, 'в': 0.045, 'л': 0.045, 'р': 0.041, 'к': 0.041, 'д': 0.031, 'м': 0.03, 'у': 0.03, 'п': 0.028, 'ь': 0.021, 'ы': 0.019, 'ч': 0.019, 'б': 0.019, 'я': 0.019, 'г': 0.017, 'з': 0.017, 'ж': 0.011, 'х': 0.01, 'й': 0.01, 'ш': 0.01, 'ю': 0.006, 'ц': 0.003, 'щ': 0.003, 'э': 0.002, 'ф': 0.001}
IOC_TH = 0.055
ENTROPY = 4.457
KEYS = ["т", "да", "зло", "крах", "месть", "денацификация", "самоуничтожение", "сельскохозяйственный", "электрофотополупроводниковый"]

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

# Calculate appearences of letters in text.
def count_letters(text: str) -> dict:
    return Counter(text)

# Calculate entropy.    
def entropy(text: str) -> float:
    count = count_letters(text)
    total = sum(count.values())
    probs = {l:c/total for l, c in count.items()}
    return -sum(p * log(p, 2) for p in probs.values() if p > 0)
   
# Calculate practical index of coincidence.
def ioc(text: str) -> float:
    n = len(text)
    count = count_letters(text)
    ioc = 0
    for i in ALPHABET:
        ioc += count[i] * (count[i] - 1)
    return ioc / (n * (n - 1))
    
# Separate ciphered text into blocks.
def separate(text: str, period: int) -> list:
    blocks = [''] * period
    for i in range(len(text)):
        blocks[i % period] += text[i]
    return blocks

# Find period (key length).    
def find_period(text: str, show=False) -> int:
    # Initialize period.
    period = 1
    acc = 0.005
    while period <= 50:
        blocks = separate(text, period)
        res = 0
        for b in blocks:
            res += ioc(b)
        res /= period
        # Visualize correlation between period and IoC values.
        if show:
            print(f"{period}\t{res}")
        else:
            if IOC_TH - res < acc:
                return period
        period += 1
    return 0

# Find key based on found period.    
def found_key(text: str, period: int):
    blocks = separate(text, period)
    # List of the most common letters in blocks.
    common = []
    for b in blocks:
        # Find and store the most common letter in a block b.
        letters = dict(sorted(count_letters(b).items(), reverse=True, key=lambda item: item[1]))
        common.append(encode(list(letters)[0]))
    while True:
        s = []
        for i in range(14):
            s.append(encode(list(FREQS)[randint(0, 5)]))
        key = ''.join([decode((y-x)%M) for x, y in zip(common, s)])
        if ENTROPY - entropy(decrypt(text, key)) < 1:
            #print(key)
            visualize(text, key, "d")
    
# Swap letters with their corresponding numbers.
def encode(text: str):
    encoded = [ALPHABET.index(x) for x in text]
    if len(encoded) == 1:
        return encoded[0]
    else:
        return encoded

# Swap numbers with their corresponding letters.
def decode(nums) -> str:
    if isinstance(nums, int):
        return ALPHABET[nums]
    else:
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
def decrypt(text: str, key: str):
    ct = encode(text)
    r = encode(key)
    sz = len(r)
    for i in range(len(text)):
        ct[i] = (ct[i] - r[i % sz]) % M
    return decode(ct)

# Support function for visualize.
def split_text(text: str, size=30) -> list:
    res = []
    i = 0
    n = len(text)
    while i < n:
        res.append(text[i:i+size])
        i += size
    return res
   
# Visualize encryption.
def visualize(text: str, key: str, act='e') -> None:
    ksize = len(key)
    i = 0
    parts = split_text(text)
    for p in parts:
        tsize = len(p)
        if act == 'e':
            print(f"""M:\t{p}
r:\t{key * (tsize//ksize) + key[:tsize%ksize]}
C:\t{encrypt(p, key)}\n""")
        elif act == 'd':
            print(f"""C:\t{p}
r:\t{key * (tsize//ksize) + key[:tsize%ksize]}
M:\t{decrypt(p, key)}\n""")
        else:
            print("Incorrect act value. Choose between \'e\' and \'d\'")    

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("""USAGE: ./cp2.py INPUTFILE
[*] INPUTFILE\t- path to the input file""")
    else:
        f = sys.argv[1]
        # Read and format russian text.
        text = format_text(read_file(f))
        '''
        # Task 1. Encrypt custom text with different keys.
        print(find_period(text))
        for r in KEYS:
            print(f"IoCpr = {ioc(encrypt(text, r))}")
            visualize(text, r)
        '''
        # Task 2. Find key length.
        period = find_period(text)
        print(f"Key length is {period}")
        # Task 3. Find key.
        #print(f"Key = {found_key(text, period)}")
        #find_key(blocks, period)
        #visualize(text[:30], "щкккэтойекрпкк", 'd')
        #visualize(text[:30], "гууужьчтоущшуу", 'd')
        #visualize(text[:30], "энннахсминутнн", 'd')
        found_key(text[:30], period)
        #visualize(text[:60], "гсдтщбтнстюдйд", "d")
        
'''
# IOC_TH was found by using iocth and FREQS:

# Calculate theoretical index of coincidence.
def iocth(text: str) -> float:
    n = len(text)
    th = 0
    for i in ALPHABET:
        th += FREQS[i] * n * (FREQS[i] * n - 1)
    return th / (n * (n - 1))
''' 
