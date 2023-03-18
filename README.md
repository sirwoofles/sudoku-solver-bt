# sudoku-solver-bt
Solving a sudoku puzzle using backtracking method

From an initial state, expand to state1 and to state 2.
At state2, before generating successors, check for constraint violations. If yes, backtrack to try something else

The rules of a sudoku puzzle are as follows:

1. for any given row, a digit 1-9 can only appear once
2. for any given coloumn, a digit 1-9 can only appear once
3. for any given block, a digit 1-9 can only appear once

for this backtracking method, iterate to the first empty cell, fill in numbers starting from 1 to 9, after filling in 1, check if it violates any of the 3 rules of the game, 
if it doesn't, iterate to the next cell and repeat the same.
if at the end of the row, a dead end is reached, move back to the previous decision point(cell) and try the next digit. and continue.

repeat until end game is reached.

worst case scenario, there is 9 digits in every cell to explore. therefore for m number of unfilled cells.
time complexity is O(9^m)