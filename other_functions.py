def print_table(table):
    for i in range(9):
        if i % 3 == 0:
            print("-------------------------")
        for t in range(9):
            if t % 3 == 0:
                print("|", end=" ")
            print(table[i][t], end=" ")
        print("|")
    print("-------------------------")


def find_unsolved_spaces(table):

    unsolved = []
    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[row][col] == 0:
                unsolved.append((col, row))
    return unsolved


def in_unsolved_spaces(col, row, unsolved):
    if (col, row) in unsolved:
        return True
    return False

def has_unsolved_spaces(dict):
    for key in dict:
        if dict[key].value == 0:
            return False
    return True



def in_hitbox(point, x,y,width):
    if x < point[0] < x + width:
        if y < point[1] < y + width:
            return True
    return False

