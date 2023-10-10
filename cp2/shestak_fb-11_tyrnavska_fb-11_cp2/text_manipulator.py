import re


# function for formatting text without spaces
def cleaning_without_spaces(path):
    with open(path, 'r', encoding="UTF-8") as reader:
        cleaned_text = re.sub(r'[^а-яА-ЯёЁ]', '', reader.read()).replace('\n', '').replace('ё', 'е').replace('Ё', 'Е').lower()
        return cleaned_text


# funtion for creating valid text without spaces
def creating_valid_text_without_spaces(input_path, output_path):
    with open(output_path, 'w', encoding="UTF-8") as writer:
        writer.write(cleaning_without_spaces(input_path))


# function for returning valid text as string
def get_text(path):
    with open(path, 'r', encoding="UTF-8") as reader:
        return reader.read()


if __name__ == '__main__':
    # creating valid text examples
    # valid text without spaces
    creating_valid_text_without_spaces('text.txt', 'valid_text_without_spaces.txt')
