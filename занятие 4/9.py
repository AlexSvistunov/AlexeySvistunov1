
n = int(input("Введите кол-во чисел из ряда Фибоначчи: "))
def S(z):
    x = 1
    c = 0
    while(x<z):
        x,c=x+c,x
    return(x+c-1)
print("Сумма чисел равна: ",S(n))

