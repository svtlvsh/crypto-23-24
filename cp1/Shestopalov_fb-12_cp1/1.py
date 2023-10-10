import math

def calculate_r(entropy):
    r=1-entropy/math.log2(34)
    return r

def calculate_r1(entropy):
    r=1-entropy/math.log2(33)
    return r

def count_letter_frequency(text):
    text = ''.join([char.lower() for char in text if char.isalpha() or char.isspace()])
    letter_frequency = {}
    for char in text:
        if char in letter_frequency:
            letter_frequency[char] += 1
        else:
            letter_frequency[char] = 1
    return letter_frequency

def count_bigram_frequency(text):
    text = ''.join([char.lower() for char in text if char.isalpha() or char.isspace()])
    bigram_frequency = {}
    for i in range(len(text) - 1):
        bigram = text[i:i + 2]
        if bigram in bigram_frequency:
            bigram_frequency[bigram] += 1
        else:
            bigram_frequency[bigram] = 1
    return bigram_frequency

def count_bigram_frequency_without(text):
    text = ''.join([char.lower() for char in text if char.isalpha() or char.isspace()])
    bigram_frequency_witout = {}
    for i in range(0, len(text) - 1, 2):
        bigram = text[i:i + 2]
        if bigram in bigram_frequency_witout:
            bigram_frequency_witout[bigram] += 1
        else:
            bigram_frequency_witout[bigram] = 1
    return bigram_frequency_witout

def calculate_entropy(frequency_dict, text_length):
    entropy = 0.0
    for count in frequency_dict.values():
        probability = count / text_length
        entropy -= probability * math.log2(probability)
    return entropy

def print_frequency_table(frequency_dict, total_count, title):
    print(title)
    print("+---------------+------------+-----------+")
    print("|   Character   |    Count   | Frequency |")
    print("+---------------+------------+-----------+")
    for char, count in sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True):
        frequency = (count / total_count) * 100
        print(f"| {char:<13} | {count:<10} | {frequency:.3f}%    |")
    print("+---------------+------------+-----------+")

if __name__ == "__main__":
    input_file_path = r'C:\Users\Sasha\Desktop\lab1_1.txt'
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    letter_frequency_with_spaces = count_letter_frequency(text)
    bigram_frequency_with_spaces = count_bigram_frequency(text)
    bigram_frequency_with_spaces_without = count_bigram_frequency_without(text)
    text_length_with_spaces = len(text)

    text_without_spaces = text.replace(" ", "")

    letter_frequency_without_spaces = count_letter_frequency(text_without_spaces)
    bigram_frequency_without_spaces = count_bigram_frequency(text_without_spaces)
    bigram_frequency_without_spaces_without = count_bigram_frequency_without(text_without_spaces)
    text_length_without_spaces = len(text_without_spaces)

    entropy_h1_letters_with_spaces = calculate_entropy(letter_frequency_with_spaces, text_length_with_spaces)
    entropy_h1_bigrams_with_spaces = calculate_entropy(bigram_frequency_with_spaces, text_length_with_spaces - 1)
    entropy_h1_bigrams_with_spaces_without = calculate_entropy(bigram_frequency_with_spaces_without, (text_length_without_spaces - 1)//2)

    entropy_h1_letters_without_spaces = calculate_entropy(letter_frequency_without_spaces, text_length_without_spaces)
    entropy_h1_bigrams_without_spaces = calculate_entropy(bigram_frequency_without_spaces, text_length_without_spaces - 1)
    entropy_h1_bigrams_without_spaces_without = calculate_entropy(bigram_frequency_without_spaces_without, (text_length_without_spaces - 1)//2)

    print("Ентропія H1 для літер (з пробілами):", entropy_h1_letters_with_spaces)
    print("Ентропія H1 для літер (без пробілів):", entropy_h1_letters_without_spaces)
    print("Ентропія H2 для біграм (з пробілами, з перетинами):", 0.5*entropy_h1_bigrams_with_spaces)
    print("Ентропія H2 для біграм (без пробілів, з перетинами):", 0.5*entropy_h1_bigrams_without_spaces)
    print("Ентропія H2 для біграм (з пробілами, без перетинів):", 0.5*entropy_h1_bigrams_with_spaces_without)
    print("Ентропія H2 для біграм (без пробілів, без перетинів):", 0.5*entropy_h1_bigrams_without_spaces_without)
    print("Надлишковість для літер (з пробілами):", calculate_r(entropy_h1_letters_with_spaces))
    print("Надлишковість для літер (без пробілів):", calculate_r(entropy_h1_letters_without_spaces))
    print("Надлишковість для біграм (з пробілами, з перетинами):", calculate_r1(0.5 * entropy_h1_bigrams_with_spaces))
    print("Надлишковість для біграм (без пробілів, з перетинами):", calculate_r1(0.5 * entropy_h1_bigrams_without_spaces))
    print("Надлишковість для біграм (з пробілами, без перетинів):", calculate_r1(0.5 * entropy_h1_bigrams_with_spaces_without))
    print("Надлишковість для біграм (без пробілів, без перетинів):", calculate_r1(0.5 * entropy_h1_bigrams_without_spaces_without))

    print("\n")
    print_frequency_table(letter_frequency_with_spaces, text_length_with_spaces, "Частота літер (з пробілами):")
    print_frequency_table(bigram_frequency_with_spaces, text_length_with_spaces - 1, "Частота біграм:")
    print("\n")
