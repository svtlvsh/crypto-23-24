import text_manipulator as tm
from collections import defaultdict, Counter


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


def separator(text_ex, key_len):
    groups = [[] for _ in range(key_len)]

    for i in range(0, len(text_ex), key_len):
        for k in range(key_len):
            try:
                groups[k].append(text_ex[i+k])
            except IndexError:
                continue

    unic_groups = [{i for i in g} for g in groups]

    return groups, unic_groups


def indexes(separated):
    groups, unic_groups = separated
    # print(groups, unic_groups)
    all_indexes = []
    for i in range(len(groups)):
        first_part = 1 / (len(groups[i]) * (len(groups[i]) - 1))
        second_part = [groups[i].count(x)*(groups[i].count(x)-1) for x in unic_groups[i]]
        # print(second_part)
        second_part = sum(second_part)
        # print(first_part, second_part)
        all_indexes.append(first_part * second_part)

    mean_index = sum(all_indexes) / len(all_indexes)

    return mean_index


def approx_equal(x, y, epsilon=0.001):
    return abs(x - y) < epsilon


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

freqs_sqs = [float(i)**2 for i in tm.get_frequency("letters_frequency_without_spaces.csv").values()]
MI = sum(freqs_sqs)  # 0.05593598260963655
# print(MI)


########
# 3

encrypted_text = tm.get_text("encrypted_var1.txt")
# print(encrypted_text)

I = 0
r = 1

# for i in range(2, 100):
#     print(indexes(separator(encrypted_text, i)))

while not approx_equal(0.0553, I):
    r += 1
    I = indexes(separator(encrypted_text, r))

print("r =", r)

groups = separator(encrypted_text, r)[0]
most_fr_letter = [l for l in tm.get_frequency("letters_frequency_without_spaces.csv").keys()]

# print(Counter(groups[0]))

# fin_key1 = ''
# fin_key2 = ''
# fin_key3 = ''

def get_fin_keys(n):
    fin_key = ''
    for i in groups:
        counter = Counter(i)
        # print(counter)
        most_fr_letter_in_group = counter.most_common(1)[0][0]
        pos = ord(most_fr_letter_in_group) - ord(most_fr_letter[n])
        # print(most_fr_letter_in_group, most_fr_letter[n])
        # print(pos)
        if pos >= 0:
            fin_key += chr(pos + 1072)
        else:
            fin_key += chr(1103 + pos)

    return fin_key


print(get_fin_keys(0))
# print(get_fin_keys(1))
# print(get_fin_keys(2))



# for i in groups:
#     counter = Counter(i)
#     print(counter)
#     most_fr_letter_in_group = counter.most_common(1)[0][0]
#     pos = ord(most_fr_letter_in_group) - ord(most_fr_letter[n])
#     print(most_fr_letter_in_group, most_fr_letter[n])
#     print(pos)
#     if pos >= 0:
#         fin_key += chr(pos + 1072)
#     else:
#         fin_key += chr(1103 + pos)

# print(fin_key)
# print(ord('ї'))


print(vig_encrypt([-x for x in key_to_nums('вчебспирбтрю')], encrypted_text))





