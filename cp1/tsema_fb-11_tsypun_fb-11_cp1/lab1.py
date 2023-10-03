import math


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

            isSpacePresent = False
            isNewLineCPresent = False
            isBegining = False

        elif s.lower() in alpha:
            output += s.lower()

            isSpacePresent = False
            isNewLineCPresent = False
            isBegining = False

    return isNewLineCPresent, output


# def compute_entropy():


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

    bigr_wo_int_dict = {i: bigr_wo_int_dict[i] for i in sorted(bigr_wo_int_dict.keys())}
    bigr_w_int_dict = {i: bigr_w_int_dict[i] for i in sorted(bigr_w_int_dict.keys())}
    onegr_wo_int_dict = {i: onegr_wo_int_dict[i] for i in sorted(onegr_wo_int_dict.keys())}
    onegr_w_int_dict = {i: onegr_w_int_dict[i] for i in sorted(onegr_w_int_dict.keys())}

    print(bigr_wo_int_dict)
    print(bigr_w_int_dict)

    ent_2_1, ent_2_2 = 0, 0

    for v in bigr_wo_int_dict.values():
        ent_2_1 -= (v/(sum(bigr_wo_int_dict.values()))) * math.log2(v/(sum(bigr_wo_int_dict.values())))
    
    for v in bigr_w_int_dict.values():
        ent_2_2 -= (v/(sum(bigr_w_int_dict.values()))) * math.log2(v/(sum(bigr_w_int_dict.values())))

    print(ent_2_1/2, ent_2_2/2, '\n', sum(bigr_wo_int_dict.values()), sum(bigr_w_int_dict.values()))
    
    ent_1_1, ent_1_2 = 0, 0
    for v in onegr_w_int_dict.values():
        ent_1_1 -= (v/(sum(onegr_w_int_dict.values()))) * math.log2(v/(sum(onegr_w_int_dict.values())))
    
    for v in onegr_wo_int_dict.values():
        ent_1_2 -= (v/(sum(onegr_wo_int_dict.values()))) * math.log2(v/(sum(onegr_wo_int_dict.values())))

    
    print(ent_1_1, ent_1_2, '\n', sum(onegr_wo_int_dict.values()), sum(onegr_w_int_dict.values()))
    # print(onegr_wo_int_dict)
    # print(onegr_w_int_dict)
