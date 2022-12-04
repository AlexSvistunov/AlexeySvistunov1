#блок Б номер 2
q=[]
def F(q):
	n=int(input('Введите число: '))
	if n == 0:
		return q
	q.append(n)
	return F(q)


p=F(q)
p.sort()
print('Второе по величине число: ',p[-2])