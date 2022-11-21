q = input("Введите ваше предложение: ")
def F(x):
    global q
    s = q.split(' ')
    d = []
    for i in s:
        d.append(i[0].upper() + i[1:])
    print(" ".join(d))
F(q)