q = input("Введите ваше предложение: ")
s = q.split(' ')
d = []
for i in s:
    d.append(i[0].upper() + i[1:])
print(" ".join(d))