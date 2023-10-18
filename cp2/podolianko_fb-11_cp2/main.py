import json
from typing import Dict, Tuple, List

import vigenere
import utils
from utils import index_of_coincidence
from consts import *
from vigenere import *


def main():
    with open('./data/sample_for_encryption_norm.txt', 'rt', encoding='utf-8') as file:
        text = file.read()

    average_ioc = index_of_coincidence(text)  # todo use longer text
    print(f'IOC of a sample natural text: {average_ioc}')
    print(f"IOC of the chosen clear text: {index_of_coincidence(text):e}")
    print(f'Even alphabet IOC: {IOC_RANDOM:e}')
    print()

    encrypted_texts = []
    for key in [KEY_2, KEY_3, KEY_4, KEY_5, KEY_15]:
        encrypted_texts.append(
            encrypt(text,
                    utils.normalize_string(key, ALPHABET, TRANSLATOR),
                    ALPHABET)
        )
        print(f"IOC of sample text encrypted with key '{key}': {index_of_coincidence(encrypted_texts[-1]):e}")

        print(key, encrypted_texts[-1])
        print(f'Guessed key: {utils.guess_key_len_1(encrypted_texts[-1], IOC_RANDOM, average_ioc)}')

        print()

    with open('./data/task.txt', 'rt', encoding='utf-8') as file:
        task = file.read()

    task_norm = utils.normalize_string(task, ALPHABET, TRANSLATOR)
    with open('./data/letters_whitespaces_False.json', 'rt') as file:
        letter_freq = json.load(file)

    letter_freq = list(letter_freq.items())

    # with open('./data/sample_big_norm.txt', 'rt', encoding='utf-8') as file:
    #     letter_freq = utils.letter_freq(file.read())

    guessed_length = utils.guess_key_len_1(task_norm, IOC_RANDOM, average_ioc, 30)
    print(f'Guessing key length: {guessed_length}')
    print("Will now let user interactively adjust the key [n - exit, r - reset adjustments]")
    # an adjustments means to take the next nth most frequent alphabet letter
    # and calculate the key from this letter and most frequent cyphertext letter in the block
    adjustments = {i: 0 for i in range(guessed_length)}
    while True:
        key = guess_vigenere_key(task_norm, guessed_length, letter_freq, adjustments=adjustments)
        print(f"Guessed key: {key}")
        print(f'Already adjusted: {adjustments}')
        print(' '.join(decrypt(task, key, ALPHABET)[i:i + guessed_length] for i in range(0, len(task), guessed_length)))
        # print(decrypt(task, key, ALPHABET))
        adjust_index = input('Which key index to adjust? ')
        try:
            adjust_index = int(adjust_index) % guessed_length
            adjustments[adjust_index] += 1
        except ValueError:
            match adjust_index:
                case 'n':
                    break
                case 'r':
                    print("Resetting adjustments...\n")
                    adjustments = {i: 0 for i in range(guessed_length)}
                case _:
                    print("Wrong input")

    print('Decrypted text:')
    print(decrypt(task, key, ALPHABET))


def guess_vigenere_key(ct: str, key_len: int, sample_frequencies: List[Tuple[str, float]],
                       adjustments: Dict[int, int]) -> str:
    blocks = list(map(lambda x: ''.join(x), utils.split_as_caesar_blocks(ct, key_len)))
    sorted_sample_letter_f: List[Tuple[str, float]] = sorted(sample_frequencies, key=lambda x: x[1], reverse=True)
    key = [''] * key_len

    for i in range(key_len):
        nth_most_frequent_letter_i = utils.to_indexes(sorted_sample_letter_f[adjustments[i]][0], ALPHABET)[0]
        most_frequent_ct_letter = sorted(utils.letter_freq(blocks[i]), key=lambda x: x[1], reverse=True)[0][0]
        most_frequent_ct_letter_i = utils.to_indexes(most_frequent_ct_letter, ALPHABET)[0]
        key[i] = utils.from_indexes([(most_frequent_ct_letter_i - nth_most_frequent_letter_i) % len(ALPHABET)],
                                    ALPHABET)

    return ''.join(key)


if __name__ == '__main__':
    main()
