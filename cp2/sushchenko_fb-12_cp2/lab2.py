alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alph_len = len(alphabet)


def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        i_index = alphabet.index(text[i])
        k_index = alphabet.index(key[i % len(key)])
        result += alphabet[(i_index + k_index) % alph_len]
    return result


def index_vidpov(text):
    text_length = len(text)
    amounts = {}
    sum = 0
    if text_length - 1 > 0:
        for i in text:
            if i in amounts:
                amounts[i] += 1
            else:
                amounts[i] = 1

        for i in alphabet:
            if i in amounts:
                sum += amounts[i] * (amounts[i] - 1)

        return sum/(text_length*(text_length-1))
    else:
        return 0


def find_blocks(text, r):
    result = ""
    for i in range(0, len(text) - r, 2*r):
        result += text[i]
        result += text[r+i]
    return result


def find_key_len(en_text):
    for i in range(2, 31):
        blocks = find_blocks(en_text, i)
        index_vid = index_vidpov(blocks)
        print(index_vid)

def find_keys(block_text):
    freq_decr = list("оеаинт")
    freqs_encr = {}

    for i in block_text:
        if i in freqs_encr:
            freqs_encr[i] += 1
        else:
            freqs_encr[i] = 1

    for i in alphabet:
        if i in freqs_encr:
            freqs_encr[i] = freqs_encr[i]/len(block_text)

    freqs_encr = dict(sorted(freqs_encr.items(), key=lambda x: x[1], reverse=True))

    for i in range(5):
        y_i = alphabet.index(list(freqs_encr)[i])
        k_i = alphabet.index(freq_decr[i])
        #print(freqs_encr[i])
        print("key:", (y_i - k_i) % alph_len)


if __name__ == '__main__':
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    print("ВТ:", text)
    print("index_vidpov:", index_vidpov(text))

    keys = ["шо", "бру", "крип", "мячик", "безпонятияк"]

    for key in keys:
        r_key = encrypt(text, key)
        index_v = index_vidpov(r_key)
        print("ШТ:", r_key)
        #print(blocks(text, len(key)))
        print("index_vidpov:", index_v)

    with open("text2.txt", "r", encoding="utf-8") as f:
        en_text = f.read()

    #block = blocks(en_text, 2)
    #print(find_blocks(en_text, 4))
    #print(break_text_into_blocks(en_text, 4))
    #sum2 = 0
    #for i in block:
       # print(i)
        #sum2 += index_vidpov(i)
    #print(sum2/len(block))
    find_key_len(en_text) # 19
    find_keys(find_blocks(en_text, 19))
