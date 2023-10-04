import re

def filter():
    with open("variant_2.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    # Робимо всі букви маленькими
    text = text.lower()

    # Прибираєм все, що не входить в російський алфавіт, лишаєм пробіли
    text = re.sub(r'[^\sа-я]', '', text)

    # Прибираємо подвійні пробіли, або всі пробіли
    text = re.sub(r'\s+', '', text)

    with open("variant_2.txt", 'w', encoding='utf-8') as file:
        file.write(text)

#filter()

def shifr_vigenera(key):

    with open('2.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Оголошуємо алфавіт, який ми будемо використовувати для шифрування.
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = []  # Список для зберігання зашифрованого тексту.

    key_index = 0  # Змінна для відстеження поточного індексу символа ключа.

    # Проходимо через кожен символ вхідного тексту.
    for char in text:

        char_index = alphabet.index(char)  # Знаходимо індекс поточної літери тексту.

        # Отримуємо поточний символ ключа
        key_char = key[key_index % len(key)]
        key_index += 1

        # Знаходимо індекс поточного символа ключа в алфавіті.
        key_char_index = alphabet.index(key_char)

        # Обчислюємо індекс символа зашифрованого тексту, додаючи індекси символів тексту та ключа.
        encrypted_char_index = (char_index + key_char_index) % len(alphabet)

        # Знаходимо символ зашифрованого тексту, використовуючи обчислений індекс.
        encrypted_char = alphabet[encrypted_char_index]

        # Додаємо символ зашифрованого тексту до списку зашифрованого тексту.
        result.append(encrypted_char)

    return ''.join(result)

key = 'суперкороваходитднем'

encrypted_text = shifr_vigenera(key)

with open('3.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

def index_vidpovidnosti():
    with open("variant_2.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    dictionary = {}
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for char in alphabet:
        dictionary[char] = 0

    for item in list(text):
        if item in dictionary:
            dictionary[item] += 1

    print(dictionary)

    suma = 0
    for i in alphabet:
        suma += dictionary[i] * (dictionary[i] - 1)
    suma = (1/(len(text)*(len(text)-1))) * suma
    return print(suma)

index_vidpovidnosti()

def index_vidpovidnosti_help(text):

    dictionary = {}
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for char in alphabet:
        dictionary[char] = 0

    for item in list(text):
        if item in dictionary:
            dictionary[item] += 1

    suma = 0
    for i in alphabet:
        suma += dictionary[i] * (dictionary[i] - 1)
    suma = (1/(len(text)*(len(text)-1))) * suma
    return suma

def find_r(r):
    with open("variant_2.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    array = []
    for i in range(0, len(text), r):
        n_gram = text[i:i + r]
        if len(n_gram) == r:
            array.append(n_gram)

    suma_r = 0
    for i in range(0, len(array)-1):
        suma_r += index_vidpovidnosti_help(array[i])
    suma_r = suma_r / len(array)
    return print(suma_r)

for i in range(2, 30):
    find_r(i)

