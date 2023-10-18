# 5 var Tsema Tsypun


alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


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
    

def vigenere(key: str, text: str, decrypt: bool) -> str:
    key = key.lower()
    r = len(key)
    m = len(alpha)
    result = ""

    for i in range(len(text)):
        result += alpha[(alpha.index(text[i]) + ((-1) ** int(decrypt))*alpha.index(key[i % r])) % m]

    return result
