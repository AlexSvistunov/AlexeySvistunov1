file1=open('C:/Users/pc/Desktop/prog/AlexeySvistunov/задание 10/SvistunovAlexey_U-223_vvod.txt','r')
file2=open('C:/Users/pc/Desktop/prog/AlexeySvistunov/задание 10/SvistunovAlexey_U-223_vivod.txt','w+')

N = []
c = file1.readlines()
for i in range(len(c)):
    N.append((c[i].rstrip()).split())
print(N)

def F(N):
    for i in range(len(N)):
        N[i].sort()

    maximum = 0
    for i in range(len(N)):
        if int(N[i][-1]) > maximum:
            maximum = int(N[i][-1])
    file2.write(str(maximum))
    file2.close()
F(N)