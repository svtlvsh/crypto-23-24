from math import log2

alpha = "абвгдежзийклмнопрстуфхцчшщыьэюя"


def freq_count(fLine: str, n: int, ngr_dict: dict, ngr_intercept=False) -> None:
    step = 1 if ngr_intercept else n
    
    for i in range(0, len(fLine) - n, step):
        if not fLine[i: i + n]:
            continue

        if fLine[i: i + n] not in ngr_dict.keys():
            ngr_dict.update({fLine[i: i + n]: 1})
        else:
            ngr_dict[fLine[i: i + n]] += 1

    ngr_dict = {i: ngr_dict[i] for i in sorted(ngr_dict.keys())}


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
    ngr_count = sum(freq_dict.values())
    entropy = 0
    for freq in freq_dict.values():
        entropy -= (freq / ngr_count) * log2(freq / ngr_count)

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

    # with open("purified_text_w_null.txt", "w", encoding="utf8") as hFile:
    #     isnlp = False
    #     for fLine in fLine_gen("lab_text.txt"):
    #         isnlp, pur_line = text_purification(fLine, isnlp)
    #         hFile.writelines(pur_line)
    #         print(pur_line)

    bigr_wo_int_dict = {}
    bigr_w_int_dict = {}
    onegr_wo_int_dict = {}
    onegr_w_int_dict = {}

    for fLine in fLine_gen("purified_text_w_s.txt"):
        freq_count(fLine, 2, bigr_wo_int_dict) # w/o ngram interceptions
        freq_count(fLine, 2, bigr_w_int_dict, True) # w ngram interceptions
        freq_count(fLine, 1, onegr_wo_int_dict) # w/o ngram interceptions
        freq_count(fLine, 1, onegr_w_int_dict, True) # w ngram interceptions

    print(compute_entropy(2, bigr_w_int_dict),
          compute_entropy(2, bigr_wo_int_dict), '\n', 
          compute_entropy(1, onegr_w_int_dict), 
          compute_entropy(1, onegr_wo_int_dict))
