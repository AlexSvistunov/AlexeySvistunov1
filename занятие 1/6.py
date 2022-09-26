x = 5                   #способ 1
y = 15
a = x
x = y
y = a
print(x,y)

x = 5                    #способ 2
y = 6
x , y = y , x
print(x,y)