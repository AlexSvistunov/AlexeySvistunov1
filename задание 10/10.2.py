file1=open('C:/Users/pc/Desktop/prog/AlexeySvistunov/задание 10/SvistunovAlexey_U-223_vvod(2).txt','r')
file2=open('C:/Users/pc/Desktop/prog/AlexeySvistunov/задание 10/SvistunovAlexey_U-223_vivod(2).txt','w+')

def sort_by_line(matrix, k):
    m = [(i, el) for i, el in enumerate(matrix[k].copy())]
    m.sort(key=lambda e: e[1])
    w = len(matrix[0])
    h = len(matrix)
    new_matrix = []
    for i in range(h):
        new_matrix.append([])
        for j in range(w):
            new_matrix[i].append(matrix[i][m[j][0]])
    return new_matrix


matrix = []
c = file1.readlines()
for i in range(len(c)):
    matrix.append((c[i].rstrip()).split())
print(matrix)
d = (sort_by_line(matrix, 2))
for i in range(len(matrix)):
    file2.write(" ".join(d[i]) + "\n")
file2.close()