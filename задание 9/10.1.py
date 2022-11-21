
matriza = [[11,17,15,16],
[18,15,12,10],
[5,9,7,15]]
def F(matriza):
    print('Исходная матрица: ')
    for i in range(len(matriza)):
        for j in range(len(matriza[0])):
            print(matriza[i][j], end = ' ')
        print()


    for i in range(len(matriza)):
        matriza[i].sort()

    maximum = 0

    for i in range(len(matriza)):
        if matriza[i][-1] > maximum:
            maximum = matriza[i][-1]

    print('Измененная матрица: ')

    for i in range(len(matriza)):
        for j in range(len(matriza[0])):
            print(matriza[i][j], end = ' ')
        print()

    print('Максимальный элемент среди упорядоченных строк: ', maximum)
F(matriza)