import re

n = int(input())
for i in range(n):
    texto = input()
    txt = ''
    for l in texto:
        if re.match("[a-zA-Z]", l):
            txt += chr(ord(l)+3)
        else:
            txt += l
    txt = txt[::-1]
    meio = int((len(txt)/2))
    m1 = txt[0:meio]
    m2 = txt[meio:]
    m = ''
    for l in m2:
        m += chr(ord(l)-1)
    txt1 = m1+m
    print(txt1)
