import random
from matplotlib import pyplot
from itertools import cycle

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчъыьэюя '
LETTER_TO_INDEX = {letter: index for index, letter in enumerate(ALPHABET)}
SAMPLE_SIZE = 50
RUNS_PER_SAMPLE = 10

class Lab2Text:

    def __init__(self, text):
        self.text = text
        self.text = self.clean_text()

    def clean_text(self):
        text = self.text.lower()
        text = ''.join([char for char in text if char in ALPHABET])
        return text

    def cypher_text(self, key=None):
        if not key:
            return self.text
        cypher = ''
        for textLetter, keyLetter in zip(self.text, cycle(key)):
            textLetterIndex = LETTER_TO_INDEX[textLetter]
            keyLetterIndex = LETTER_TO_INDEX[keyLetter]
            cypherLetterIndex = (textLetterIndex + keyLetterIndex) % len(ALPHABET)
            cypher += ALPHABET[cypherLetterIndex]
        return cypher

def calculate_affinity(text):
    frequencies = {}
    for letter in text:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    affinity = sum(frequency * (frequency - 1) for frequency in frequencies.values()) / (len(text) * (len(text) - 1))
    return affinity

with open('input.txt', 'r', encoding='utf8') as f:
    inputText = f.read()
formattedText = Lab2Text(inputText)

affinities = []
for keyLength in range(20, SAMPLE_SIZE):
    sumAffinity = 0
    for i in range(RUNS_PER_SAMPLE):
        key = ''.join([random.choice(ALPHABET) for letter in range(keyLength)])
        cypherText = formattedText.cypher_text(key=key)
        affinity = calculate_affinity(cypherText)
        sumAffinity += affinity
    averageAffinity = sumAffinity / RUNS_PER_SAMPLE
    affinities.append(averageAffinity)

pyplot.xlabel('Key length')
pyplot.ylabel('Affinity index')
pyplot.plot(affinities)
pyplot.show()