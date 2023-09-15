#!/usr/bin/python3

from math import log

ALPHABET_LEN = 32
ROUND_FLOAT = 3

def frequency(ngrams: dict, text: str) -> dict:
    # get length of the ngram in dict
    n = len(list(ngrams.keys())[0])
    total = len(text) - n + 1
    frequencies = {ngr : count / total for (ngr, count) in ngrams.items()}
    return frequencies
    
def print_bigram_frequency(frequencies: dict) -> None:
    # check if frequencies correspond to bigrams 
    if len(list(frequencies.keys())[0]) != 2:
        print("Failed to show frequencies of ngrams: n != 2")
    else:
        # second letter (without duplicates)
        second_letter = list(set([x[1] for x in frequencies]))
        # first letter (without duplicates)
        first_letter = list(set([x[0] for x in frequencies]))
        # put in ablphabetical order
        first_letter.sort()
        second_letter.sort()
        data = []
        for i in range(len(first_letter)):
            row = [0] * len(second_letter)
            for j in range(len(second_letter)):
                ngr = f"{first_letter[i]}{second_letter[j]}"
                if ngr in frequencies:
                    row[j] = round(frequencies[ngr], ROUND_FLOAT)
            data.append(row)
        format_row = "{:>8}" * (len(second_letter) + 1)
        print(format_row.format("", *second_letter))
        for letter, value in zip(first_letter, data):
            print(format_row.format(letter, *value))

# frequency = probability (ngram count -> infinity)
def entropy(probabilities: list) -> float:
    entropy = 0
    for p in probabilities.values():
        entropy += p * log(p, 2)
    return -entropy
 
def count_ngram(text: str, n: int) -> dict:
    ngrams = {}
    text_len = len(text)
    for s in range(text_len - n + 1):
        ngr = text[s:s + n]
        if ngr not in ngrams:
            ngrams[ngr] = text.count(ngr)
    return ngrams
    
def read_file(fname: str, spaces=True) -> str:
    allowed = "абвгдежзийклмнопрстуфхцчшщыьэюя "
    with open(fname, "r") as f:
        text = f.read()
        f.close()
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
    if spaces:
        text = " ".join(temp)
    else:
        text = "".join(temp)
    return text
    
# Testing functions
text = read_file("temp.txt", spaces=True)
text_spaceless = read_file("temp.txt", spaces=False)
letter_count = count_ngram(text, 1)
letter_count_spaceless = count_ngram(text_spaceless, 1)
letter_freqs = frequency(letter_count, text)
#print(f"Letter frequency is:\n{letter_freqs}")
letter_freqs_spaceless = frequency(letter_count_spaceless, text_spaceless)
bigram_count = count_ngram(text, 2)
bigram_count_spaceless = count_ngram(text_spaceless, 2)
bigram_freqs = frequency(bigram_count, text)
#print(f"Bigram frequency is:\n{bigram_freqs}")
bigram_freqs_spaceless = frequency(bigram_count_spaceless, text_spaceless)
letter_entr = entropy(letter_freqs)
letter_entr_spaceless = entropy(letter_freqs_spaceless)
bigram_entr = entropy(bigram_freqs)
bigram_entr_spaceless = entropy(bigram_freqs_spaceless)
#print(f"Text is:\n{text}")
#print(f"Letter count is:\n{letter_count}")
#print(f"Bigram count is:\n{bigram_count}")
#print(f"Letter entropy is:\n{letter_entr}")
#print(f"Bigram entropy is:\n{bigram_entr}")
#print(f"Letter entropy without spaces is:\n{letter_entr_spaceless}")
#print(f"Bigram entropy without spaces is:\n{bigram_entr_spaceless}")
print("Frequency matrix:")
print_bigram_frequency(bigram_freqs)
