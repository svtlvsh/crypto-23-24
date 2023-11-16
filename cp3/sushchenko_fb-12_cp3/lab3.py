alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
alph_len = len(alphabet)
bigram_top_freq = ["ст", "но", "то", "на", "ен"]


def bigram_freq(text):
    freqs = {}
    for i in range(0, len(text)-1, 2):
        bigram = text[i] + text[i+1]
        if bigram in freqs:
            freqs[bigram] += 1
        else:
            freqs[bigram] = 1

    freqs = dict(sorted(freqs.items(), key=lambda x: x[1], reverse=True))
    return list(freqs.keys())[:5]


def alph_to_num(alph):
    result = []
    for i in alph:
        a = alphabet.index(i[0])
        b = alphabet.index(i[1])
        result.append(a * alph_len + b)
    return result


def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = ext_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def find_keys(X, Y):
    keys = []
    for x1 in X:
        for y1 in Y:
            for x2 in X:
                for y2 in Y:
                    if x1 == x2 or y1 == y2:
                        pass
                    else:
                        gcd, x, y = ext_gcd(x1-x2, alph_len**2)

                        if gcd == 1:
                            a = ((y1-y2)*x) % alph_len**2
                            b = (y1 - a*x1) % alph_len**2
                            keys.append((a, b))
    return keys


def decrypt(text, key):
    result = ""
    bigrams = []
    gcd, a, y = ext_gcd(key[0], alph_len ** 2)

    for i in range(0, len(text)-1, 2):
        bigrams.append(text[i] + text[i+1])
    bigrams = alph_to_num(bigrams)

    for i in bigrams:
        x = (a*(i-key[1])) % alph_len ** 2
        x_i1 = x // 31
        x_i2 = x % 31
        result += alphabet[x_i1]
        result += alphabet[x_i2]

    return result


def find_prop_text(text):
    denied = ["аь", "ьь", "ээ", "юф"]
    for i in denied:
        if i in text:
            return False
    return True


if __name__ == '__main__':
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    bigram_aplh = bigram_freq(text)
    keys = find_keys(alph_to_num(bigram_top_freq), alph_to_num(bigram_aplh))
    for key in keys:
        decrypted_text = decrypt(text, key)
        if find_prop_text(decrypted_text):
            print(decrypted_text)
            print(key)
