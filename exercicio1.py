print(" ____  ____  ____  ____")
print("||B ||||i ||||n ||||o ||")
print("||__||||__||||__||||__||")
print("|/__\||/__\||/__\||/__\|")

n = [int(x) for x in input().split()]
m2=0
m3=0
m4=0
m5=0

for num in n:
  if(num%2==0):
    m2=m2+1
  if(num%3==0):
    m=m3+1
  if(num%4==0):
    m4=m4+1
  if(num%5==0):
    m5=m5+1
    
print(m2, end="")
print(" Multiplo(s) de 2")
print("------------------------")
print(m3, end="")
print(" Multiplo(s) de 3")
print("------------------------")
print(m4, end="")
print(" Multiplo(s) de 4")
print("------------------------")
print(m5, end="")
print(" Multiplo(s) de 5")
