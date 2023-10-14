# Це ключі шифрування, довжиною 2, 3, 4, 5, 10 і 20 відповідно
KEYS: tuple = ('да', 'дуб', 'хлеб', 'туман', 'облачность', 'завтрапятницакайфуем')

# Алфавіт
ALPHABET: str = 'абвгдежзийклмнопрстуфхцчшщыьэюя'


# Ця функція зчитує текстовий файл та поверає string з текстом цього файлу
def file_read(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        text: str = file.read()
    return text


# Ця функція отримує текст та повертає редагований текст для подальшого аналізу
def text_edit(text: str) -> str:
    text = text.replace('ё', 'е')
    text = text.replace('ъ', 'ь')
    text = text.lower()
    text = ''.join(char for char in text if char in ALPHABET)
    text = text.replace(' ', '')
    return text


# Ця функція зашифровує текст
def encryption(key: str, input_text: str) -> str:
    global ALPHABET
    key_index: int = 0
    encrypted_text: str = ''
    for char in input_text:
        encrypted_char_index = (ALPHABET.index(char) + ALPHABET.index(key[key_index])) % len(ALPHABET)
        encrypted_char = ALPHABET[encrypted_char_index]
        encrypted_text += encrypted_char
        key_index += (key_index + 1) % len(key)
    return encrypted_text


# text = file_read('task1.txt')
# text = text_edit(text)
# print(encryption(KEYS[0], text))