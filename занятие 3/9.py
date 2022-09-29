z = int(input('Введите первую сторону шоколадки: '))
x = int(input('Введите вторую сторону шоколадки: '))
c = int(input('Введите количество долек: '))

def func(n,m,k):
    if k < n * m and (k % n == 0 or k % m == 0):
        return 'Да'
    else:
        return 'Нет'

print(func(z,x,c))