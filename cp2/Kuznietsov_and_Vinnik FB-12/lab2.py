import re

def filter():
    with open("1.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    # Робимо всі букви маленькими
    text = text.lower()

    # Прибираєм все, що не входить в російський алфавіт, лишаєм пробіли
    text = re.sub(r'[^\sа-я]', '', text)

    # Прибираємо подвійні пробіли, або всі пробіли
    text = re.sub(r'\s+', '', text)

    with open("2.txt", 'w', encoding='utf-8') as file:
        file.write(text)

#filter()

def encrypt_vigenere(key):

    with open('2.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Оголошуємо алфавіт, який ми будемо використовувати для шифрування.
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = []  # Список для зберігання зашифрованого тексту.

    key_index = 0  # Змінна для відстеження поточного індексу символа ключа.

    # Проходимо через кожен символ вхідного тексту.
    for char in text:
        if char in alphabet:
            # Якщо символ є літерою з нашого алфавіту, продовжуємо шифрування.
            char_index = alphabet.index(char)  # Знаходимо індекс поточної літери тексту.

            # Отримуємо поточний символ ключа (циклічно, якщо ключ коротший за текст).
            key_char = key[key_index % len(key)]
            key_index += 1  # Збільшуємо індекс символа ключа для наступного символу тексту.

            # Знаходимо індекс поточного символа ключа в алфавіті.
            key_char_index = alphabet.index(key_char)

            # Обчислюємо індекс символа зашифрованого тексту, додаючи індекси символів тексту та ключа.
            encrypted_char_index = (char_index + key_char_index) % len(alphabet)

            # Знаходимо символ зашифрованого тексту, використовуючи обчислений індекс.
            encrypted_char = alphabet[encrypted_char_index]

            # Додаємо символ зашифрованого тексту до списку зашифрованого тексту.
            encrypted_text.append(encrypted_char)
        else:
            # Якщо символ не належить алфавіту, додаємо його без змін до зашифрованого тексту.
            encrypted_text.append(char)

    # Повертаємо зашифрований текст як рядок.
    return ''.join(encrypted_text)

key = 'жопа'

encrypted_text = encrypt_vigenere(key)

with open('3.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)