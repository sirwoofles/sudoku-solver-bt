import time
start_time = time.time()

#starting sudoku grid with empty cells '0' and some pre-filled cells
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

import numpy as np
print('Unsolved puzzle =')
print(np.matrix(grid))
print()
#function check row, then coloumn, then block, if 'n' can be placed in that cell
def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for i in range(1,10):
                    if possible(y,x,i):
                        grid[y][x] = i
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))

print('Solved puzzle =')
solve()
print()
print("Process finished in:",time.time() - start_time,"seconds")