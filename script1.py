import numpy as np
import random
import datetime
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


class GameofLifeThree(object):
    def __init__(self, size):
        self.columns = int(size)
        self.rows = int(size)
        self.size = size
        self.grid_array = np.full((size, size), 0)
        self.ticks = 0
        
    def random(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = np.random.choice((0,1), p=[0.5, 0.5])
                # self.grid_array[x][y] = random.randint(0,1)
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
        self.ticks +=1
        d = new_grid.reshape((size, size))
        alv = np.count_nonzero(d)
        non_alv = (size*size) - alv
    
        
        return new_grid.reshape((size, size)), alv, non_alv

    
    def getTicks(self):
        return self.ticks

    def getPopulation(self):
        alive = self.alv
        dead = self.non_alv
        return alive, dead
    
    
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
    size = 100
    time_steps = 50
    object_three = GameofLifeThree(size)
    gridBoard = object_three.random()
   
    
    t1= datetime.datetime.now() #Gives initial time when the simulation starts

    def visualize(frameNum):
        global gridBoard, im1
        alvx = []
        gridBoard, alv, nonAlv = object_three.conway_assignment_three(gridBoard)
        im1.set_data(gridBoard)
                
        if object_three.getTicks() > time_steps:
            plt.close()

        return alvx


    fig1, ax1 = plt.subplots()
    mat1 = ax1.matshow(gridBoard)
    im1 = plt.imshow(gridBoard, cmap ='Blues')
    ax1.set_title('Conway Assignment Three')
    
    _ = animation.FuncAnimation(fig1, visualize, interval=50)
    plt.show()

    t2 = datetime.datetime.now()
    diff = t2.second - t1.second

 