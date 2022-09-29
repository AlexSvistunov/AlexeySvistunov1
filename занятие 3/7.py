
z = int(input("Введите натуральное число "))
def Q(a):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        return ('Да')
    else:
        return ('Нет')

print(Q(z))