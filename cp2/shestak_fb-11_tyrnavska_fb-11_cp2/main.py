import text_manipulator
from collections import defaultdict


alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # 32
al_len = 32
first_char = ord('а')  # 1072

alphabet_dict = defaultdict()
for l in alphabet:
    alphabet_dict[l] = ord(l) - 1071

print(alphabet_dict)


def key_to_nums(key):
    num_key = [alphabet_dict[x] for x in list(key)]
    return num_key

# print(key_to_nums('привет'))


def vig_encrypt(key, text):
    encrypted_text = ''
    key_len = len(key)
    for i in range(len(text)):
        l = text[i]
        k = key[i % key_len]
        encrypted_text += chr((ord(l) - 1072 + k) % 32 + 1072)

    return encrypted_text

encrypted = vig_encrypt(key_to_nums('да'), 'привет')
print(encrypted)
print(vig_encrypt([-5, -1], encrypted))
