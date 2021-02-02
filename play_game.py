from gen_and_solve import *
from gen_game import *
from legalmoves import *
from other_functions import *

is_solved = False



if input("Do you have a pre-made board? (y/n)") == "y":

    f = open(input("Write filename with extencion: (board.txt)"), "r")
    lines = f.readlines()
    if input("Is your board already solved? (y/n) ") == "y":
        is_solved = True
    board = []
    for i in lines:
        inp_line = i.replace(" ", "").rstrip().split(",")
        new_line = []
        for t in inp_line:
            new_line.append(int(t))
        board.append(new_line)
    f.close()
else:
    is_solved = True
    board = gen_filled_board()

if is_solved:
    board = gen_game(board, int(input("Select difficulty: (number between 1 - 10, where 10 is most difficult) ")))


print(board)

unsolved_spaces = find_unsolved_spaces(board)

game_board = []
for i in board:
    game_board.append(i[:])

run = True

print("Quit game without saving by typing command: 'quit'")
print("Delete number by typing command: 'delete'")
print("Show solution by typing command: 'solution'")
print("Reset board in this session by typing: 'reset'")
print("Save to file board by typing: 'save board'")

while run:
    print_table(game_board)
    inp = input("Place number: 'row,col,number' (row column and number must be between 1-9)")
    try:
        if inp.lower() == "quit":
            run = False

        elif inp.lower() == "reset":
            game_board = []
            for i in board:
                game_board.append(i[:])

        elif inp.lower() == "solution":
            run = False
            print_table(find_solution(game_board))

        elif inp.lower() == "delete":
            deletenumb = input("Delete number: row(1-9), col(1,9)")
            deletenumb = deletenumb.replace(" ", "").split(",")
            deletepos = []
            for t in deletenumb:
                deletepos.append(int(t))

            game_board[deletepos[0]-1][deletepos[1]-1] = 0

        elif inp.lower() == "save board":
            f = open(input("Type filename where you want to save: (board.txt)"), "w")

            for i in range(len(game_board)-1):
                write_line = ""
                for t in range(len(game_board[i])-1):
                    write_line += f"{game_board[i][t]}, "
                write_line += f"{game_board[i][len(game_board[i])-1]}\n"
                f.write(write_line)
            write_line = ""
            for u in range(len(game_board[8])-1):
                write_line += f"{game_board[8][u]}, "
            write_line += f"{game_board[8][len(game_board[8]) - 1]}"
            f.write(write_line)
            f.close()
            rune = False

        else:
            inp = inp.replace(" ", "").split(",")
            guess = []
            try:
                for t in inp:
                    guess.append(int(t))


                if is_legal_move(guess[1]-1, guess[0]-1, guess[2], game_board) and \
                        in_unsolved_spaces(guess[1]-1, guess[0]-1, unsolved_spaces):

                    game_board[guess[0]-1][guess[1]-1] = guess[2]
                else:
                    print("Illegal move, try again")

            except:
                print("Write numbers between 1 and 9")

            if len(find_unsolved_spaces(game_board)) == 0:
                run = False
                print("You did it! So proud of you :D")

    except:
        print("Unknown input. Try again")