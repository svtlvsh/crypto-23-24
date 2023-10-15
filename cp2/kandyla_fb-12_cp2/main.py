from random import randint
def main():
    unfiltered = "unfiltered.txt"
    filtered = "filtered.txt"
    encoded = {"r2.txt": 2, "r3.txt": 3, "r4.txt": 4, "r5.txt": 5, "r10.txt": 10, "r15.txt": 15, "r20.txt": 20}
    text_filter(unfiltered, filtered)
    for file in encoded.keys():
        encode(encoded.get(file), filtered, file)


def text_filter(unfiltered_file, filtered_file):
    with open(unfiltered_file, 'r', encoding="utf8") as file:
        text = file.read().lower()
    new_string = ""
    allowed = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    for symbol in text:
        if symbol in allowed:
            new_string += symbol
        elif symbol == 'ё':
            new_string += 'е'
    final_text = ' '.join(new_string.split())
    with open(filtered_file, 'w', encoding="utf-8") as file:
        file.write(final_text)

def encode(r, filtered_file, output_file):
    with open(filtered_file, 'r', encoding="utf8") as file:
        text = file.read()
    num = randint(0, len(text))
    key = text[0:r]
    print(key)
    encoded_text = ""
    i = 0
    for symbol in text:
        encoded_text += chr((ord(symbol) + ord(key[i % r])) % 32 + 1072)
        i += 1
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(encoded_text)

if __name__ == "__main__":
    main()

