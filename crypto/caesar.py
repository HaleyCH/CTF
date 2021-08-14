__author__ = "HaleyC"

def getCh(ch, i):
    if ch.islower():
        return chr( ( ord(ch)  - ord("a") + i ) % 26 + ord("a") )
    if ch.isupper():
        return chr( ( ord(ch)  - ord("A") + i ) % 26 + ord("A") )
    return ch

def getCh_allCaesar(ch,i):
    return chr(ord(ch)+i)

def print_ASCII(ch):
     s = ""
     for c in ch:
         s = s+ str(ord(c)) +" "
     print("[*]:"+s)
     ss = ""
     css = ""
     for c in range(len(ch)-1):
         ss = ss + str(ord(ch[c+1])-ord(ch[c])) + " "
         css = css + chr(ord(ch[c+1])-ord(ch[c])+ord('a')) + " "
     print("[*]:"+ss)
     print("[*]:"+css)

text = input("[@]: Input text:")

for i in range(26):
    out = ""
    j = i
    for ch in text:
        out += getCh(ch,j)
       #  j += 1
    print("[+] :"+out)
print_ASCII(text)
print("[!]: Finish.")