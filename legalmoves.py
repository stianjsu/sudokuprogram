def check_row(colnr, rownr, nr, table):
    for i in range(9):
        if table[rownr][i] == nr and colnr != i:
            return False
    return True


def check_col(colnr, rownr, nr, table):
    for i in range(9):
        if table[i][colnr] == nr and i != rownr:
            return False
    return True


def check_grid(colnr, rownr, nr, table):
    x = (colnr // 3) * 3
    y = (rownr // 3) * 3

    x_numbs = [x, x + 1, x + 2]
    y_numbs = [y, y + 1, y + 2]

    for i in y_numbs:
        for t in x_numbs:
            if table[i][t] == nr and i != rownr and i != colnr:
                return False
    return True


def is_legal_move(colnr, rownr, nr, table):
    if check_col(colnr, rownr, nr, table) and check_row(colnr, rownr, nr, table) and check_grid(colnr, rownr, nr, table):
        return True
    return False
