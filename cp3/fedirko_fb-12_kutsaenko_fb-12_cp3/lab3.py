most_popular_bigrams = ["ст", "но", "то", "на", "ен"]
alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"

def GCD(a,b):
    if b == 0:
        return a, 1, 0
    d, x, y = GCD(b, a % b)
    return d, y, x - (a // b) * y

result = GCD(144, 120)
print("НСД: ", result[0])
print("Коефіцієнти x, y: ", result[1], result[2])

def mod_inv(a, m):
    gcd, x, y = GCD(a, m)
    if gcd != 1:
        raise ValueError(f"Не існує оберненого")
    else:
        return x % m

def solve_linear_congruence(a, b, m):
    gcd, x, y = GCD(a, m)
    if b % gcd == 0:
        x0 = (x * (b // gcd)) % m
        solutions = [(x0 + k * (m // gcd)) % m for k in range(gcd)]
        return solutions
    else:
        return []

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        text = file.read()
    return text

def bigram_frequencies(text):
    bigrams = [text[i:i+2] for i in range(0, len(text) - 1, 2)]
    return bigrams

def calculate_bigram_frequencies(text):
    bigrams = [text[i:i+2] for i in range(0, len(text) - 1, 2)]
    return Counter(bigrams)


def find_most_frequent_bigrams(text, n):
    frequencies = calculate_bigram_frequencies(text)
    most_common_bigrams = frequencies.most_common(n)
    result = [[bigram[0][0], bigram[0][1]] for bigram in most_common_bigrams]
    return result

def bichar_to_number(bigram):
    alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
    
    x, y = bigram
    num_x = alphabet.index(x)
    num_y = alphabet.index(y)
    #print(num_x, num_y)
    
    m = len(alphabet)
    #print(m)
    result = num_x * m + num_y
    
    return result

def bigrams_to_numbers(bigrams):
    result = [bichar_to_number(bigram) for bigram in bigrams]
    return result

def number_to_bichar(number):
    alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
    m = len(alphabet)
    
    num_x = number // m
    num_y = number % m
    
    char_x = alphabet[num_x]
    char_y = alphabet[num_y]
    
    return char_x + char_y

def numbers_to_bigrams(numbers):
    result = ''.join([''.join(number_to_bichar(number)) for number in numbers])
    return result
