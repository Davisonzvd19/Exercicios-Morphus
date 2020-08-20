print(" ____  ____  ____  ____")
print("||B ||||i ||||n ||||o ||")
print("||__||||__||||__||||__||")
print("|/__\||/__\||/__\||/__\|")

n=int(input())
l = [int(x) for x in input().split()]
m2=0
m3=0
m4=0
m5=0
for num in range(n):
    if(l[num]%2==0):
        m2=m2+1
    if(l[num]%3==0):
        m3=m3+1
    if(l[num]%4==0):
        m4=m4+1
    if(l[num]%5==0):
         m5=m5+1
print(m2, end="")
print(" Multiplo(s) de 2")
print(m3, end="")
print(" Multiplo(s) de 3")
print(m4, end="")
print(" Multiplo(s) de 4")
print(m5, end="")
print(" Multiplo(s) de 5")
