def F(a,b):
    while a > b:
        print("Ошибка! Не соответствует условию, при котором a<=b")
    for i in range(a,b+1):
        print(i)
(F(int(input('Введите число a: ')),int(input('Введите число b: '))))


