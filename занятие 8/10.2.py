ez = input('Введите предложение: ').split(' ')[::-1]
def F(x):
    global ez
    print(' '.join(ez))
F(ez)