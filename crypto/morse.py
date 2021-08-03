def getCh(ch):
    Keys = 'abcdefghijklmnopqrstuvwxyz0123456789'
    Values = ['.-','-...','-.-.','-..','.','..-.','--.','....',
          '..','.---','-.-','.-..','--','-.','---','.--.',
          '--.-','.-.','...','-', '..-','...-','.--','-..-',
          '-.--','--..','-----','.----','..---','...--',
          '....-','.....','-....','--...','---..','----.']
    i = Values.index(ch)
    if i:
        return Keys[i].upper()
    return "ERROR "

def decode(text, dot=".", line="-", spl=" "):
    text.replace(dot,".")
    text.replace(line,"-")
    chs = text.split(spl)
    out = ""
    for ch in chs:
        out += getCh(ch)
    print("[!]:"+out)

decode(".. .-.. --- ...- . -.-- --- ..-")