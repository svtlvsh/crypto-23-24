from collections import Counter
import math
import numpy as np
import pandas as pd
import re


# Function to open and read a text file, converting it to lowercase
def read_file(t):
    with open(t, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Function to edit text: remove non-Russian letters, reduce spaces, and replace "ъ" and "ё"
def filter_text(t):
    text = read_file(t).lower()

    # Remove non-Russian letters
    text = re.sub("[^а-я]", " ", text)

    # Reduce multiple spaces to a single space
    text = re.sub(r'\s+', ' ', text)

    # Replace "ъ" with "ь" and "ё" with "е"
    text = text.replace("ъ", "ь").replace("ё", "е")

    return text


# Function to delete spaces from a text file
def delete_spaces(t):
    # Remove all spaces
    return re.sub(r'\s+', '', t)


# Function to count monograms (single characters) and calculate entropy
def count_letters(t):
    count_m = Counter(t)

    # Normalize the counts to get frequencies
    for i in count_m.keys():
        count_m[i] = count_m[i] / len(t)

    # Sort and print monogram frequencies in descending order
    display_dict_as_table(dict(sorted(count_m.items(), key=lambda item: item[1], reverse=True)))

    entropy_m = 0

    # Calculate entropy for monograms
    for i in count_m.keys():
        entropy_m += (-count_m[i] * math.log2(count_m[i]))

    # Print the calculated entropy for monograms
    print(f"Letter entropy in monograms: {round(entropy_m, 10)}")
    return entropy_m


# Function to count bigrams (pairs of characters) and calculate entropy
def count_bigrams(t, spaces, intersection):
    if intersection:
        # Create bigrams with overlapping characters
        bigram = [t[i:i + 2] for i in range(len(t))]
        _intersection = "_with_intersection"
    else:
        # Create non-overlapping bigrams
        bigram = [t[i:i + 2] for i in range(0, len(t) - 1 if len(t) % 2 == 1 else len(t), 2)]
        _intersection = "_without_intersection"
    if spaces:
        _spaces = "_with_spaces"
    else:
        _spaces = "_without_spaces"
    count_b = Counter(bigram)

    # Calculate bigram frequencies
    freq_b = {i: round(count_b[i] / len(bigram), 10) for i in count_b}

    # Sort and print bigram frequencies in descending order
    display_bigram_matrix(dict(sorted(freq_b.items(), key=lambda item: item[1], reverse=True)), "text"+_spaces+_intersection+".xlsx")
    entropy_b = 0

    # Calculate entropy for bigrams
    for i in freq_b.keys():
        entropy_b += - (freq_b[i]) * math.log2(freq_b[i])

    # Divide by 2 to calculate entropy for individual symbols, not bigrams
    entropy_b = entropy_b / 2

    # Print the calculated entropy for letters in bigrams
    print(f"Letter entropy in bigrams: {entropy_b}")
    return entropy_b


def display_dict_as_table(dictionary):
    df = pd.DataFrame(list(dictionary.items()), columns=['Letter', 'Frequency'])

    print(df)


def display_bigram_matrix(bigram_dict, file):
    # List of unique letters
    unique_letters = sorted(set(bigram[0] for bigram in bigram_dict.keys()))

    # Initialize matrix
    matrix_size = len(unique_letters)
    matrix = np.zeros((matrix_size, matrix_size))

    # Fillup matrix with frequences
    for i, letter1 in enumerate(unique_letters):
        for j, letter2 in enumerate(unique_letters):
            bigram = letter1 + letter2
            if bigram in bigram_dict:
                matrix[i][j] = bigram_dict[bigram]

    # Create DataFrame and output it
    df = pd.DataFrame(matrix, index=unique_letters, columns=unique_letters)
    df.to_excel(file, index=True, engine='openpyxl')
    print(df)


if __name__ == "__main__":

    # Filter text
    text_with_spaces = filter_text("source.txt")
    text_without_spaces = delete_spaces(text_with_spaces)

    # Calculate monogram statistics for text with spaces
    print("Monograms in text with spaces:")
    entropy = count_letters(text_with_spaces)
    print(f"Redundancy: {1 - (entropy / math.log2(32))}\n")

    # Calculate monogram statistics for text without spaces
    print("Monograms in text without spaces:")
    entropy = count_letters(text_without_spaces)
    print(f"Redundancy: {1 - (entropy / math.log2(31))}\n")

    # Calculate bigram statistics for text with spaces with and without intersection
    print("Bigrams in text with spaces and with intersection:")
    entropy = count_bigrams(text_with_spaces, True, True)
    print(f"Redundancy: {1 - (entropy / math.log2(32))}\n")

    print("Bigrams in text with spaces and without intersection:")
    entropy = count_bigrams(text_with_spaces, True, False)
    print(f"Redundancy: {1 - (entropy / math.log2(32))}\n")

    # Calculate bigram statistics for text without spaces with and without intersection
    print("Bigrams in text without spaces and with intersection:")
    entropy = count_bigrams(text_without_spaces, False, True)
    print(f"Redundancy: {1 - (entropy / math.log2(31))}\n")

    print("Bigrams in text without spaces and without intersection:")
    entropy = count_bigrams(text_without_spaces, False, False)
    print(f"Redundancy: {1 - (entropy / math.log2(31))}\n")
