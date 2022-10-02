# Sudoku :

- Originally a purely console based UI, ported to a GUI using pygame.
  Directly porting the game with a GUI lead to rather unstructured code.
  While this was more of a challenge to see if I was able to do this, I might go back
  to clean it up. But for now it works pretty well.
- If you want to look into the code, I have not commented the files and the
  program was written as a test for a visual solving-algorithm. I also tested
  the use of object-oriented solutions for my gameboard, which led to
  to a miss-mash of methods and classmethods.

### How to set up:

- Requires Python version 3.9 or newer
  and pygame (pip install pygame)
- All saved gamefiles must be in root directory

### How to use:

- Open and run the play_game.py-file. If set up correctly the program should start
- Saving a board requires you to type the boardname in the console.
  Havent implemented a visual way yet
- Saving a board requires you to end the filename with ".txt"
  Eks: my_game_board.txt

## Note:

- The program is very specific in which sudoku-boards it can read.
  View the examplefile if you wish to play your own board.
- I didn't bother to learn how to spell sudoku
