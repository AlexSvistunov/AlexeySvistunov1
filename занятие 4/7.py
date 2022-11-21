n=int(input("Введите натуральное число: "))
while n<1:
    print("Неверно! Введите натуральное число!")
    n = int(input("Введите натуральное число: "))
def F():
    z=0
    S=1
    for i in range(1,n+1):
        S*=i
        z=z+S
    return S
print(F())