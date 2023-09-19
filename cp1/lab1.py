import re

def filter():
    with open("1.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    # Робимо всі букви маденькими
    text = text.lower()

    # Прибираєм все, що не входить в російський алфавіт, лишаєм пробіли
    text = re.sub(r'[^\sа-яё]', '', text)

    # Прибираємо подвійні пробіли, або всі пробіли
    text = re.sub(r'\s+', ' ', text)

    with open("2.txt", 'w', encoding='utf-8') as file:
        file.write(text)

filter()