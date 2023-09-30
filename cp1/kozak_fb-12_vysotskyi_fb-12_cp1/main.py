from re import sub

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
print(len(ALPHABET))

path = "text.txt"

def clean_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    text = sub("[^а-яё\s]", "", text)
    text = text.replace("\n", " ")
    print(text[0:10000]) 

clean_text(path)

