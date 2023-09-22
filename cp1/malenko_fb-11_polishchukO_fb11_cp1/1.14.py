import math

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчъыьэюя'

class Lab1Text:

    def __init__(self, text, spaces=True):
        self.alphabet = ALPHABET+' ' if spaces else ALPHABET
        self.spaces = spaces
        self.text = text
        self.text = self.clean_text()

    def clean_text(self):
        text = self.text.lower()
        text = ''.join([char for char in text if char in self.alphabet])
        return text

    def get_frequency(self, length, distance=1):
        frequencies = {}
        ngrams_count = 0
        for i in range(0, len(self.text)-length+1, distance):
            ngram = self.text[i:i+length]
            ngrams_count += 1
            if ngram in frequencies:
                frequencies[ngram] += 1
            else:
                frequencies[ngram] = 1
        normalized_frequencies = {ngram: frequency/ngrams_count for ngram, frequency in frequencies.items()}
        print(dict(sorted(normalized_frequencies.items(), key=lambda item: item[1], reverse=True)[:10]))
        # print(sum(normalized_frequencies.values()))
        return normalized_frequencies

    def get_entropy(self, length, distance=1):
        entropy = 0
        frequencies = self.get_frequency(length, distance=distance)
        for frequency in frequencies.values():
            if not frequency:
                continue
            entropy -= frequency * math.log2(frequency)
        normalized_entropy = entropy / length
        return normalized_entropy

    def get_redundancy(self, length, distance=1):
        entropy = self.get_entropy(length, distance=distance)
        redundancy = 1 - (entropy / math.log2(len(self.alphabet)))
        return redundancy

with open('input.txt', 'r', encoding='utf8') as f:
    inputText = f.read()

textWithSpaces = Lab1Text(inputText, spaces=True)
h1WithSpaces = textWithSpaces.get_entropy(1, 1)
h2Step1WithSpaces = textWithSpaces.get_entropy(2, 1)
h2Step2WithSpaces = textWithSpaces.get_entropy(2, 2)
r1WithSpaces = textWithSpaces.get_redundancy(1, 1)
r2Step1WithSpaces = textWithSpaces.get_redundancy(2, 1)
r2Step2WithSpaces = textWithSpaces.get_redundancy(2, 2)
print(f'Entropy for symbols with whitespaces = {h1WithSpaces}\n'
      f'Entropy for bigrams (step 1) with whitespaces = {h2Step1WithSpaces}\n'
      f'Entropy for bigrams (Step 2) with whitespaces = {h2Step2WithSpaces}\n'
      f'Redundancy for symbols with whitespaces = {r1WithSpaces}\n'
      f'Redundancy for bigrams (step 1) with whitespaces = {r2Step1WithSpaces}\n'
      f'Redundancy for bigrams (Step 2) with whitespaces = {r2Step2WithSpaces}\n\n')


textNoSpaces = Lab1Text(inputText, spaces=False)
h1NoSpaces = textNoSpaces.get_entropy(1, 1)
h2Step1NoSpaces = textNoSpaces.get_entropy(2, 1)
h2Step2NoSpaces = textNoSpaces.get_entropy(2, 2)
r1NoSpaces = textNoSpaces.get_redundancy(1, 1)
r2Step1NoSpaces = textNoSpaces.get_redundancy(2, 1)
r2Step2NoSpaces = textNoSpaces.get_redundancy(2, 2)
print(f'Entropy for symbols without whitespaces = {h1NoSpaces}\n'
      f'Entropy for bigrams (step 1) without whitespaces = {h2Step1NoSpaces}\n'
      f'Entropy for bigrams (Step 2) without whitespaces = {h2Step2NoSpaces}\n'
      f'Redundancy for symbols without whitespaces = {r1NoSpaces}\n'
      f'Redundancy for bigrams (step 1) without whitespaces = {r2Step1NoSpaces}\n'
      f'Redundancy for bigrams (Step 2) without whitespaces = {r2Step2NoSpaces}\n\n')
