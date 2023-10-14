#!/usr/bin/python3

from collections import Counter
from random import choice, randint
import sys

ALPHABET = "абвгдежзийклмнопрстуфхцчшщыьэюя"
M = len(ALPHABET)
FREQS = {'о': 0.114, 'е': 0.086, 'а': 0.078, 'и': 0.068, 'н': 0.063, 'т': 0.061, 'с': 0.051, 'в': 0.045, 'л': 0.045, 'р': 0.041, 'к': 0.041, 'д': 0.031, 'м': 0.03, 'у': 0.03, 'п': 0.028, 'ь': 0.021, 'ы': 0.019, 'ч': 0.019, 'б': 0.019, 'я': 0.019, 'г': 0.017, 'з': 0.017, 'ж': 0.011, 'х': 0.01, 'й': 0.01, 'ш': 0.01, 'ю': 0.006, 'ц': 0.003, 'щ': 0.003, 'э': 0.002, 'ф': 0.001}
BIGRAMS = ['вс', 'се', 'ех', 'хр', 'ри', 'ис', 'ст', 'то', 'оп', 'пр', 'ро', 'од', 'да', 'ав', 'вц', 'цы', 'ыо', 'ди', 'ин', 'нт', 'та', 'ам', 'мт', 'ол', 'ль', 'ьк', 'ко', 'ои', 'ио', 'ос', 'ан', 'на', 'вл', 'ли', 'ив', 'ва', 'ае', 'ет', 'тч', 'чт', 'ов', 'ве', 'ед', 'дь', 'ьо', 'он', 'ни', 'иу', 'уж', 'же', 'ем', 'ме', 'ер', 'рт', 'тв', 'вы', 'ые', 'еэ', 'эк', 'ке', 'ее', 'ду', 'уб', 'би', 'нн', 'но', 'ог', 'го', 'ло', 'ая', 'як', 'ка', 'ак', 'яс', 'ск', 'аз', 'за', 'ал', 'лн', 'оз', 'зд', 'др', 'ре', 'ев', 'ву', 'ук', 'зы', 'ыв', 'яп', 'па', 'ьц', 'це', 'мн', 'ап', 'по', 'ле', 'еч', 'ож', 'жв', 'вэ', 'эт', 'ту', 'ом', 'ат', 'ух', 'хо', 'от', 'ть', 'ьн', 'кр', 'ра', 'ай', 'йс', 'св', 'во', 'ой', 'йт', 'ти', 'вк', 'ое', 'вр', 'мя', 'яз', 'де', 'ес', 'сь', 'ьт', 'те', 'еб', 'бе', 'ен', 'не', 'еп', 'оя', 'ял', 'лы', 'ый', 'йд', 'дв', 'ор', 'рп', 'ещ', 'щи', 'иц', 'ца', 'аж', 'жи', 'вз', 'до', 'ок', 'му', 'уд', 'ел', 'лу', 'ус', 'вв', 'зя', 'яв', 'вш', 'ши', 'ие', 'ег', 'ну', 'ую', 'юп', 'пл', 'ла', 'уо', 'тд', 'вн', 'ек', 'кн', 'ня', 'яж', 'ьл', 'лю', 'юд', 'ии', 'им', 'ею', 'ющ', 'тр', 'ас', 'иш', 'шк', 'ку', 'ун', 'аг', 'га', 'ад', 'ит', 'ьб', 'бл', 'иж', 'жн', 'уи', 'гд', 'ез', 'зв', 'ся', 'йп', 'ич', 'чи', 'ны', 'ыи', 'йн', 'рд', 'че', 'кв', 'вч', 'ах', 'хс', 'сб', 'дн', 'ою', 'юн', 'ар', 'ру', 'ию', 'юс', 'со', 'гр', 'иб', 'бу', 'мж', 'жа', 'ьр', 'ур', 'зг', 'тс', 'ми', 'ир', 'сс', 'аю', 'см', 'мо', 'ьв', 'юм', 'ут', 'тб', 'бо', 'ят', 'ьс', 'яч', 'об', 'бы', 'ын', 'сд', 'ьд', 'ых', 'ха', 'яб', 'аш', 'мг', 'ге', 'ям', 'мк', 'ры', 'бк', 'ки', 'ип', 'пи', 'жк', 'ум', 'ша', 'ря', 'яг', 'гл', 'ыб', 'ыл', 'пе', 'еш', 'нц', 'ил', 'из', 'зо', 'са', 'юк', 'ик', 'зч', 'кг', 'лх', 'ош', 'шо', 'ба', 'гз', 'зн', 'йи', 'сн', 'кя', 'яд', 'бя', 'яю', 'юч', 'яи', 'вп', 'лж', 'ги', 'их', 'хм', 'тн', 'ыр', 'ьи', 'лп', 'уч', 'лт', 'тя', 'ец', 'цп', 'лс', 'ше', 'чу', 'ье', 'ящ', 'ий', 'йм', 'шп', 'си', 'сю', 'чн', 'цу', 'дя', 'ян', 'иг', 'жп', 'иэ', 'оо', 'ео', 'ви', 'ул', 'ча', 'яе', 'оу', 'тп', 'пк', 'сл', 'ма', 'аи', 'нд', 'ей', 'йк', 'ид', 'уз', 'зк', 'кл', 'ьа', 'лч', 'зз', 'ач', 'оч', 'ув', 'лв', 'ыч', 'нб', 'ды', 'ыс', 'вь', 'ще', 'чш', 'еж', 'хи', 'тт', 'аб', 'еи', 'уш', 'ык', 'кб', 'ыз', 'дм', 'иф', 'фа', 'нп', 'ья', 'дч', 'жо', 'рс', 'пя', 'хв', 'хл', 'оэ', 'тф', 'фо', 'кт', 'зж', 'ея', 'мы', 'аа', 'хт', 'ты', 'чс', 'лм', 'бр', 'кч', 'ци', 'мп', 'жт', 'жд', 'нь', 'дц', 'ыш', 'тм', 'нк', 'уг', 'рн', 'ох', 'яй', 'ьз', 'ьч', 'ьп', 'йч', 'ып', 'гу', 'бн', 'зь', 'цс', 'бв', 'юу', 'ью', 'зп', 'шь', 'ыд', 'рм', 'зи', 'яф', 'фе', 'тю', 'кс', 'дл', 'ля', 'жч', 'сх', 'фи', 'вт', 'зе', 'мл', 'ыт', 'мх', 'мв', 'юл', 'уп', 'мб', 'рж', 'ыг', 'бс', 'ым', 'дс', 'ьж', 'чч', 'лк', 'чк', 'лз', 'рц', 'йх', 'хщ', 'ао', 'кщ', 'ща', 'зб', 'дк', 'оа', 'ау', 'ищ', 'вм', 'шл', 'нч', 'лр', 'ия', 'сп', 'ащ', 'йр', 'ню', 'йб', 'йв', 'цв', 'нв', 'вг', 'гв', 'нс', 'ху', 'ср', 'кп', 'еу', 'хд', 'вя', 'хз', 'ац', 'рб', 'чь', 'кд', 'вд', 'лг', 'мш', 'мс', 'юр', 'лб', 'йо', 'кк', 'шн', 'ях', 'ьу', 'юи', 'дз', 'рк', 'мм', 'ыщ', 'пн', 'зш', 'су', 'уа', 'йж', 'хш', 'пы', 'хб', 'ьш', 'цз', 'ыу', 'гн', 'зу', 'ьм', 'жб', 'хн', 'тк', 'сч', 'ущ', 'йг', 'вж', 'рр', 'рв', 'лл', 'зл', 'чо', 'шу', 'юо', 'тг', 'рф', 'рг', 'дп', 'еа', 'хг', 'вх', 'сц', 'нл', 'мч', 'жм', 'гс', 'йц', 'цо', 'яо', 'тж', 'мц', 'яэ', 'сы', 'мэ', 'лд', 'ощ', 'йз', 'рз', 'пу', 'йл', 'оф', 'тл', 'мз', 'нз', 'гш', 'уя', 'дт', 'зм', 'яа', 'тщ', 'сж', 'юф', 'кф', 'юб', 'ют', 'жу', 'уе', 'мд', 'эй', 'йф', 'нф', 'фу', 'пч', 'рш', 'пп', 'яя', 'яр', 'аэ', 'эд', 'йш', 'бщ', 'рь', 'хп', 'яу', 'йа', 'ьг', 'зт', 'пь', 'зр', 'юж', 'нг', 'юз', 'цк', 'кж', 'йу', 'эх', 'фр', 'нр', 'юх', 'цм', 'бм', 'хэ', 'нх', 'тх', 'бд', 'вб', 'чр', 'дд', 'хч', 'нм', 'юв', 'хе', 'мр', 'кз', 'хх', 'дш', 'уй', 'аф', 'фт', 'юш', 'цэ', 'рч', 'сэ', 'зс', 'жс', 'ьэ', 'иа', 'еф', 'дю', 'гк', 'км', 'ьф', 'нэ', 'яш', 'сз', 'цч', 'цт', 'тш', 'шт', 'оц', 'тэ', 'дх', 'рл', 'юэ', 'вф', 'мф', 'йя', 'жэ', 'ыа', 'бт', 'дб', 'уф', 'бэ', 'бц', 'рю', 'юг', 'кш', 'фя', 'йэ', 'ьх', 'сг', 'юа', 'хк', 'ыэ', 'бь', 'сш', 'тз', 'пщ', 'юя', 'тц', 'эс', 'йе', 'цн', 'кэ', 'лэ', 'хж', 'лф', 'рх', 'дг', 'зэ', 'нщ', 'юю', 'щу', 'пц', 'пт', 'хц', 'бж', 'юе', 'эл', 'ыж', 'гп', 'уу', 'бш', 'фы', 'сф', 'хф', 'бх', 'жл', 'шг', 'гт', 'рщ', 'гм', 'нж', 'эм', 'сщ', 'жх', 'жр', 'пс', 'лш', 'гб', 'бг', 'шв', 'чв', 'гч', 'бп', 'щр', 'фл', 'хь', 'мщ', 'ьщ', 'уэ', 'хя', 'кх', 'зц', 'жз', 'чп', 'гг', 'дж', 'цх', 'ыя', 'щн', 'фс', 'цб', 'гя', 'цг', 'жж', 'жя', 'вщ', 'шб', 'мь', 'чг', 'чэ', 'шд', 'жь', 'щь', 'кц', 'щс', 'бз', 'дэ', 'ыф', 'лщ', 'йю', 'зю', 'чд', 'яц', 'шс', 'пд', 'пг', 'цд', 'ээ', 'нш', 'бю', 'рэ', 'чз', 'чх', 'юц', 'пш', 'йщ', 'вю', 'уц', 'зх', 'бб', 'шм', 'пв', 'хю', 'шх', 'гэ', 'фм', 'фь', 'бч', 'уь', 'чм', 'чб', 'шр', 'чж', 'мю', 'ыц', 'лц', 'цр', 'чл', 'зф', 'эф', 'пх', 'шя', 'цц', 'фч', 'що', 'эп', 'цю', 'шж', 'фн', 'жф', 'дщ', 'цф', 'эг', 'шз', 'жг', 'шч', 'щт', 'цл', 'жц', 'ыю', 'зщ', 'фб', 'эч', 'юй', 'рй', 'гж', 'гх', 'пб', 'ця', 'нй']
IOC_TH = 0.055
ENTROPY = 4.457
KEYS = ["т", "да", "зло", "крах", "месть", "денацификация", "самоуничтожение", "сельскохозяйственный", "электрофотополупроводниковый"]

# Read n characters of file fname.
def read_file(fname: str, n=0) -> str:
    with open(fname, "r") as f:
        if n:
            text = f.read(n)
        else:
            text = f.read()
    return text
 
# Filter and edit text.   
def format_text(text: str) -> str:
    # Remove uppercase letters.
    text = text.lower()
    # Replace some letters.
    text = text.replace("ё", "е")
    text = text.replace("ъ", "ь")
    # Remove other symbols.
    for i in range(len(text)):
        if text[i] not in ALPHABET:
            text = text.replace(text[i], " ")
    text = text.replace(" ", "")
    return text

# Calculate appearences of letters in text.
def count_letters(text: str) -> dict:
    return Counter(text)
   
# Calculate practical index of coincidence.
def ioc(text: str) -> float:
    n = len(text)
    count = count_letters(text)
    ioc = 0
    for i in ALPHABET:
        ioc += count[i] * (count[i] - 1)
    return ioc / (n * (n - 1))
    
# Separate ciphered text into blocks.
def separate(text: str, period: int) -> list:
    blocks = [''] * period
    for i in range(len(text)):
        blocks[i % period] += text[i]
    return blocks

# Find period (key length).    
def find_period(text: str, show=False) -> int:
    # Initialize period.
    period = 1
    acc = 0.005
    if show:
        print("Period\tIoC")
    while period <= 50:
        blocks = separate(text, period)
        res = 0
        for b in blocks:
            res += ioc(b)
        res /= period
        # Visualize correlation between period and IoC values.
        if show:
            print(f"{period}\t{res}")
        else:
            if IOC_TH - res < acc:
                return period
        period += 1
    return 0

# BASED ON BIGRAMS
def text_is_valid(text: str) -> bool:
    for i in range(len(text)-1):
        if text[i:i+2] not in BIGRAMS:
            return False
    return True
    
def key_is_valid(text: str, key: str, ind: int) -> bool:
    ot = decrypt(text, key)
    for i in range(ind, len(ot), len(key)):
        if ot[i:i+2] not in BIGRAMS:
            print(f"Key {key} ({key[ind:ind+2]}) is invalid ({ot[i:i+2]} at {i})\n{ot[i:i+30]}")
            return False
    return True    
    
# Find key based on found period.    
def find_key(text: str, period: int):
    blocks = separate(text, period)
    # List of the most common letters in blocks.
    common = []
    for b in blocks:
        # Find and store the most common letter in b.
        letters = dict(sorted(count_letters(b).items(), reverse=True, key=lambda item: item[1]))
        common.append(encode(list(letters)[0]))
    # Create list of the most common russian letter.
    s = [encode(list(FREQS)[0])] * period
    # Create key based on the most common letters of russian and CT.
    base_key = [decode(y-x) for x, y in zip(common, s)]
    # Find the first two letters of a key that may be correct. 
    for i in ALPHABET:
        base_key[0] = i
        for j in ALPHABET:
            base_key[1] = j
            key = ''.join(base_key)
            if text_is_valid(key[:2]):
                print(f"Possible key: {key}")
                if key_is_valid(text, key, 0):
                    print(f"{key} is correct")
                    visualize(text[:90], key, 'd')
    
# Swap letters with their corresponding numbers.
def encode(text: str):
    encoded = [ALPHABET.index(x) for x in text]
    if len(encoded) == 1:
        return encoded[0]
    else:
        return encoded

# Swap numbers with their corresponding letters.
def decode(nums) -> str:
    if isinstance(nums, int):
        return ALPHABET[nums]
    else:
        return ''.join([ALPHABET[x] for x in nums])
   
# Encrypt text with Vigenere cipher.
def encrypt(text: str, key: str) -> str:
    ct = encode(text)
    r = encode(key)
    sz = len(r)
    for i in range(len(text)):
        ct[i] = (ct[i] + r[i % sz]) % M
    return decode(ct)

# Decrypt text encrypted with Vigenere cipher.  
def decrypt(text: str, key: str):
    ct = encode(text)
    r = encode(key)
    sz = len(r)
    for i in range(len(text)):
        ct[i] = (ct[i] - r[i % sz]) % M
    return decode(ct)

# Support function for visualize.
def split_text(text: str, size=30) -> list:
    res = []
    i = 0
    n = len(text)
    while i < n:
        res.append(text[i:i+size])
        i += size
    return res
   
# Visualize encryption.
def visualize(text: str, key: str, act='e') -> None:
    ksize = len(key)
    i = 0
    parts = split_text(text)
    for p in parts:
        tsize = len(p)
        if act == 'e':
            print(f"""M:\t{p}
r:\t{key * (tsize//ksize) + key[:tsize%ksize]}
C:\t{encrypt(p, key)}\n""")
        elif act == 'd':
            print(f"""C:\t{p}
r:\t{key * (tsize//ksize) + key[:tsize%ksize]}
M:\t{decrypt(p, key)}\n""")
        else:
            print("Incorrect act value. Choose between \'e\' and \'d\'")    

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("""USAGE: ./cp2.py INPUTFILE
[*] INPUTFILE\t- path to the input file""")
    else:
        f = sys.argv[1]
        # Read and format russian text.
        text = format_text(read_file(f))
        
        # Task 1. Encrypt custom text with different keys.
        '''
        print(find_period(text))
        for r in KEYS:
            print(f"IoCpr = {ioc(encrypt(text, r))}")
            visualize(text, r)
        '''
        # Task 2. Find key length.
        period = find_period(text)
        #print(f"Key length is {period}")
        # Task 3. Find key.
        find_key(text, period)
        #visualize(text[:90], "гтттакоучтмныш", 'd')
        #visualize(text[:30], "гууужьчтоущшуу", 'd')
        #visualize(text[:30], "энннахсминутнн", 'd')
        #visualize(text[:60], "гсдтщбтнстюдйд", "d")
        #keys = open("keys.txt", "r").read().split("\n")
        #for k in keys:
            #visualize(text[:30], k, 'd')
        
'''
# IOC_TH was found by using iocth and FREQS:

# Calculate theoretical index of coincidence.
def iocth(text: str) -> float:
    n = len(text)
    th = 0
    for i in ALPHABET:
        th += FREQS[i] * n * (FREQS[i] * n - 1)
    return th / (n * (n - 1))
''' 
