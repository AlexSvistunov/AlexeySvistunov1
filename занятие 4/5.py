n = int(input("Введите натуральное число: "))
while n<1:
    print("Ошибка! Вы ввели неверное число!:")
    n = int(input("Введите натуральное число: "))
s = 0
for i in range(1,n+1):
    s+=i**3
print(s)
