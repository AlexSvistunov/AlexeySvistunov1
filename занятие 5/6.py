x=int(input("Введите число: "))
b=0
S=0
while x!=0:
    S+=x
    b+=1
    x=int(input("Введите число: "))
print(S/b)