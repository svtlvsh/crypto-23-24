import math

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet_len = len(alphabet)
alphabet_set = {i:alphabet[i] for i in range(alphabet_len)}
file = "text.txt"

print("Alphabet: ", alphabet, "\nLength: ", alphabet_len)

def read_text_from_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        text = file.read()
    return text.strip()

def char_frequency(text):
    # Initialize a dictionary to store character frequencies
    dict_with_frequency = {}
    for char in alphabet:
        dict_with_frequency[char] = 0

    # Count the frequencies of characters in the text
    for item in text:
        if item in dict_with_frequency:
            dict_with_frequency[item] += 1
    # Calculate and print normalized character frequencies
    for char in alphabet:
        dict_with_frequency[char] = dict_with_frequency[char] / len(text)
    return dict_with_frequency 

def entropy(dict_with_frequency):   
    entropy_list = []
    for i in dict_with_frequency.values():
        if i != 0:
         entropy_list.append(-(i * math.log2(i)))
        else:
            entropy_list.append(0)
            
    for j in dict_with_frequency.keys():
        # if len(j) > 1:   
        #     entropy = 0.5 * sum(entropy_list)
        # else:
            entropy = sum(entropy_list)
    print(f"Entropy: {entropy}")
    return entropy

def detect_key_length():
    text = read_text_from_file(file)
    def temp(text):      
        dict_with_frequency = char_frequency(text)
        entropy(dict_with_frequency)
        sorted_dict_with_frequency = dict(sorted(dict_with_frequency.items(), reverse=True, key= lambda item:item[1]))
        print(sorted_dict_with_frequency)

    for i in range(1,10):
        print(f"\nEach {i} char analysys:\n")
        temp(text[::i])

# detect_key_length()
# detected key length for variant 14 key_length=8

key_length = 8 





# def write_text_to_file(file_path, text, mode='w'):
#     with open(file_path, mode) as file:
#         file.write(text)
# write_text_to_file(file, text.replace("\n",''))