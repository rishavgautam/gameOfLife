import numpy as np
import random
import matplotlib.pyplot as plt 
from matplotlib import style
import time


class GameofLifeTwo(object):
    def __init__(self, size):
        self.columns = int(size)
        self.rows = int(size)
        self.size = size
        self.grid_array = [[0 for i in range(self.rows)] for j in range(self.columns)] #creating list of lists
        
    def random(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
                self.grid_array[x][y] = np.random.choice((0,1), p=[0.5, 0.5])
        return self.grid_array

    def blinker(self):
        self.grid_array[10][10] = 1
        self.grid_array[10][11] = 1
        self.grid_array[10][12] = 1
        return self.grid_array


    def glider(self):
        self.grid_array[4][3] = 1
        self.grid_array[5][4] = 1
        self.grid_array[5][5] = 1
        self.grid_array[4][5] = 1
        self.grid_array[3][5] = 1
        return self.grid_array

    
    def personal(self):
        self.grid_array[1][0] = 1
        self.grid_array[2][1] = 1
        self.grid_array[2][2] = 1
        self.grid_array[1][2] = 1
        self.grid_array[0][2] = 1
        self.grid_array[3][2] = 1
        return self.grid_array



    #Main logic of the program.
    def conway_assignment_two(self, x):
        self.grid_array = x
        next = np.ndarray(shape=(self.rows, self.columns))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.findNeighbors_two(x, y)
                
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next
        return self.grid_array


    def findNeighbors_two(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]
        total -= self.grid_array[x][y]
        return total
    
    

class GameofLifeThree(object):
    def __init__(self, size):
        self.columns = int(size)
        self.rows = int(size)
        self.size = size
        self.grid_array = np.full((size, size), 0)
        
    def random(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
        return self.grid_array

    def blinker(self):
        self.grid_array[10][10] = 1
        self.grid_array[10][11] = 1
        self.grid_array[10][12] = 1
        return self.grid_array


    def glider(self):
        self.grid_array[4][3] = 1
        self.grid_array[5][4] = 1
        self.grid_array[5][5] = 1
        self.grid_array[4][5] = 1
        self.grid_array[3][5] = 1
        return self.grid_array

    
    def personal(self):
        self.grid_array[1][0] = 1
        self.grid_array[2][1] = 1
        self.grid_array[2][2] = 1
        self.grid_array[1][2] = 1
        self.grid_array[0][2] = 1
        self.grid_array[3][2] = 1
        return self.grid_array



    def conway_assignment_three(self, grid_board):
        rows = 0
        cols = 0
    
        def neighbor_fn(item):
            nonlocal rows, cols, grid_board
            neighbor = self.get_neighbors(rows, cols)
            cols += 1
            if(cols % size == 0):
                rows += 1
                cols = 0
            return neighbor

        neighbors  = np.array(list(map(neighbor_fn, range(size ** 2))))
        grid_vec = grid_board.reshape(size ** 2)

        newly_born = (neighbors == 3) & (grid_vec == 0)
        survived = ((neighbors == 2) | (neighbors == 3)) & grid_vec == 1

        new_grid = np.full(size ** 2, 0)
        new_grid[newly_born | survived] = 1
        return new_grid.reshape((size, size))

    
   
    
    
    def get_neighbors(self, x, y):
        board = gridBoard
        top = (x - 1) % size
        bottom = (x + 1) % size
        left = (y - 1) % size
        right = (y + 1) % size

        neighbors = board[top][left]    + board[top][y]    + board[top][right] + \
                    board[x][left]      +                    board[x][right] + \
                    board[bottom][left] + board[bottom][y] + board[bottom][right]
        return neighbors



if __name__ == '__main__':
    
    size = 750
    states = 3
    time_steps = 100

    boardHistory = []
    object_two = GameofLifeTwo(size)
    object_three = GameofLifeThree(size)


    if states == 3:
        grid = object_two.random()
        gridBoard = object_three.random()
    
    assignment2 = []
    assignment3 = []
    boardSize = []
    
    for j in range(4):
        size += 250
        boardSize.append(size)
        object_two = GameofLifeTwo(size)
        object_three = GameofLifeThree(size)

        if states == 3:
            grid = object_two.random()
            gridBoard = object_three.random()

        t1 = time.time()

        dataFromBoard = grid

        for i in range(time_steps):
            dataFromBoard = object_two.conway_assignment_two(dataFromBoard)
        
    
        t2 = time.time()

        diff = (t2-t1)*1000
        timePlot = time_steps/diff
        assignment2.append(timePlot)



        t3 = time.time()

        for i in range(time_steps):
            gridBoard = object_three.conway_assignment_three(gridBoard)        
        
        t4 = time.time()

        diff = ((t4-t3))*1000
        timePlot2 = time_steps/diff
        assignment3.append(timePlot2)


    

    style.use('seaborn')
    plt.figure(figsize=(12, 7))
    plt.plot(boardSize, assignment2, label="Using Iteration", marker='D')
    plt.plot(boardSize, assignment3, label="Without Iteration", marker='D')
    plt.title('Speed comparison between using iteration method vs non iteration method')
    plt.xlabel('Screen Size')
    plt.ylabel('Time steps/milliseconds')
    plt.legend()
    plt.savefig("./speedComparison.png")
    plt.show()