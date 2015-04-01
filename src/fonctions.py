""" this file contains fonctions ncessary for game.py"""


# lib imports
from random import sample, choice


def data():
    """returns:
            - 5 random numbers;
            - list of 3 results possible by just 2 numbers;
            - list of 3 results possible by 3 numbers;"""

    # random 5 numbers from 1 to 9
    n = sample( range(1, 10), 5)
    # lists results
    res_2, res_3 = list(), list()
    # possibles results by 2 numbers
    probability_2 = [
                    n[2]+n[0], n[2]-n[0], n[2]+n[1], n[2]-n[1],
                    n[2]+n[3], n[2]-n[3], n[2]+n[4], n[2]-n[4],
                    n[0]+n[1], n[0]-n[3], n[3]+n[4], n[4]-n[1]
    ]
    # possibles results by 3 numbers
    probability_3 = [
                    n[0]+n[1]-n[4], n[0]+n[1]-n[2], n[0]+n[2]-n[1],
                    n[0]+n[2]-n[3], n[0]+n[2]+n[3], n[0]+n[2]+n[4],
                    n[1]+n[0]-n[2], n[1]+n[0]-n[3], n[1]+n[2]-n[0],
                    n[1]+n[2]-n[3], n[1]+n[2]-n[4], n[1]+n[2]+n[4]
    ]
    # choose 3 from probability_2
    while len(res_2) < 3 :
        r = choice (probability_2)
        if r != 0 and r not in res_2:
            res_2.append( abs(r) )
    # choose 3 from probability_3
    while len(res_3) < 3:
        r = choice(probability_3)
        if r != 0 and r not in (res_2 or res_3):
            res_3.append( abs(r) )
    return n, res_2, res_3



def calcul_input(i):
    """return total the post type str."""
    # init total
    inpt = 0
    # len the input great than 3
    if len(i) > 2:
        if i[1] == '+':
            inpt = int(i[0]) + int(i[2])
        else:
            inpt = int(i[0]) - int(i[2])
    # len the input great than 4
    if 4 < len(i) < 7:
        if i[3] == '+':
            inpt += int(i[4])
        else:
            inpt -= int(i[4])
    return inpt


        

        

    
