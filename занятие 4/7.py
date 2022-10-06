n=int(input("Введите натуральное число: "))
while n<1:
    print("Неверно! Введите натуральное число!")
    n = int(input("Введите натуральное число: "))
z=0
S=1
for i in range(1,n+1):
    S*=i
    z=z+S
print(S)