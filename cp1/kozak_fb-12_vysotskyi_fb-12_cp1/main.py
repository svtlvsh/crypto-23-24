from re import sub

path = "clean_text.txt"

def clean_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    text = sub("[^а-яё ]", " ", text)
    text = sub("\s+", " ", text)
    return text

def save_text(filepath, text):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

def read_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def count_letters(filepath):    # Підрахунок літер у тексті
    letter_dict = {}
    text = read_text(filepath)
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


