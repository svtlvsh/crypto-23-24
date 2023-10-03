alpha = "абвгдежзийклмнопрстуфхцчшщыьэюя"


def freq_count(fLine: str, n: int, ngr_dict: dict, ngr_intercept=False) -> None:
    for i in range(len(fLine) - n):
        if ngr_intercept:
            if fLine[i: i + n] == n * " ":
                continue

            if fLine[i: i + n] not in ngr_dict.keys():
                ngr_dict.update({fLine[i: i + n]: 1})
            else:
                ngr_dict[fLine[i: i + n]] += 1
        else:
            if fLine[i*n: i*n + n] == n * " ":
                continue

            if fLine[i*n: i*n + n] not in ngr_dict.keys():
                ngr_dict.update({fLine[i*n: i*n + n]: 1})
            else:
                ngr_dict[fLine[i*n: i*n + n]] += 1
            

def text_purification(fLine: str, isnlp=False, save_space=False) -> [bool, str]:
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

            isSpacePresent = False
            isNewLineCPresent = False
            isBegining = False

        elif s.lower() in alpha:
            output += s.lower()

            isSpacePresent = False
            isNewLineCPresent = False
            isBegining = False

    return isNewLineCPresent, output


def fLine_gen(fPath: str) -> str:
    with open(fPath, "r", encoding="utf8") as hFile:
        while fLine := hFile.readline():
            yield fLine


if __name__ == "__main__":
    with open("purified_text_w_s.txt", "w", encoding="utf8") as hFile:
        isnlp = False
        for fLine in fLine_gen("lab_text.txt"):
            isnlp, pur_line = text_purification(fLine, isnlp, True)
            hFile.writelines(pur_line)
            print(pur_line)

    with open("purified_text_w_null.txt", "w", encoding="utf8") as hFile:
        isnlp = False
        for fLine in fLine_gen("lab_text.txt"):
            isnlp, pur_line = text_purification(fLine, isnlp)
            hFile.writelines(pur_line)
            print(pur_line)

    bigr_wo_int_dict = {}
    bigr_w_int_dict = {}
    onegr_wo_int_dict = {}
    onegr_w_int_dict = {}

    for fLine in fLine_gen("purified_text_w_s.txt"):
        freq_count(fLine, 2, bigr_wo_int_dict) # w/o ngram interceptions
        freq_count(fLine, 2, bigr_w_int_dict, True) # w ngram interceptions
        freq_count(fLine, 1, onegr_wo_int_dict) # w/o ngram interceptions
        freq_count(fLine, 1, onegr_w_int_dict, True) # w ngram interceptions


    print(bigr_wo_int_dict)
    print(bigr_w_int_dict)
    print(onegr_wo_int_dict)
    print(onegr_w_int_dict)
