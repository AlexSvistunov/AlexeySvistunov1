def F():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    for i in range(a,b+1):
        print(i)
    for z in range(a,b-1,-1):
        return z
(F())