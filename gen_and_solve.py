import random
from legalmoves import *
import time


def gen_filled_board():
    time1 = time.perf_counter()

    table = []
    for i in range(9):
        table.append([0,0,0,0,0,0,0,0,0])

    global failed_attempts
    failed_attempts = 0

    def gen_table(x,y,ok):
        global failed_attempts
        if x == 9:
            if y == 8:
                return True
            else:
                y += 1
                x = 0

        run = True
        li = [1,2,3,4,5,6,7,8,9]

        while run:
            if failed_attempts > 10000:
                return False

            if len(li) == 0:
                failed_attempts += 1
                return False
            else:
                int = li.pop(random.randint(0, len(li)-1))

            if is_legal_move(x,y,int, table):
                table[y][x] = int
                if gen_table(x+1,y, ok):
                    return True
                else:
                    table[y][x] = 0
        return False

    while not gen_table(0,0,1):
        failed_attempts = 0
        table = []
        for i in range(9):
            table.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    return table

