from re import sub

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
print(len(ALPHABET))

def clean_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    text = sub("[^а-яё\s]", "", text) 
