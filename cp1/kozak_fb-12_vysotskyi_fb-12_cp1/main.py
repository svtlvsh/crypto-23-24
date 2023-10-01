from re import sub

path = "text.txt"

def clean_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    text = sub("[^а-яё ]", " ", text)
    text = sub("\s+", " ", text )
    return text

def save_text(filepath, text):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

