import random
from legalmoves import *


def gen_filled_board():

    table = []
    for i in range(9):
        table.append([0,0,0,0,0,0,0,0,0])

    def gen_numb(li):
        if len(li) == 0:
            return False
        return li[random.randint(0, len(li)-1)]

    def gen_table(x,y):
        if x == 9:
            if y == 8:
                return True
            else:
                y += 1
                x = 0

        run = True
        li = [1,2,3,4,5,6,7,8,9]

        while run:
            int = gen_numb(li)

            if int == False:
                return False

            li.remove(int)
            if is_legal_move(x,y,int, table):
                table[y][x] = int
                if gen_table(x+1,y):
                    return True
                else:
                    table[y][x] = 0

        return False

    gen_table(0,0)
    return table


def find_solution(table):

    def solve_board(x ,y):
        if x == 9:
            if y == 8:
                return True
            else:
                y += 1
                x = 0
        while table[y][x] != 0:
            x += 1
            if x == 9:
                if y == 8:
                    return True
                else:
                    y += 1
                    x = 0

        for i in range(1,10):
            if is_legal_move(x,y,i, table):
                table[y][x] = i
                if solve_board(x+1,y):
                    return True
                else:
                    table[y][x] = 0

        return False

    solve_board(0,0,1)

    return table

