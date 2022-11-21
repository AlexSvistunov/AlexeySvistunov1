def F():
    a = [54,31,65,356,74652,4234,24,576,2,21,76,43,142,1,4]
    print(' '.join([str(i) for i in a]))
    c = []
    for i in a:
        if i < 10:
            c.append(str(0))
        if i > 20:
            c.append(str(1))
        if 10 <=i <= 20:
            c.append(str(i))
    print(' '.join(c))
F()