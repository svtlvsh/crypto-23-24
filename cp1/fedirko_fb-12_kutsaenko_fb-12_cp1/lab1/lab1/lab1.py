import string
import re
from collections import Counter
from math import log

# Функція для підрахунку частот букв в тексті
def calculate_letter_frequencies(text):
    text = re.sub(r'[^а-яё]', ' ', text.lower())  # Видалити всі символи, крім російських букв та пробілів
    letter_frequencies = Counter(text)
    total_letters = len(text)
    letter_probabilities = {letter: count / total_letters for letter, count in letter_frequencies.items()}
    sorted_probabilities = dict(sorted(letter_probabilities.items(), key=lambda x: x[1], reverse=True))
    return sorted_probabilities

# Функція для підрахунку частот біграм в тексті та створення матриці частот
def calculate_bigram_frequencies(text):
    text = re.sub(r'[^а-яё ]', ' ', text.lower())
    bigrams = [text[i:i+2] for i in range(len(text) - 1)]
    bigram_frequencies = Counter(bigrams)
    total_bigrams = len(bigrams)

    # Створення матриці частот біграм
    alphabet = list(" абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    bigram_matrix = [[0] * len(alphabet) for _ in range(len(alphabet))]

    for bigram, count in bigram_frequencies.items():
        first_letter, second_letter = bigram
        first_index = alphabet.index(first_letter)
        second_index = alphabet.index(second_letter)
        bigram_matrix[first_index][second_index] = count / total_bigrams

    return bigram_matrix, alphabet

# Функція для підрахунку частот біграм в тексті без пробілів та створення матриці частот
def calculate_bigram_frequencies_no_spaces(text):
    text = re.sub(r'[^а-яё]', '', text.lower())  # Вилучити всі символи, крім російських букв
    bigrams = [text[i:i+2] for i in range(len(text) - 1)]
    bigram_frequencies_no_spaces = Counter(bigrams)
    total_bigrams_no_spaces = len(bigrams)

    # Створення матриці частот біграм
    alphabet_no_spaces = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    bigram_matrix_no_spaces = [[0] * len(alphabet_no_spaces) for _ in range(len(alphabet_no_spaces))]

    for bigram, count in bigram_frequencies_no_spaces.items():
        first_letter, second_letter = bigram
        first_index = alphabet_no_spaces.index(first_letter)
        second_index = alphabet_no_spaces.index(second_letter)
        bigram_matrix_no_spaces[first_index][second_index] = count / total_bigrams_no_spaces

    return bigram_matrix_no_spaces, alphabet_no_spaces


# Функція для обчислення значення H1 за безпосереднім визначенням
def calculate_h1(probabilities):
    return -sum(prob * log(prob, 2) for prob in probabilities.values())

# Функція для обчислення значення H2 за безпосереднім визначенням
def calculate_h2(bigram_matrix):
    EPSILON = 1e-10  # Доданий малий епсілон, щоб уникнути log(0)
    return -sum(prob**2 * log((prob**2) + EPSILON, 2) for row in bigram_matrix for prob in row)

# Зчитування тексту з файлу
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        text = file.read()
    return text

# Задайте шлях до файлу, який містить текст
file_path = 'H:\web\Te.txt'

# Зчитайте текст з файлу
text = read_text_from_file(file_path)

# Обчислення частот букв та біграм
letter_probabilities = calculate_letter_frequencies(text)
bigram_matrix, unique_bigrams = calculate_bigram_frequencies(text)
h1 = calculate_h1(letter_probabilities)
h2 = calculate_h2(bigram_matrix)

print("Частоти букв (відсортовані за спаданням):")
for letter, probability in letter_probabilities.items():
    print(f"{letter}: {probability:.4f}")
print("\nH1",h1)    

print("\nМатриця частот біграм:")
print("   " + " ".join(unique_bigrams))
for i, row in enumerate(bigram_matrix):
    print(f"{unique_bigrams[i]} " + " ".join([f"{prob:.4f}" for prob in row]))
print("\nH2",h2)
text_without_spaces = text.replace(" ", "")

# Обчислення H1 та H2 на тексті без пробілів
letter_probabilities_no_spaces = calculate_letter_frequencies(text_without_spaces)
bigram_matrix_no_spaces, unique_bigrams_no_spaces = calculate_bigram_frequencies_no_spaces(text_without_spaces)
h1_no_spaces = calculate_h1(letter_probabilities_no_spaces)
h2_no_spaces = calculate_h2(bigram_matrix_no_spaces)

print("\nТекст без пробілів:")
print(text_without_spaces)
print("Частоти букв (відсортовані за спаданням):")
for letter, probability in letter_probabilities_no_spaces.items():
    print(f"{letter}: {probability:.4f}")
print("\nH1 (без пробілів):", h1_no_spaces)
print("\nМатриця частот біграм:")
print("   " + " ".join(unique_bigrams_no_spaces))
for i, row in enumerate(bigram_matrix_no_spaces):
    print(f"{unique_bigrams_no_spaces[i]} " + " ".join([f"{prob:.4f}" for prob in row]))
print("H2 (без пробілів):", h2_no_spaces)