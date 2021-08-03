__author__ = "HaleyC"

def getCh(ch, i):
    if ch.islower():
        return chr( ( ord(ch)  - ord("a") + i ) % 26 + ord("a") )
    if ch.isupper():
        return chr( ( ord(ch)  - ord("A") + i ) % 26 + ord("A") )
    return ch

def getCh_allCaesar(ch,i):
    return chr(ord(ch)+i)

text = input("[@]: Input text:")

for i in range(26):
    out = ""
    j = i
    for ch in text:
        out += getCh_allCaesar(ch,j)
       #  j += 1
    print("[*] :"+out)
print("[!]: Finish.")