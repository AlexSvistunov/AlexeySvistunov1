n = int(input("Введите количество ступенек: "))
while n > 9 or n <=0:
    print("Неверно! Введите число от 1 до 9!")
    n = int(input("Введите количество ступенек: "))
for i in range(n):
    for z in range(1,i+2):
        print(z,end='')
    print()