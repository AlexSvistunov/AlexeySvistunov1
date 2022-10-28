a=int(input("Введите число: "))
b=int(input("Введите число: "))
s=0
while b!=0:
    if b>a:
        s+=1
    a=b
    b=int(input("Введите число: "))
print(s)