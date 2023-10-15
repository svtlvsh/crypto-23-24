from random import choice
import csv


# Алфавіт
ALPHABET: str = 'абвгдежзийклмнопрстуфхцчшщыьэюя'


# Ця функція зчитує текстовий файл та поверає string з текстом цього файлу
def file_read(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        text: str = file.read()
    return text


# Ця функція створює ключ певної довжини
def key_generate(key_len) -> str:
    new_key = ''.join(choice(ALPHABET) for i in range(key_len))
    return new_key


# Ця функція рахує індекси відповідності
def affinity_index(encrypted_text: str) -> float:
    frequency: dict = {}
    affinity: float = 0.0
    for char in encrypted_text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 0
    for char in frequency:
        affinity += (frequency[char] * (frequency[char] - 1)) / \
                    (len(encrypted_text) * len(encrypted_text) - 1)
    return affinity


# Ця функція створює csv файл з результатами
def create_csv_file(filename: str, affinity_dict: dict):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Довжина ключа", "Індекс"])
        for affinity in affinity_dict:
            if affinity == 'Вхідний текст':
                key_len = 'Вхідний текст'
            else:
                key_len = len(affinity)
            affinity = affinity_dict[affinity]
            affinity = affinity.replace('.', ',')
            writer.writerow([key_len, affinity])