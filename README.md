# Sudokuprogram:
* Originally a purely console based UI, ported to a GUI using pygame.
Trying to keep some of my functions and algorithms functionable
across the port, led to a lot of spaghetticode which im not proud of.
While this was more of a challenge to see if I was able to do this, I might go back
to clean it up. But for now, it is what it is, and it works pretty well.
* If you want to look into the code, I have not commented the files and the 
program was written as a test for a visual solving-algorithm. I also tested 
the use of object-oriented solutions for my gameboard, which led to
to a miss-mash of methods and classmethods. 

### How to set up:

* Requires Python version 3.9 or newer (as of 03.02.2021)
 and ability to import the pygame-library
* All gamefiles must lie in same folder
### How to use:
* Open and run the play_game.py-file. If set up correctly the program should start :)
* Saving a board requires you to type the boardname in the console.
Havent implemented a visual way yet (might later)
* Saving a board requires you to end the filename with ".txt"
Eks: my_game_board.txt
## Note:
* The program is very specific in which sudoku-boards it can read. 
View the examplefile if you wish to play your own board.
* I do not know how to spell suduko, so bear with me if you look in to the code