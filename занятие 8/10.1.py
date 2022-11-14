N = int(input("Введите число N: "))
a,b,c = input('Введите число a: '), input('Введите число b: ') , input('Введите число c: ')

count = 0
for y in range(100,N):
    if str(a) in str(y) and str(b) in str(y) and str(c) in str(y):
        count+=1
print(count)
