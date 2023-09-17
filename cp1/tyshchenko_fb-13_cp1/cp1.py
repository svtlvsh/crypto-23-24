#!/usr/bin/python3

from math import log

ALPHABET_LEN = 32
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
def probability(n: int, text: str) -> dict:
    ngrams = ngram_processing(text, n, count=True)
    total = sum(ngrams.values())
    probabilities = {ngr : count / total for ngr, count in ngrams.items()}
    return probabilities
    
def conditional_probability(n: int, text: str) -> dict:
    # n = m + 1
    ngrams = ngram_processing(text, n)
    mgrams = ngram_processing(text, n - 1)
    possibilities = dict.fromkeys(ngrams, 0)
    for ngr in ngrams:
        for mgr in mgrams:
            if ngr[:len(mgr)] == mgr:
                possibilities[ngr] += 1
    total = sum(possibilities.values())
    cond_probabilities = {ngr : count / total for ngr, count in possibilities.items()}
    return cond_probabilities
    
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

# It is used for calculating both simple and conditional entropy
def entropy(probabilities: dict) -> float:
    entropy = -sum(p * log(p, 2) for p in probabilities.values())
    return entropy

# Testing functions
#print(ngram_processing("abcde", 2))
text = read_file("small.txt")
text = format_text(text)

cp_10 = conditional_probability(10, text)
#print(f"H^(10) = {cp_10}")
cp_20 = conditional_probability(20, text)
#print(f"H^(20) = {cp_20}")
cp_30 = conditional_probability(30, text)
#print(f"H^(30) = {cp_30}")
print(f"H_cond(cp_10) = \n{entropy(cp_10)}")
print(f"H_cond(cp_20) = \n{entropy(cp_20)}")
print(f"H_cond(cp_30) = \n{entropy(cp_30)}")
'''
text_spaceless = read_file("temp.txt")
text_spaceless = format_text(text_spaceless, allow_spaces=False)
letter_count = ngram_processing(text, 1, count=True)
letter_count_spaceless = ngram_processing(text_spaceless, 1, count=True)
bigram_count = ngram_processing(text, 2, count=True)
bigram_count_spaceless = ngram_processing(text_spaceless, 2, count=True)
letter_freqs = probability(1, text)
#print(f"Letter probability is:\n{letter_freqs}")
letter_freqs_spaceless = probability(1, text_spaceless)
bigram_freqs = probability(2, text)
bigram_freqs_spaceless = probability(2, text_spaceless)
#print(f"Bigram probability is:\n{bigram_freqs}")
letter_entr = entropy(letter_freqs)
letter_entr_spaceless = entropy(letter_freqs_spaceless)
bigram_entr = entropy(bigram_freqs)
bigram_entr_spaceless = entropy(bigram_freqs_spaceless)
#print(f"Text is:\n{text}")
#print(f"Letter count is:\n{letter_count}")
#print(f"Bigram count is:\n{bigram_count}")
print(f"Letter entropy is:\n{letter_entr}")
print(f"Bigram entropy is:\n{bigram_entr}")
print(f"Letter entropy without spaces is:\n{letter_entr_spaceless}")
print(f"Bigram entropy without spaces is:\n{bigram_entr_spaceless}")
#print("Bigram frequency (probability) matrix:")
#print_bigram_probability(bigram_freqs)
'''
