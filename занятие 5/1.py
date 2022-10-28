N = int(input("Введите число: "))
def F(n):
    b = 1
    while b**2 <= n:
        print (b**2)
        b += 1
F(N)