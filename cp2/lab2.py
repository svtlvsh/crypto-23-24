# Function to encrypt plaintext with Vigenère cipher
def vigenere_cipher(plaintext, key):
    encrypted_text = []
    repeat_count = len(plaintext) // len(key)
    key_repeated = key * repeat_count
    key_repeated += key[:len(plaintext) - len(key_repeated)]
    plaintext=[*plaintext]
    key_repeated=[*key_repeated]
    for i in range(0,len(plaintext)):
        encrypted_text.append(chr((ord(plaintext[i])-1071+ord(key_repeated[i])-1071)%32 +1071))
    return "".join(encrypted_text)


def find_freq(formated_text):
    letter_frequency = {}
    for litera in formated_text:
        if litera in letter_frequency:
            letter_frequency[litera] += 1
        else:
            letter_frequency.update({litera: 1})
    return letter_frequency
def print_freq(let_freq,formated_text):
    print("загальна "," відсоток від ")
    print("кількість"," загального")
    for letter, frequency in sorted(let_freq.items(), key=lambda x:x[1], reverse=True):
        print(f"{letter}: {frequency},    %= {round(int(frequency)/len(formated_text)*100,3)}")
    return None
def calc_IC(letter_freq,total_length):
    ic = 0.0
    for count in letter_freq.values():
        ic += (count * (count - 1)) / (total_length * (total_length - 1))
    return ic

input_file_path = 'D:\\uni year 3\\crypto labs\\crypto-23-24\\cp2\\test.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:

    text = file.read()
text.replace('\n'," ")
text1_freq=find_freq(text)

# print_freq(text1_freq,text)
print(calc_IC(text1_freq,len(text)))

# Read input text from a file
input_file = "D:\\uni year 3\\crypto labs\\crypto-23-24\\cp2\\input_to_cipher.txt"
with open(input_file, "r",encoding='utf-8') as file:
    plaintext = file.read()
# Specify the key
key = "арбуз"

# Encrypt the plaintext using the Vigenère cipher
encrypted_text = vigenere_cipher(plaintext, key)
text2_freq=find_freq(encrypted_text)
print(calc_IC(text2_freq,len(encrypted_text)))
print(encrypted_text)