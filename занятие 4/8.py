n = int(input("Введите количество ступенек: "))
def F(x):
    if x > 9 or x < 1:
        print ("Неверно! Введите числа от 1 до 9!")
        n = int(input("Введите количество ступенек: "))
    else:
        for i in range (1, x+1):
            for k in range(1, i+1):
                print (k, sep='', end='')
            print()
F(n)