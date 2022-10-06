n = int(input("Введите число n>0: "))
while n<=0:
    print("Ошибка! Число n должно быть натуральным")
    n = int(input("Введите число n>0: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Факториал числа " + str(n) + " равен: ",fact)