def oddeven(x):
    lst = []
    for i in x:
        if (i % 3 == 0):
            lst.append(i)
    return lst

x = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

print (oddeven(x))