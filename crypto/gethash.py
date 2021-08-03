import random
import hashlib

def get_hash(length):
    alphabase = "abcdefghijklmnopqrstuvwxyz1234567890"
    text = "a"
    m = hashlib.md5()
    m.update(text.encode('gbk'))

    while not m.hexdigest()[:2] == "0e":
        text = ""
        for i in  range(length):
            text = text+ random.choice(alphabase)
            m = hashlib.md5()
            m.update(text.encode("gbk"))
    return text

val1 = get_hash(5)
val2 = get_hash(5)

print("[!] Val1 : " + val1 + "| MD5 : " + hashlib.md5(val1.encode("gbk")).hexdigest())
print("[!] Val2 : " + val2 + "| MD5 : " + hashlib.md5(val2.encode("gbk")).hexdigest())
