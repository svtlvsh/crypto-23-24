#!/usr/bin/python3
from pprint import pp 
import string
import math
from decimal import *

e_,a_,q_ = "[!]","[*]","[?]"
TEXT_FILENAME = 'text2'
RUS_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
getcontext().prec = 100

def clearText(text:str) -> str:
    text_ = list(text)
    permitted = RUS_ALPHABET
    result = [char for char in text_ if char in permitted]
    return ''.join(result)

def parseText(text:str) -> str:
    text_ = list(text)
    permitted = RUS_ALPHABET + string.punctuation + string.digits + ' '
    result = [char for char in text_ if char in permitted]
    return ''.join(result)

def printFreq(freq:dict) -> None:
    res_str = " ".join(["| {}:{:.12f}".format(item,freq[item]) for item in freq.keys()]) + " |"
    res_str = "".join([char + "\n" if (c + 1) % ((res_str.find(".")+14) * 5) == 0 else char for c,char in enumerate(res_str)])
    print(res_str)


def freqCalc(text:str,ch_len:int=1) -> dict:
    frequencies = {}
    text_len = len(text)
    for pos in range(0,text_len-ch_len+1):
        ch = text[pos:pos+ch_len]
        frequencies[ch] = frequencies.get(ch, 0) + 1
    frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1]))
    for item in frequencies: frequencies[item] = Decimal.from_float(frequencies[item] / text_len)
    return frequencies

def getEntropy(freq:dict) -> float:
    entropy = Decimal(0.0)
    for f in freq.values(): entropy -= f * Decimal.from_float(math.log2(f))
    return entropy


def main() -> None:
    with open(TEXT_FILENAME) as f:
        text_rus_clear = f.read().replace("\n"," ").lower()
    
    print(f"{a_} Counting the frequency for characters one by one...")
    freq_single = freqCalc(parseText(text_rus_clear))
    print(f"{e_} Frequency for each char:")
    printFreq(freq_single)
    entr1 = getEntropy(freq_single)
    print(f"{e_} Entropy H1: {entr1}")
    print(f"|\n{a_} Same text without spaces and special chars...")
    freq_single_WoSpaces = freqCalc(clearText(text_rus_clear))
    printFreq(freq_single_WoSpaces)
    entr1_ = getEntropy(freq_single_WoSpaces)
    print(f"{e_} H1 wo spaces: {entr1_}")
    print(f"|\n{a_} Counting frequency for bigrams with overlay...")
    freq_bigram = freqCalc(parseText(text_rus_clear),2)
    print(f"{e_} Frequency for bigrams:")
    if input("> Show bigram frequencies table? [y/n] ").lower() == "y": printFreq(freq_bigram)
    entr2 = getEntropy(freq_bigram)
    print(f"{e_} Entropy H2: {entr2}")
    print(f"|\n{a_} Counting frequency for bigrams without spaces...")
    freq_bigram_WoSpaces = freqCalc(clearText(text_rus_clear),2)
    print(f"{e_} Frequency for bigrams:")
    if input("> Show bigram frequencies table? [y/n] ").lower() == "y": printFreq(freq_bigram_WoSpaces)
    entr2_ = getEntropy(freq_bigram_WoSpaces)
    print(f"{e_} H2 wo spaces: {entr2_}")
if __name__ == "__main__":
    main()
