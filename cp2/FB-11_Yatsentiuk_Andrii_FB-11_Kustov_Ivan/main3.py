with open('message.txt', 'r', encoding = 'utf-8') as file: #8143 символа
    file_contents = file.read()
    file_contents = file_contents.lower()

def IndexVidpovidnosty(encoded_text):
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    length = len(encoded_text)
    j = 0
    sum = 0
    while j < len(ukrainian_alphabet):
        encoded_text_count = encoded_text.count(ukrainian_alphabet[j])
        sum = sum + (encoded_text_count * (encoded_text_count - 1))
        j = j + 1
    result = (1/(length * (length-1))) * sum
    return result




