import random as r

lst = []

def part():
    rand = r.randint(0,2)

    if (rand == 0):
        return 'A'
    elif (rand == 1):
        return 'B'
    else:
        return 'C'

for i in range(1,101):
    lst.append([i, part()])

print (lst)

dic = {}

for i in range(1,101):
    dic[i] = part()

print (dic)