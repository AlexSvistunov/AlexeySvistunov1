n = int(input('Введите целое число N: '))
def F(x):
    sum = 0
    for i in range(x):
        sum+=int(input("Введите число: "))
    return(sum)
print("Сумма чисел равна:",F(n))