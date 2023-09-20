import math
import re
from collections import Counter
import pandas as pd

def text_editing(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read()
        for letter in content:
            content = content.replace(letter, letter.lower())
        content = content.replace('ъ', 'ь')
        content = content.replace('ё', 'е') 
        content = re.sub(r'[.,(){}\[\]\'"!?*-<>—:;\d`/\\enxiva\s]+', ' ', content)
    with open('cp1_edited.txt', 'w', encoding='utf8') as file:
        file.write(content)
    return content

def no_whitespaces(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read()
        content = content.replace(' ', '')
    with open('cp1_without_whitespaces.txt', 'w', encoding='utf8') as file:
        file.write(content)
    return content

def frequency_letter(text):
    letters = Counter(text)
    freq_letter = {num: letters[num] / sum(letters.values()) for num in letters.keys()}

    df = pd.DataFrame(list(freq_letter.items()), columns=['Літера', 'Частота'])
    df = df.sort_values(by=['Частота'], ascending=False)
    if ' ' in df['Літера'].values:
        df.to_csv('frequency_letter_whitespaces.csv')
    else:
        df.to_csv('frequency_letter_no_whitespaces.csv')        
    return freq_letter

def frequency_bigram(text, step_num):
    bigrams = {}
    for i in range(len(text) - step_num):
        bigram = text[i] + text[i + step_num]
        if bigram in bigrams:
            continue
        else:
            bigrams[bigram] = text.count(bigram)
            
    freq_bigram = {num: bigrams[num] / sum(bigrams.values()) for num in bigrams.keys()}
    
    df = pd.DataFrame(list(freq_bigram.items()), columns=['Біграма', 'Частота'])
    df = df.sort_values(by=['Частота'], ascending=False)
    for b in df['Біграма'].values:
        if re.search(r'\s', b):
            df.to_csv('frequency_bigram_whitespaces_{}.csv'.format(step_num))
        else:
            df.to_csv('frequency_bigram_no_whitespaces_{}.csv'.format(step_num))
    return freq_bigram

def entropy(frequency):   
    entropy = []
    for i in frequency.values():
        if i != 0:
         entropy.append(-(i * math.log2(i)))
        else:
            entropy.append(0)
            
    for j in frequency.keys():
        if len(j) > 1:   
            entropy_num = 0.5 * sum(entropy)
        else:
            entropy_num = sum(entropy)
    return entropy_num

def redundancy(entropy, alphabet_num):
    redundancy = 1 - (entropy / math.log2(alphabet_num))
    return redundancy

filename_original = 'cp1_text.txt'
filename_edited = 'cp1_edited.txt'

text_with_whitespaces = text_editing(filename_original)
text_without_whitespaces = no_whitespaces(filename_edited)

h1_with_whitespaces = entropy(frequency_letter(text_with_whitespaces))
h1_without_whitespaces = entropy(frequency_letter(text_without_whitespaces))
h2_step1_with_whitespaces = entropy(frequency_bigram(text_with_whitespaces, 1))
h2_step1_without_whitespaces = entropy(frequency_bigram(text_without_whitespaces, 1))
h2_step2_with_whitespaces = entropy(frequency_bigram(text_with_whitespaces, 2))
h2_step2_without_whitespaces = entropy(frequency_bigram(text_without_whitespaces, 2))

r1_with_whitespaces = redundancy(h1_with_whitespaces, 32)
r1_without_whitespaces = redundancy(h1_without_whitespaces, 31)
r2_step1_with_whitespaces = redundancy(h2_step1_with_whitespaces, 32)
r2_step1_without_whitespaces = redundancy(h2_step1_without_whitespaces, 31)
r2_step2_with_whitespaces = redundancy(h2_step2_with_whitespaces, 32)
r2_step2_without_whitespaces = redundancy(h2_step2_without_whitespaces, 31)

print(f'--- Ентропія для літер з пробілом: {h1_with_whitespaces}',
      f'    Ентропія для літер без пробілу: {h1_without_whitespaces}',
      f'    Ентропія для біграм, які перетинаються, з пробілом: {h2_step1_with_whitespaces}',
      f'    Ентропія для біграм, які перетинаються, без пробілу: {h2_step1_without_whitespaces}',
      f'    Ентропія для біграм, які не перетинаються, з пробілом: {h2_step2_with_whitespaces}',
      f'    Ентропія для біграм, які не перетинаються, без пробілу: {h2_step2_without_whitespaces}')

print(f'--- Надлишковість для літер з пробілом: {r1_with_whitespaces}', 
      f'    Надлишковість для літер без пробілу: {r1_without_whitespaces}', 
      f'    Надлишковість для біграм, які перетинаються, з пробілом: {r2_step1_with_whitespaces}',
      f'    Надлишковість для біграм, які перетинаються, без пробілу: {r2_step1_without_whitespaces}', 
      f'    Надлишковість для біграм, які не перетинаються, з пробілом: {r2_step2_with_whitespaces}',
      f'    Надлишковість для біграм, які не перетинаються, без пробілу: {r2_step2_without_whitespaces}')