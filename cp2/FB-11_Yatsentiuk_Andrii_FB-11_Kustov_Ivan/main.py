with open('text.txt', 'r', encoding = 'utf-8') as file:
    file_contents = file.read()
    file_contents = file_contents.lower()

file_contents = file_contents.replace(",","")
file_contents = file_contents.replace("!","")
file_contents = file_contents.replace("?","")
file_contents = file_contents.replace("=","")
file_contents = file_contents.replace("-","")
file_contents = file_contents.replace("_","")
file_contents = file_contents.replace(".","")
file_contents = file_contents.replace(":","")
file_contents = file_contents.replace(";","")
file_contents = file_contents.replace("1","")
file_contents = file_contents.replace("2","")
file_contents = file_contents.replace("3","")
file_contents = file_contents.replace("4","")
file_contents = file_contents.replace("5","")
file_contents = file_contents.replace("6","")
file_contents = file_contents.replace("7","")
file_contents = file_contents.replace("8","")
file_contents = file_contents.replace("9","")
file_contents = file_contents.replace("0","")
file_contents = file_contents.replace(" ", "")
file_contents = file_contents.replace("'", "")
file_contents = file_contents.replace("\n", "")



ukrainian_lowercase = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def Encoding(text, key): # only lowercase text without spaces, key is also lowercase
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    key_array = []
    for char in key:
        key_array.append(ukrainian_alphabet.index(char))
    result = ""
    i = 0
    while i < len(text):
        plain_pos = ukrainian_alphabet.index(text[i])
        new_pos = (plain_pos+key_array[i%len(key_array)])%len(ukrainian_alphabet)
        result = result + ukrainian_alphabet[new_pos]
        i = i + 1
    return result


def Decode(text, key):
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
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

#encoding
text = file_contents
key = "ва"
encoded = Encoding(text, key)
with open("encoded_output2.txt", "w") as file:
    file.write(encoded)
print(encoded)

#encoding
text = file_contents
key = "гжя"
encoded = Encoding(text, key)
with open("encoded_output3.txt", "w") as file:
    file.write(encoded)
print(encoded)

#encoding
text = file_contents
key = "фрмя"
encoded = Encoding(text, key)
with open("encoded_output4.txt", "w") as file:
    file.write(encoded)
print(encoded)

#encoding
text = file_contents
key = "щгрхя"
encoded = Encoding(text, key)
with open("encoded_output5.txt", "w") as file:
    file.write(encoded)
print(encoded)

#encoding
text = file_contents
key = "шякрамифжє"
encoded = Encoding(text, key)
with open("encoded_output10.txt", "w") as file:
    file.write(encoded)
print(encoded)

#print(file_contents)
