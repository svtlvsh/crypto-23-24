import re
from collections import Counter

def filter_text(text):
    filtered_text = re.sub(r'[^А-Яа-яЁё ]', ' ', text).lower()
    filtered_text = re.sub(r'\s+', ' ', filtered_text)
    return filtered_text
def process_text(text):
    filtered_text = filter_text(text)
    letter_count = Counter(filtered_text)
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[0])
    return sorted_letter_count
def calculate_and_sort_letter_frequencies(text):
    filtered_text = filter_text(text)
    total_letters = len(filtered_text)
    letter_count = Counter(filtered_text)
    letter_frequencies = {letter: count / total_letters for letter, count in letter_count.items()}
    sorted_letter_frequencies = sorted(letter_frequencies.items())
    return sorted_letter_frequencies
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

file_path = 'text.txt'

input_text = load_text_from_file(file_path)

letter_frequencies = process_text(input_text)

print("Частота букв:")
for letter, count in letter_frequencies:
    print(f"{letter}: {count}")

letter_frequencies = calculate_and_sort_letter_frequencies(input_text)

print("\nЧастота появлення кожної букви:")
for letter, frequency in letter_frequencies:
    print(f"{letter}: {frequency:.6f}")


