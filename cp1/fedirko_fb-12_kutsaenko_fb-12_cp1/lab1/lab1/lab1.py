import re
from collections import Counter
from math import log

# Функція для підрахунку частот букв в тексті
def calculate_letter_frequencies(text):
    text = re.sub(r'[^а-яё]', ' ', text.lower())  # Видалити всі символи, крім російських букв
    letter_frequencies = Counter(text)
    total_letters = len(text)
    letter_probabilities = {letter: count / total_letters for letter, count in letter_frequencies.items()}
    return letter_probabilities

# Функція для підрахунку частот біграм в тексті
def calculate_bigram_frequencies(text):
    text = re.sub(r'[^а-яё]', ' ', text.lower())  # Видалити всі символи, крім російських букв
    bigrams = [text[i:i+2] for i in range(len(text) - 1)]
    bigram_frequencies = Counter(bigrams)
    total_bigrams = len(bigrams)
    bigram_probabilities = {bigram: count / total_bigrams for bigram, count in bigram_frequencies.items()}
    return bigram_probabilities

# Функція для обчислення значення H1 за безпосереднім визначенням
def calculate_h1(probabilities):
    return -sum(prob * log(prob, 2) for prob in probabilities.values())

# Функція для обчислення значення H2 за безпосереднім визначенням
def calculate_h2(probabilities):
    return -sum(prob**2 * log(prob, 2) for prob in probabilities.values())

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
bigram_probabilities = calculate_bigram_frequencies(text)

# Обчислення H1 та H2 за безпосереднім визначенням
h1 = calculate_h1(letter_probabilities)
h2 = calculate_h2(bigram_probabilities)
print(text)
print("Частоти букв:")
print(letter_probabilities)
print("\nH1:", h1)
print("\nЧастоти біграм:")
print(bigram_probabilities)
print("\nH2:", h2)

# Вилучення всіх пробілів з тексту
text_without_spaces = text.replace(" ", "")

# Обчислення H1 та H2 на тексті без пробілів
letter_probabilities_no_spaces = calculate_letter_frequencies(text_without_spaces)
bigram_probabilities_no_spaces = calculate_bigram_frequencies(text_without_spaces)
h1_no_spaces = calculate_h1(letter_probabilities_no_spaces)
h2_no_spaces = calculate_h2(bigram_probabilities_no_spaces)

#print("\nТекст без пробілів:")
#print(text_without_spaces)
print("\nЧастоти букв (без пробілів):")
print(letter_probabilities_no_spaces)
print("\nH1 (без пробілів):", h1_no_spaces)
print("\nЧастоти біграм (без пробілів):")
print(bigram_probabilities_no_spaces)
print("\nH2 (без пробілів):", h2_no_spaces)
