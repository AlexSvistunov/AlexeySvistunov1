
list = [1,2,3,4,5,6,6,1,2,8,8,9,10,1]
def F():
    global x
    s = set(list)
    g = []
    for i in s:
        if(list.count(i)>1):
            g.append(i)
    if len(g)>=1:
        print(g)
    else:
        print('Нет повторяющихся элементов!')
F()