import random as r
def jackpot():
    f_num = r.randint(1,10)
    s_num = r.randint(1,10)
    t_num = r.randint(1,10)

    if ((f_num == 7) and (s_num == 7) and (t_num == 7)):
        print ("잭팟")
    else:
        print ("잭팟 아님")

def replay(user):
    if (user == 'quit'):
        exit()
    else:
        jackpot()
        return replay(input())

jackpot()
replay(input())
