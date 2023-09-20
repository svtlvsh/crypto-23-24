import re
import math

def filter():
    with open("1.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    # Робимо всі букви маленькими
    text = text.lower()

    # Прибираєм все, що не входить в російський алфавіт, лишаєм пробіли
    text = re.sub(r'[^\sа-яё]', '', text)

    # Прибираємо подвійні пробіли, або всі пробіли
    text = re.sub(r'\s+', ' ', text)

    with open("2.txt", 'w', encoding='utf-8') as file:
        file.write(text)

filter()

def chastota():
    with open("2.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    list(text)
    dictionary = {}
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "

    for char in alphabet:
        dictionary[char] = 0

    for item in list(text):
        if item in dictionary:
            dictionary[item] += 1

    print(dictionary)

    for i in alphabet:
        dictionary[i] = dictionary[i] / len(list(text))

    print(dictionary)

    suma = 0
    for i in alphabet:
        suma += (-1)*(dictionary[i] * math.log2(dictionary[i]))

    print(suma)

chastota()

def chastota_bigram():
    with open("2.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    dictionary = {}
    array = []

    for i in range(0, len(text), 2):
        bigram = text[i:i + 2]
        if len(bigram) == 2:
            array.append(bigram)

    for i in range(1, len(text), 2):
        bigram = text[i:i + 2]
        if len(bigram) == 2:
            array.append(bigram)

    #print(array)

    for i in array:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    print(dictionary)

    # Cортування біграм в спадному орядку
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    sorted_dictionary = dict(sorted_dictionary)

    print(sorted_dictionary)

    for i in list(sorted_dictionary.keys()):
        sorted_dictionary[i] = sorted_dictionary[i] / len(array)
        #sorted_dictionary[i] = round(sorted_dictionary[i], 5)

    print(sorted_dictionary)

    suma = 0
    for i in list(sorted_dictionary.keys()):
        suma += (-1) * (sorted_dictionary[i] * math.log2(sorted_dictionary[i])) / 2
    print(suma)

chastota_bigram()