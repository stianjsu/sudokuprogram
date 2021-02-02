import random
from gen_and_solve import *


def gen_game(table, difficulty):
    if difficulty > 10:
        difficulty = 10
    elif difficulty < 1:
        difficulty = 1

    for i in table:
        for t in range(len(i)):
            if 4 >= random.randint(1, 14 - difficulty):
                i[t] = 0
    return table


def get_premade(difficulty, textfilename = ""):

    if textfilename != "":

        f = open(textfilename, "r")
        lines = f.readlines()

        board = []
        for i in lines:
            inp_line = i.replace(" ", "").rstrip().split(",")
            new_line = []
            for t in inp_line:
                new_line.append(int(t))
            board.append(new_line)
        f.close()
    else:
        board = gen_game(gen_filled_board(),difficulty)


    return board

#if is_solved:
#    board = gen_game(board, int(input("Select difficulty: (number between 1 - 10, where 10 is most difficult) ")))
