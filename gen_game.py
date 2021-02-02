import random


def gen_game(table, difficulty):
    if difficulty > 10:
        difficulty = 10
    elif difficulty < 1:
        difficulty = 1

    for i in table:
        for t in range(len(i)):
            if 1 == random.randint(1, 12 - difficulty):
                i[t] = 0
    return table
