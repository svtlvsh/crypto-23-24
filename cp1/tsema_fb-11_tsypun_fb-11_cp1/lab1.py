from math import log2

alpha = "абвгдежзийклмнопрстуфхцчшщыьэюя"


def freq_count(text: str, n: int, ngr_intercept=False) -> dict[str, float]:
    step = 1 if ngr_intercept else n
    ngr_dict = {}
    
    for i in range(0, len(text) - n, step):
        if not text[i: i + n]:
            continue

        if text[i: i + n] not in ngr_dict.keys():
            ngr_dict.update({text[i: i + n]: 1})
        else:
            ngr_dict[text[i: i + n]] += 1

    return {i: ngr_dict[i] / sum(ngr_dict.values()) for i in sorted(ngr_dict.keys())}


def text_purification(fLine: str, isnlp=False, save_space=False) -> (bool, str):
    isSpacePresent = False
    isNewLineCPresent = isnlp
    isBegining = True

    substitutions = {"ъ": "ь", "ё": "е"}
    output = ""
    for s in fLine:
        if s == " " and not isSpacePresent and not isBegining:
            isSpacePresent = True
            if save_space:
                output += s
            continue

        if s == '\n' and not isNewLineCPresent:
            isNewLineCPresent = True
            if save_space and not isSpacePresent:
                output += " "
                isSpacePresent = True
            continue

        if s in substitutions.keys():
            output += substitutions[s]

        elif s.lower() in alpha:
            output += s.lower()

        isSpacePresent = False
        isNewLineCPresent = False
        isBegining = False
    
    return isNewLineCPresent, output


def compute_entropy(n: int, freq_dict: dict):
    entropy = 0
    for freq in freq_dict.values():
        entropy -= freq * log2(freq)

    return entropy / n


def fLine_gen(fPath: str):
    with open(fPath, "r", encoding="utf8") as hFile:
        while fLine := hFile.readline():
            yield fLine


if __name__ == "__main__":
    # with open("purified_text_w_s.txt", "w", encoding="utf8") as hFile:
    #     isnlp = False
    #     for fLine in fLine_gen("lab_text.txt"):
    #         isnlp, pur_line = text_purification(fLine, isnlp, True)
    #         hFile.writelines(pur_line)
    #         print(pur_line)

    # hFile.close()

    # with open("purified_text_w_null.txt", "w", encoding="utf8") as hFile:
    #     isnlp = False
    #     for fLine in fLine_gen("lab_text.txt"):
    #         isnlp, pur_line = text_purification(fLine, isnlp)
    #         hFile.writelines(pur_line)
    #         print(pur_line)

    # hFile.close()

    with open("purified_text_w_s.txt", "r", encoding="utf8") as hFile:
        text = hFile.read()

    hFile.close()

    bigr_wo_int_dict = freq_count(text, 2)          # w/o ngram interceptions
    bigr_w_int_dict = freq_count(text, 2, True)     # w ngram interceptions
    onegr_wo_int_dict = freq_count(text, 1)         # w/o ngram interceptions
    onegr_w_int_dict = freq_count(text, 1, True)    # w ngram interceptions

    print(bigr_wo_int_dict)
    print(bigr_w_int_dict)
    print(onegr_wo_int_dict)
    print(onegr_w_int_dict)

    print(compute_entropy(2, bigr_w_int_dict),
          compute_entropy(2, bigr_wo_int_dict), '\n', 
          compute_entropy(1, onegr_w_int_dict), 
          compute_entropy(1, onegr_wo_int_dict))