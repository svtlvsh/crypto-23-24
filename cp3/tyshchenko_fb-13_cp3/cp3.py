#!/bin/python3

from collections import Counter
import sys

ALPHABET = "абвгдежзийклмнопрстуфхцчшщыьэюя"
M = len(ALPHABET)
BIGRAMS = ["ст", "но", "то", "на", "ен"]

# Calculate gcd(a, b).
def euclid(a: int, b: int) -> list:
    assert a >= b, "a should not be less than b"
    # Initialize base values.
    r = a % b
    u = [1, 0]
    v = [0, 1]
    q = [a // b]
    # Find gcd(a, b) and inverses.
    while a % b:
        a = b
        b = r
        r = a % b
        u.append(u[-2] - q[-1] * u[-1])
        v.append(v[-2] - q[-1] * v[-1])
        q.append(a // b)
    # Return [gcd(a, b), a^(-1), b^(-1)].
    return [b, u[-1], v[-1]]

# Solve a * x = b mod n.
def lin_cmp(a: int, b: int, n: int):
    lst = euclid(n, a)
    # Case gcd(a, n) == 1.
    if lst[0] == 1:
        return (lst[2] * b) % n
    # Case gcd(a, n) = d > 1 and b % d != 0.
    if b % lst[0] != 0:
        #print("Case gcd(a, n) = d > 1 and b % d != 0.")
        return 0
    # Case gcd(a, n) = d > 1 and b % d == 0. 
    else:
        a //= lst[0]
        b //= lst[0]
        n //= lst[0]
        x = (euclid(n, a)[2] * b) % n
        #print("Case gcd(a, n) = d > 1 and b % d == 0.")
        return [x + i * n for i in range(lst[0])]

# Count bigrams of a text.
def count_bigrams(text: str, overlap=False) -> dict:
    text_len = len(text)
    if overlap:
        step = 1
    else:
        step = 2
    bigrams = [text[s:s + 2] for s in range(0, text_len - 1, step)]
    bigram_count = dict(sorted(Counter(bigrams).items(), reverse=True, key=lambda item: item[1]))
    return bigram_count

# Encode bigram.
def encode(bigram: str) -> int:
    encoded = ALPHABET.index(bigram[0]) * M + ALPHABET.index(bigram[1])
    return encoded

# Decode bigram.
def decode(codes) -> str:
    second = codes % M
    first = codes // M
    return f"{ALPHABET[first]}{ALPHABET[second]}"

# Find candidates for keys.
def find_keys(ct: str) -> list:
    keys = []
    ct_bigrams = list(count_bigrams(ct))
    # CORNER CASE "1-1 2-2"
    # Solve (X* - X**)a = (Y* - Y**) mod m^2.
    a = lin_cmp(BIGRAMS[0] - BIGRAMS[1], ct_bigrams[0] - ct_bigrams[1], M ** 2)
    for i in a:
        b = (ct_bigrams[0] - i * BIGRAMS[0]) % M ** 2
        keys.append((i, b))
    return keys

# Check if deciphered PT is sensible.
def sensible(pt: str) -> int:
    score = 0
    # COUNT LETTERS (most and least frequent)
    bigrams = list(count_bigrams(ct, overlap=True))
    for i in range(5):
        if bigrams[i] == BIGRAMS[i]:
            score += 1
    return score 

# TESTS
# Find inverse.
print(euclid(155, 29))
# Solve linear comparison (case 1).
print(lin_cmp(7, 19, 41))
# Solve linear comparison (case 3).
print(lin_cmp(39, 30, 111))
# Count bigrams of "hello world!" without and with overlap.
print(count_bigrams("hello world! hello mum"))
print(count_bigrams("hello world! hello mum", overlap=True))
# Encode and decode bigram.
print(f"{decode(63)} ({encode('вб')})")
