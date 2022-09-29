def qwe(n):
    hours = n % (60*24)//60
    mins = n % 60
    return hours,mins
print(qwe(30000))