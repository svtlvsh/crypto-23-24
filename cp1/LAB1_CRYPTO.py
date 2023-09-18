


with open('Text.txt', 'r') as file:
    # Read the entire file content into a string
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

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
global_letter_count = 0
for char in file_contents:
    # Check if the current character is an alphabetic character
    if char.isalpha():
        global_letter_count += 1



for letter in letters:
    letter_count = file_contents.count(letter)
    letter_frequency = round(letter_count/global_letter_count, 4)
    print(f"Букви '{letter}': {letter_frequency}")


bigrams = [letters[i] + letters[j] for i in range(len(letters)) for j in range(len(letters))]

global_bigram_count = 0
for bigram in bigrams:
    bigram_count = file_contents.count(bigram)
    global_bigram_count += bigram_count

for bigram in bigrams:
    bigram_count = file_contents.count(bigram)
    if bigram_count > 0:  # Check if bigram_count is greater than zero
        bigram_frequency = bigram_count / global_bigram_count
        print(f"Біграмма '{bigram}': {bigram_frequency}")





