from re import sub

path = "clean_text.txt"

def clean_text(filepath):
    text = read_text(filepath)
    text = text.lower()
    text = sub("[^а-яё ]", " ", text)
    text = sub("\s+", " ", text)
    return text

def text_without_spaces(filepath):
    text = read_text(filepath)
    text = sub("\s", "", text)
    return text


def save_text(filepath, text):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

def read_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def count_letters(filepath):    # Підрахунок символів у тексті
    letter_dict = {}
    text = read_text(filepath)
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def count_letter_frequency(filepath):    # Підрахунок частоти символів
    letter_dict = count_letters(filepath)
    total_count = sum(letter_dict.values())   # Повна кількість символів
    letter_frequency = {letter: count / total_count for letter, count in letter_dict.items()}
    return letter_frequency

def count_letter_frequency_without_spaces(filepath):  # Підрахунок частоти символів без пробілів
    letter_dict = count_letters(filepath)
    spaces_count = letter_dict.get(' ')
    total_count_no_spaces = sum(letter_dict.values()) - spaces_count
    del letter_dict[' ']
    letters_frequency_without_spaces = {letter: count / total_count_no_spaces for letter, count in letter_dict.items()}
    return letters_frequency_without_spaces

def count_bigrams(filepath, step=1):    # Підрахунок біграм з різним кроком
    text = read_text(filepath)
    bigram_dict = {}
    for i in range(0, len(text) - 1, step):
        bigram = text[i:i+2]
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    bigram_dict = dict(sorted(bigram_dict.items(), key=lambda x: x[1], reverse=True))  # Сортування за значеннями ключів
    return bigram_dict

def count_bigram_frequency(filepath, step=1):    # Частота біграм з пробілами з різним кроком
    bigram_dict = count_bigrams(filepath, step)
    total_count = sum(bigram_dict.values())
    bigram_frequency = {bigram: count / total_count for bigram, count in bigram_dict.items()}
    return bigram_frequency

def count_bigram_frequency_without_spaces(filepath, step=1):   # Частота біграм без пробілів з різним кроком
    text = text_without_spaces(filepath)
    bigram_dict = {}
    for i in range(0, len(text) - 1, step):
        bigram = text[i:i + 2]
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    bigram_dict = dict(sorted(bigram_dict.items(), key=lambda x: x[1], reverse=True))
    total_count = sum(bigram_dict.values())
    bigram_frequency = {bigram: count / total_count for bigram, count in bigram_dict.items()}
    return bigram_frequency

def output_list(frequency: dict):
    text = ""
    for element in frequency:
        print(element, round(frequency[element], 5))
        text += f"{element},{round(frequency[element], 5)}\n"
    save_text("list.csv", text)



if __name__ == "__main__":
    print(count_bigram_frequency(path))
    output_list(count_letter_frequency(path))