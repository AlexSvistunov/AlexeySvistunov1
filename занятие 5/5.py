def F():
    b = 0
    while int(input("Введите число: ")) != 0:
        b += 1
    return(b)
print("Кол-во членов в последовательности:",F())