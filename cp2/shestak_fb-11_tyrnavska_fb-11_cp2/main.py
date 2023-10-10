import text_manipulator as tm
from collections import defaultdict


alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # 32
al_len = 32
first_char = ord('а')  # 1072
text = tm.get_text("valid_text_without_spaces.txt")
keys = ['да', 'нет', 'соль', 'сахар', 'синиймакар', 'светлоитеплосеогодня']


alphabet_dict = defaultdict()
for l in alphabet:
    alphabet_dict[l] = ord(l) - 1071


def key_to_nums(key):
    num_key = [alphabet_dict[x] for x in list(key)]
    return num_key


def vig_encrypt(key, text):
    encrypted_text = ''
    key_len = len(key)
    for i in range(len(text)):
        l = text[i]
        k = key[i % key_len]
        encrypted_text += chr((ord(l) - 1072 + k) % 32 + 1072)

    return encrypted_text


def index(text_ex):
    first_part = 1 / (len(text_ex) * (len(text_ex) - 1))
    second_part = [text.count(l)*(text.count(l)-1) for l in alphabet]
    second_part = sum(second_part)
    return first_part * second_part


def separator(text_ex, key_ex):
    groups = [[] for _ in range(len(key_ex))]

    for i in range(0, len(text_ex), len(key_ex)):
        for k in range(len(key_ex)):
            try:
                groups[k].append(text_ex[i+k])
            except IndexError:
                continue

    return groups


# testing
# encrypted = vig_encrypt(key_to_nums('да'), 'привет')
# print(encrypted)
# print(vig_encrypt([-5, -1], encrypted))

########
# 1, 2

# print('Open text:')
# print(text)
# # print()
# print(f"Index: {index(text)}")
# print()
#
# for k in keys:
#     print(f"Encrypted text with key '{k}':")
#     enc = vig_encrypt(key_to_nums(k), text)
#     print(enc)
#     # print()
#     print(f"Index: {index(enc)}")
#     print()

########


# print(tm.get_frequency("letters_frequency_without_spaces.csv"))

# freqs_sqs = [float(i)**2 for i in tm.get_frequency("letters_frequency_without_spaces.csv").values()]
# MI = sum(freqs_sqs)
# print(MI) # 0.05593598260963655




