#!/usr/bin/python3
import string
import sys
sys.path.append('../../cp1/prikhodko_fb-12_cp1')
from entropy_assessment import freqCalc
CHARSET_RU = ''.join([chr(char) for char in range(ord('а'),ord('я')+1,1) if char != ord('ъ')])
CHARSET_EN = string.ascii_lowercase
CHARSET = CHARSET_RU
MOD = len(CHARSET)

def xgcd(a:int,b:int) -> int:
    """
    Function extended GCD, used for finding unit in a ring
    input:
        a,b - integers for gcd(a,b)
    output:
        g   - gcd(a,b)
        x,y from x*a + y*b = g
    """
    if a == 0 : 
        return b,0,1
    g,xr,yr = xgcd(b%a, a) 
    x,y = yr - (b//a) * xr, xr
    return g,x,y 


def parseText(pt:str) -> str:
    """
    Function for text parsing, remove all characters that are not in CHARSET
    input:
        pt  - plain text 
    output:
        ptc - plain text cleared
    """
    ptc = ''.join([char for char in pt.lower() if char in CHARSET])
    return ptc

def parseBigrams(text:str) -> list:
    """
    Function to create bigrams of form x0*m + x1
    input:
        text    - text to parse 
    output:
        res     - list of bigrams
    """
    bigrams = [text[i:i+2] for i in range(0,len(text),2)]
    res = []
    for bg in bigrams:
        x0 = CHARSET.index(bg[0])
        x1 = CHARSET.index(bg[1])
        X = x0 * MOD + x1
        res += [X]
    return res

def getText(bigrams:list) -> str:
    """
    Function to convert list of bigrams in form x0*m + x1 to text 
    input:
        bigrams - list of bigrams 
    output:
        text    - created text
    """
    text = "" 
    for bg in bigrams:
        x1 = CHARSET[bg%MOD]
        x0 = CHARSET[bg//MOD]
        text += x0 + x1 
    return text

def affineBigramEncrypt(a:int,b:int,pt:str) -> str:
    """
    Basic function for text encryption using bigram version of Affine Cipher
    input:
        a,b - cipher key (a - factor, b - addend)
        pt  - plain text 
    output:
        ct  - cipher text
    """
    pt = parseText(pt)
    if len(pt) % 2 != 0: pt += pt[-1]
    bigrams_intConv = parseBigrams(pt)
    ct_intConv = [(bg*a + b)%MOD**2 for bg in bigrams_intConv]
    ct = getText(ct_intConv)
    return ct

def affineBigramDecrypt(a:int,b:int,ct:str) -> str:
    """
    Basic function for text decryption using bigram version of Affine Cipher
    input:
        a,b - cipher key (a - factor, b - addend)
        ct  - cipher text 
    output:
        pt  - plain text
    """
    _,a_inv,_ = xgcd(a,MOD**2)
    bigrams_intConv = parseBigrams(ct)
    pt_intConv = [((bg - b) * a_inv)%MOD**2 for bg in bigrams_intConv]
    pt = getText(pt_intConv)
    return pt




def main() -> None:
    pt_ru = "Криптография это весело, правда?"
    pt_en = "Cryptography is fun, right?"
    ct = affineBigramEncrypt(1,2,pt_ru)
    print(pt_ru)
    print(ct)
    pt_d = affineBigramDecrypt(1,2,ct)
    print(pt_d)
    freq = freqCalc(parseText(pt_ru),2,2)
    print(freq)

if __name__ == "__main__":
    main()
