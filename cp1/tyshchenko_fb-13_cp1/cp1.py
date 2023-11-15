#!/usr/bin/python3

from collections import Counter
from math import log
import sys

COLUMN_NUM = 4
ROUND_FLOAT = 3
ALPHABET = "абвгдежзийклмнопрстуфхцчшщыьэюя "
M = len(ALPHABET)

def read_file(fname: str) -> str:
    with open(fname, "r") as f:
        text = f.read()
    return text
    
def format_text(text: str, allow_spaces=True) -> str:
    # remove uppercase letters
    text = text.lower()
    # replace some letters
    text = text.replace("ё", "е")
    text = text.replace("ъ", "ь")
    # remove other symbols
    for i in range(len(text)):
        if text[i] not in ALPHABET:
            text = text.replace(text[i], " ")
    # remove extra whitespaces or all of them
    temp = text.split()
    if allow_spaces:
        text = " ".join(temp)
    else:
        text = "".join(temp)
    return text

def ngram_processing(text: str, n: int, count=True, step=1):
    text_len = len(text)
    ngrams = [text[s:s + n] for s in range(0, text_len - n + 1, step)]
    ngram_count = Counter(ngrams)
    if count:
        return ngram_count
    else:
        return ngrams

# frequency = probability (ngram count -> infinity)
def probability(n: int, text: str, round_by=ROUND_FLOAT, step=1) -> dict:
    ngrams = ngram_processing(text, n, count=True, step=step)
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
        freqs = dict(sorted(dictionary.items(), reverse=True, key=lambda item: item[1]))
        size = len(freqs)
        counter = 0
        for i in freqs:
            print(f'\t"{i}" - {freqs[i]}\t', end='')
            if (counter + 1) % COLUMN_NUM == 0 or counter + 1 == size:
                print("")
            counter += 1

def entropy(probabilities: dict) -> float:
    return -sum(p * log(p, 2) for p in probabilities.values() if p > 0)
    
def entropy_n(entr: float, n: int) -> float:
    return entr / n
    
def redundancy(entr_n: float, m: int) -> float:
    return 1 - entr_n / log(m, 2)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = sys.argv[1]
        
        # "1" - for letters, "2" - for bigrams
        # "sp" - with spaces, "st" - with step
        text_sp = format_text(read_file(f), allow_spaces=True)
        text = format_text(text_sp, allow_spaces=False)
        
        freqs1_sp = probability(1, text_sp, round_by=ROUND_FLOAT)
        freqs1 = probability(1, text, round_by=ROUND_FLOAT)
        freqs2_sp = probability(2, text_sp, round_by=ROUND_FLOAT)
        freqs2 = probability(2, text, round_by=ROUND_FLOAT)
        freqs2_sp_st = probability(2, text_sp, round_by=ROUND_FLOAT, step=2)
        freqs2_st = probability(2, text, round_by=ROUND_FLOAT, step=2)
        
        entr1_sp = entropy(freqs1_sp)
        entr1 = entropy(freqs1)
        entr2_sp = entropy_n(entropy(freqs2_sp), 2)
        entr2 = entropy_n(entropy(freqs2), 2)
        entr2_sp_st = entropy_n(entropy(freqs2_sp_st), 2)
        entr2_st = entropy_n(entropy(freqs2_st), 2)
        
        red1_sp = redundancy(entr1_sp, M)
        red1 = redundancy(entr1, M-1)
        red2_sp = redundancy(entr2_sp, M)
        red2 = redundancy(entr2, M-1)
        red2_sp_st = redundancy(entr2_sp_st, M)
        red2_st = redundancy(entr2_st, M-1)

        print("\nFrequencies (n = 1, with spaces) are:")
        print_dict(freqs1_sp)
        print("\nFrequencies (n = 1, without spaces) are:")
        print_dict(freqs1)
        print("\nFrequencies (n = 2, with spaces) are:")
        print_dict(freqs2_sp)
        print("\nFrequencies (n = 2, without spaces) are:")
        print_dict(freqs2)
        print("\nFrequencies (n = 2, with spaces, read with step) are:")
        print_dict(freqs2_sp_st)
        print("\nFrequencies (n = 2, without spaces, read with step) are:")
        print_dict(freqs2_st)
        
        print(f"\nEntropy_n (n = 1, with spaces) is:\n\t{entr1_sp}")
        print(f"\nEntropy_n (n = 1, without spaces) is:\n\t{entr1}")
        print(f"\nEntropy_n (n = 2, with spaces) is:\n\t{entr2_sp}")
        print(f"\nEntropy_n (n = 2, without spaces) is:\n\t{entr2}")
        print(f"\nEntropy_n (n = 2, with spaces, with step) is:\n\t{entr2_sp_st}")
        print(f"\nEntropy_n (n = 2, without spaces, with step) is:\n\t{entr2_st}")
        
        print(f"\nRedundancy (n = 1, with spaces) is:\n\t{red1_sp}")
        print(f"\nRedundancy (n = 1, without spaces) is:\n\t{red1}")
        print(f"\nRedundancy (n = 2, with spaces) is:\n\t{red2_sp}")
        print(f"\nRedundancy (n = 2, without spaces) is:\n\t{red2}")
        print(f"\nRedundancy (n = 2, with spaces, with step) is:\n\t{red2_sp_st}")
        print(f"\nRedundancy (n = 2, without spaces, with step) is:\n\t{red2_st}")
    else:
        print(
            """USAGE: ./cp1.py INPUTFILE
            [*] INPUTFILE\t- path to the input file""")
