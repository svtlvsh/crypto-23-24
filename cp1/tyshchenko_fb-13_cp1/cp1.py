#!/usr/bin/python3

from math import log
import sys

ALPHABET_LEN = 32
COLUMN_NUM = 4
ROUND_FLOAT = 3

def read_file(fname: str) -> str:
    with open(fname, "r") as f:
        text = f.read()
        f.close()
    return text
    
def format_text(text: str, allow_spaces=True) -> str:
    allowed = "абвгдежзийклмнопрстуфхцчшщыьэюя "
    # remove uppercase letters
    text = text.lower()
    # replace some letters
    text = text.replace("ё", "е")
    text = text.replace("ъ", "ь")
    # remove other symbols
    for i in range(len(text)):
        if text[i] not in allowed:
            text = text.replace(text[i], " ")
    # remove extra whitespaces or all of them
    temp = text.split()
    if allow_spaces:
        text = " ".join(temp)
    else:
        text = "".join(temp)
    return text

def ngram_processing(text: str, n: int, count=False):
    text_len = len(text)
    if count:
        ngrams = {}
        for s in range(text_len - n + 1):
            ngr = text[s:s + n]
            if ngr not in ngrams:
                ngrams[ngr] = text.count(ngr)
    else:
        ngrams = []
        for s in range(text_len - n + 1):
            ngr = text[s:s + n]
            if ngr not in ngrams:
                ngrams.append(ngr)
    return ngrams

# frequency = probability (ngram count -> infinity)
def probability(n: int, text: str, round_by=ROUND_FLOAT) -> dict:
    ngrams = ngram_processing(text, n, count=True)
    total = sum(ngrams.values())
    probs = {ngr : round(count/total, round_by) for ngr, count in ngrams.items()}
    return probs
    
def print_dict(dictionary: dict) -> None:
    # case print matrix
    if len(list(dictionary.keys())[0]) == 2:
        # second letter (without duplicates)
        second_letter = list(set([x[1] for x in dictionary]))
        # first letter (without duplicates)
        first_letter = list(set([x[0] for x in dictionary]))
        # put in ablphabetical order
        first_letter.sort()
        second_letter.sort()
        data = []
        for i in range(len(first_letter)):
            row = [0] * len(second_letter)
            for j in range(len(second_letter)):
                ngr = f"{first_letter[i]}{second_letter[j]}"
                if ngr in dictionary:
                    row[j] = round(dictionary[ngr], ROUND_FLOAT)
            data.append(row)
        format_row = "{:>8}" * (len(second_letter) + 1)
        print(format_row.format("", *second_letter))
        for letter, value in zip(first_letter, data):
            print(format_row.format(letter, *value))
    # case print in columns
    else:
        freqs = list(dictionary.items())
        freqs.sort()
        num = len(freqs)
        for i in range(num):
            print(f'\t"{freqs[i][0]}" - {freqs[i][1]}\t', end='')
            if (i + 1) % COLUMN_NUM == 0 or i + 1 == num:
                print("")

def entropy(probabilities: dict) -> float:
    entropy = -sum(p * log(p, 2) for p in probabilities.values() if p > 0)
    return entropy


if __name__ == "__main__":
    if len(sys.argv) == 4:
        f, n = sys.argv[1], int(sys.argv[3])
        s = True if sys.argv[2] == 'y' else False
        
        text = format_text(read_file(f), s)
        count = ngram_processing(text, n, count=True)
        freqs = probability(n, text, round_by=ROUND_FLOAT)
        entr = entropy(freqs)

        print(f"Count is:")
        print_dict(count)
        print("Frequencies (probabilities) are:")
        print_dict(freqs)
        print(f"Entropy (n = {n}, with{'' if s else 'out'} spaces) is:\n{entr}")
    else:
        print(
            """USAGE: ./cp1.py FILENAME ALLOW_SPACES N 
            [*] FILENAME\t- path to the text file
            [*] ALLOW_SPACES - leave spaces in text(y or n)
            [*] N\t\t- n-gram length (N >= 1)""")
