# 5 var Tsema Tsypun


alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def c_count(text: str, n: int, ngr_intercept=False) -> dict[str, float]:
    step = 1 if ngr_intercept else n
    c_dict = {}
    
    for i in range(0, len(text) - n, step):
        if not text[i: i + n]:
            continue

        if text[i: i + n] not in c_dict.keys():
            c_dict.update({text[i: i + n]: 1})
        else:
            c_dict[text[i: i + n]] += 1

    return c_dict


def text_purification(fLine: str, isnlp=False, save_space=False) -> (bool, str):
    isSpacePresent = False
    isNewLineCPresent = isnlp
    isBegining = True

    substitutions = {"ё": "е"}
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

        else:
            continue

        isSpacePresent = False
        isNewLineCPresent = False
        isBegining = False

    return isNewLineCPresent, output
    

def vigenere(key: str, text: str, decrypt=False) -> str:
    key = key.lower()
    r = len(key)
    m = len(alpha)
    result = ""

    for i in range(len(text)):
        result += alpha[(alpha.index(text[i]) + ((-1) ** int(decrypt))*alpha.index(key[i % r])) % m]

    return result


def ind_of_coincidence(c_dict: dict, text_len: int):
    result = 0
    for c in c_dict.values():
        result += c * (c - 1)

    return result / (text_len * (text_len - 1))


def g():
    with open("text_to_encrypt.txt", "r", encoding="utf-8") as f:
        while (l := f.readline()):
            yield l


if __name__ == "__main__":
    isnlp = False
    p_text = ""
    for l in g():
        isnlp, pt = text_purification(l, isnlp)
        p_text += pt

    ind = ind_of_coincidence(c_count(p_text, 1), len(p_text))
    print(f"\n\nI: {ind}\n\nO: {p_text}")

    keys = ("бе", "чай", "пиво", "кефир", "пиццасананасами")

    for k in keys:
        ct = vigenere(k, p_text)
        ind = ind_of_coincidence(c_count(ct, 1), len(ct))
        print(f"\n\nKey length: {len(k)}\n\nI: {ind}\n\nC: {ct}")
    
