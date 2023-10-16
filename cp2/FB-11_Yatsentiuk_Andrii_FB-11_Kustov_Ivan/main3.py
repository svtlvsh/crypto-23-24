

with open('message.txt', 'r', encoding = 'utf-8') as file:
    file_contents = file.read()
    file_contents = file_contents.lower()
    file_contents = file_contents.replace("\n","")

def closest_number(arr, target):
    return min(arr, key=lambda x: abs(x - target))

def IndexVidpovidnosty(encoded_text):
    ukrainian_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    length = len(encoded_text)
    j = 0
    sum = 0
    while j < len(ukrainian_alphabet):
        encoded_text_count = encoded_text.count(ukrainian_alphabet[j])
        sum = sum + (encoded_text_count * (encoded_text_count - 1))
        j = j + 1
    result = (1/(length * (length-1))) * sum
    return result


def Decode(text, key):
    ukrainian_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    key_array = []
    for char in key:
        key_array.append(ukrainian_alphabet.index(char))
    result = ""
    i = 0
    while i < len(text):
        encoded_pos = ukrainian_alphabet.index(text[i])
        new_pos = (encoded_pos - key_array[i%len(key_array)])%len(ukrainian_alphabet)
        result = result + ukrainian_alphabet[new_pos]
        i = i + 1
    return result










i = 1
while i < 51:
    temp_text = ""
    j = 0
    while j < (len(file_contents)):
        temp_text = temp_text + file_contents[j]
        j = j + i
    print(f"Індекс для ключа {i} - ", IndexVidpovidnosty(temp_text))
    i = i + 1


#13!!!!


