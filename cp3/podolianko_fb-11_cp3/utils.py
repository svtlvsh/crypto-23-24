from typing import List, Dict, Tuple
import re
from consts import *


def normalize_string(string: str, alphabet: str, trans) -> str:
    lower_string = string.lower()
    translated_string = lower_string.translate(trans)
    rexp_valid_chars = f'[^{alphabet}]'
    normalized_string = re.sub(rexp_valid_chars, '', translated_string)

    return normalized_string


def ngram_frequencies(text: str, n: int, overlap: bool) -> Dict[str, float]:
    """
    Calculates frequencies for ngrams in the supplied `text`
     * `text` - a String of text
     * `n` - ngram length in characters
     * `overlap` - will calculate frequencies of overlapping ngrams if true, e.g. 'abcd' wil result in ab=1/3, bc=1/3, cd=1/3; otherwise will count only non-overlapping ngrams, e.g. 'abcd' will result in ab=1/2, cd=1/2
    """
    step = n
    if overlap:
        step = 1

    freq_map = dict()
    for i in range(0, len(text) + 1 - n, step):
        ngram = text[i:i + n]
        if ngram in freq_map:
            freq_map[ngram] += 1
        else:
            freq_map[ngram] = 1

    total = sum(freq_map.values())
    for freq in freq_map.keys():
        freq_map[freq] = freq_map[freq] / total

    return freq_map


def to_indexes(text: str, alpha: str) -> List[int]:
    return [alpha.find(t) for t in text]


def from_indexes(i_list: List[int], alpha: str) -> str:
    return ''.join(alpha[i] for i in i_list)


def letter_freq(text: str) -> List[Tuple[str, float]]:
    return [(letter, text.count(letter) / len(text)) for letter in set(text)]


def md_table_rows(rows) -> str:
    return '\n'.join(['|' + '|'.join(map(str, row)) + '|' for row in rows])


def md_table_columns(columns: Tuple[List, List], formats: List[str] | Tuple = '%s') -> str:
    columns = [[format(columns[i][row], formats[i]) for row in range(len(columns[i]))] for i in range(len(columns))]

    return '\n'.join(['|' + '|'.join(row) + '|' for row in zip(*columns)])


def extended_euclid(a: int, b: int) -> Tuple[int, int, int]:
    """returns gcd, u, v"""
    # if a > b or b < 0:
    #     raise ValueError("a < b or a < 0")

    q = list()
    r = [a, b]

    while True:
        gcd = r[1]
        q.append(r[0] // r[1])
        r[0], r[1] = r[1], r[0] - q[-1] * r[1]
        if r[1] == 0:
            break

    u = list((1, 0))
    v = list((0, 1))

    for qi in q[:-1]:
        u.append(u[-2] - qi * u[-1])
        v.append(v[-2] - qi * v[-1])

    # sanity check
    # TODO REMOVE
    assert gcd == a * u[-1] + b * v[-1], "algo broken"

    return gcd, u[-1], v[-1]


def mul_inverse(a, m):
    # TODO reimpl using euclid
    x = m
    y = a % m

    if y == 0:
        raise ValueError("m|a; gcd(a,m) == m != 1")

    q = list()
    r = list((0, 1))

    while x % y != 0:
        q.append(x // y)
        x, y = y, x % y
    else:
        # we get to gcd here
        if y != 1:
            raise ValueError("gcd(a,m) != 1")

    for qi in q:
        r.append(r[1] * (-qi) + r[0])
        r.pop(0)

    return r.pop() % m


def solve_congruence(a, b, m):
    """solves ax == b mod m and returns a list of solutions (if any)"""
    raise NotImplementedError


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        with open(sys.argv[1], 'rt', encoding='utf-8') as file:
            text = file.read()
        print("Normalizing text...")
        try:
            with open(sys.argv[2], 'xt', encoding='utf-8') as file:
                file.write(normalize_string(text, ALPHABET, TRANSLATOR))
        except FileExistsError:
            print('Overwriting existing file')
            with open(sys.argv[2], 'wt', encoding='utf-8') as file:
                file.write(normalize_string(text, ALPHABET, TRANSLATOR))
    else:
        print('arguments: from to')
        exit(1)
