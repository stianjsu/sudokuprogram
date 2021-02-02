import pygame
import time
import copy
from gen_and_solve import *
from get_game import *
from legalmoves import *
from other_functions import *

pygame.init()

def assign_sudoku_class(list):
    dict = {}
    for y in range(len(list)):
        for x in range(len(list[y])):
            dict[(x, y)] = sudokuClass(x,y,list[y][x], (255,255,255), x//3+1, y//3+1)
    return dict

def get_key_pressed(e):
    if e.key == pygame.K_1:
        return 1
    if e.key == pygame.K_2:
        return 2
    if e.key == pygame.K_3:
        return 3
    if e.key == pygame.K_4:
        return 4
    if e.key == pygame.K_5:
        return 5
    if e.key == pygame.K_6:
        return 6
    if e.key == pygame.K_7:
        return 7
    if e.key == pygame.K_8:
        return 8
    if e.key == pygame.K_9:
        return 9
    if e.key == pygame.K_0:
        return 0
    return ""

def find_solution(table):
    time1 = time.perf_counter()
    global failed_counter
    failed_counter = 0

    def solve_board(x, y):
        global failed_counter
        failed_counter = failed_counter
        if x == 9:
            if y == 8:
                return True
            else:
                y += 1
                x = 0
        game_boardClass[(x, y)].color = lightblue
        update_display()
        if 0.0001 < 0.05 - 0.0005*(failed_counter//10):
            time.sleep(max(0.05 - 0.0005*(failed_counter//10), 0.0001))

        if in_unsolved_spaces(x,y,unsolved_spaces):
            if table[y][x] != 0:
                if is_legal_move(x,y,table[y][x],table):
                    game_boardClass[(x, y)].color = green
                    update_display()
                    if solve_board(x+1,y):
                        return True
        else:
            game_boardClass[(x, y)].color = green
            update_display()
            if solve_board(x + 1, y):
                return True
            game_boardClass[(x, y)].color = (200, 0, 0)
            return False

        for i in range(1,10):
            if is_legal_move(x,y,i, table):
                game_boardClass[(x,y)].color = green
                game_boardClass[(x,y)].value = i
                table[y][x] = i
                update_display()
                if solve_board(x+1,y):
                    return True
                else:
                    game_boardClass[(x, y)].value = 0
                    table[y][x] = 0
        game_boardClass[(x,y)].color = (200,0,0)
        failed_counter += 1
        return False

    solve_board(0,0)
    print(time.perf_counter()-time1)
    return table

def save_board_to_file():
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


class sudokuClass:
    def __init__(self, x, y, value, color, xmargin, ymargin):
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.posX = 2 + (2 + 90) * x + 6*xmargin
        self.posY = 2 + (2 + 90) * y + 6*ymargin
        if value == 0:
            self.startUnsolved = True
            self.unknownbox = pygame.Rect(self.posX, self.posY, 90, 90)
            self.box = pygame.Rect(self.posX+4, self.posY+4, 82, 82)
        else:
            self.startUnsolved = False
            self.box = pygame.Rect(self.posX, self.posY, 90, 90)

    def change_value(self, newvalue):
        self.value = newvalue

    def change_color(self, color):
        self.color = color

    def draw(self):
        if self.value == 0:
            text = font.render("", True, black, self.color)
        else:
            text = font.render(str(self.value), True, black, self.color)
        if(self.startUnsolved):
            pygame.draw.rect(display_surface, lightblue, self.unknownbox)
            pygame.draw.rect(display_surface, self.color, self.box)
            display_surface.blit(text, ((2 * self.posX + 90) // 2 - 8, (2 * self.posY + 90) // 2 - 8))
        else:
            pygame.draw.rect(display_surface, self.color, self.box)
            display_surface.blit(text, ((2*self.posX+90)//2 - 8, (2*self.posY+90)//2 - 8))

class button:
    def __init__(self, x, y, w, h, color, hovercolor, text, fontsize = 32):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.hovercolor = hovercolor
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', fontsize)

    def draw(self,win,pos=""):
        if pos !="" and self.hover(pos):
            pygame.draw.rect(win, self.hovercolor, (self.x, self.y, self.w, self.h),border_radius=10)
            text = self.font.render(self.text, self.hovercolor, black)
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h), border_radius=10)
            text = self.font.render(self.text, self.color, black)

        win.blit(text,
                 (self.x + (self.w / 2 - text.get_width() / 2), self.y + (self.h / 2 - text.get_height() / 2)))


    def hover(self, pos):
        if self.x < pos[0] and self.x + self.w > pos[0] and self.y < pos[1] and self.y + self.h > pos[1]:
            return True
        return False

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
lightblue = (135,206,235)
font = pygame.font.Font('freesansbold.ttf', 32)

X = 810 + 44 + 300
Y = 810 + 44

display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Sudoku')
display_surface.fill(black)


startbuttons = {
    "spmbox": button(350, 284, 500, 90, white, white, "Do you have a pre-made board?"),
    "yesbox": button(375, 450, 200, 90, white, lightblue, "Yes"),
    "nobox": button(625, 450, 200, 90, white, lightblue, "No"),
    "textfilespm": button(210,284,X-2*210,90,white,white, "Type the name of your textfile: (board.text)"),
    "textfileansw": button(210, 450, X-2*210, 90, white, white, ""),
    "difficultyspm": button(210, 284, X-2*210, 90, white, white, "Type difficulty from 0 to 9, where 9 is hardest"),
}


answered = False


while not answered:
    display_surface.fill(black)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            answered = True
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startbuttons["yesbox"].hover(pos):
                haspremade = True
                answered = True
            elif startbuttons["nobox"].hover(pos):
                haspremade = False
                answered = True

    startbuttons["spmbox"].draw(display_surface, pos)
    startbuttons["yesbox"].draw(display_surface, pos)
    startbuttons["nobox"].draw(display_surface, pos)

    pygame.display.flip()


if haspremade:
    difficulty = None
    givenfilename = False
    while not givenfilename:
        display_surface.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                givenfilename = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textfilename = startbuttons["textfileansw"].text
                    givenfilename = True
                elif event.key == pygame.K_BACKSPACE:
                    startbuttons["textfileansw"].text = startbuttons["textfileansw"].text[:-1]
                else:
                    startbuttons["textfileansw"].text += event.unicode

        startbuttons["textfilespm"].draw(display_surface)
        startbuttons["textfileansw"].draw(display_surface)

        pygame.display.flip()

    difficulty = None
    board = get_premade(difficulty, textfilename)

else:

    given_difficulty = False
    while not given_difficulty:
        display_surface.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                given_difficulty = True
                quit()
            if event.type == pygame.KEYDOWN:
                if (a := get_key_pressed(event)) != "":
                    given_difficulty = True
                    difficulty = int(a)

        startbuttons["difficultyspm"].draw(display_surface)
        pygame.display.flip()

    board = get_premade(difficulty)


unsolved_spaces = find_unsolved_spaces(board)
game_board = []
for i in board:
    game_board.append(i[:])
game_boardClass = assign_sudoku_class(game_board)

print(game_boardClass)

main_buttons = {
    "save_board":  button(895,   Y//5, 230, 90, white, lightblue, "Save board to file", 24),
    "reset_board":  button(895, 2*Y//5, 230, 90, white, lightblue, "Reset the board", 24),
    "solve_board": button(895, 3*Y//5, 230, 90, white, lightblue, "A.I. solve", 24),
    "quit": button(895, 4*Y//5, 230, 90, white, lightblue, "Quit Game", 24),
}


run = True
selectedbox = ''
prevselectedbox = ''

def update_display():

    for t in game_boardClass:

        game_boardClass[t].draw()

    for j in main_buttons:
        main_buttons[j].draw(display_surface,pos)

    pygame.display.flip()


solved = False
while run:
    display_surface.fill(black)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_buttons["solve_board"].hover(pos):
                find_solution(game_board)
                solved = True
            elif main_buttons["reset_board"].hover(pos):
                game_board = []
                for i in board:
                    game_board.append(i[:])
                game_boardClass = assign_sudoku_class(game_board)
                solved = False
            elif main_buttons["quit"].hover(pos):
                run = False
            elif main_buttons["save_board"].hover(pos):
                save_board_to_file()
                run = False

            else:
                for i in game_boardClass:
                    if game_boardClass[i].box.collidepoint(event.pos):
                        if in_unsolved_spaces(i[0],i[1],unsolved_spaces):
                            if selectedbox == i:

                                selectedbox = ''
                                prevselectedbox = i

                            else:

                                prevselectedbox = selectedbox[:]
                                selectedbox = i

        if selectedbox != '' and event.type == pygame.KEYDOWN:
            if (a := get_key_pressed(event)) != "":
                game_boardClass[selectedbox].change_value(int(get_key_pressed(event)))
                game_board[selectedbox[1]][selectedbox[0]] = int(get_key_pressed(event))
    try:
        game_boardClass[selectedbox].change_color(green)
    except:
        pass
    try:
        game_boardClass[prevselectedbox].change_color(white)
    except:
        pass

    # TODO Gjør om til egen funksjon
    if has_unsolved_spaces(game_boardClass):
        finishedgametable = []
        for y in range(0,9):
            t_row = []
            for x in range(0,9):
                t_row.append(game_boardClass[(x, y)].value)
            finishedgametable.append(t_row)
        is_solved = True
        for y in range(0,9):
            for x in range(0,9):
                if not is_legal_move(x,y,finishedgametable[y][x],finishedgametable):
                    is_solved = False

        if is_solved:
            solved = True
            for key in game_boardClass:
                game_boardClass[key].color = green
            update_display()


    if not solved:
        update_display()



pygame.quit()



'''
print("Quit game without saving by typing command: 'quit'")
print("Delete number by typing command: 'delete'")
print("Show solution by typing command: 'solution'")
print("Reset board in this session by typing: 'reset'")
print("Save to file board by typing: 'save board'")
run = True
while run:
    print_table(game_board)
    inp = input("Place number: row(1-9), col(1,9), nr(1-9)")
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

'''
