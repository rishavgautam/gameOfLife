import numpy as np
import random
import datetime
import matplotlib.pyplot as plt 
import matplotlib.animation as animation



class GameofLifeTwo(object):
    def __init__(self, size):
        self.columns = int(size)
        self.rows = int(size)
        self.size = size
        self.grid_array = [[0 for i in range(self.rows)] for j in range(self.columns)] #creating list of lists
        self.ticks = 0
        
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
    def conway_assignment_two(self):
        next = np.ndarray(shape=(self.rows, self.columns))
        
        #If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
        #If the cell is dead, then it springs to life only in the case that it has 3 live neighbors
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
        self.ticks +=1
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
    
    def getTicks(self):
        return self.ticks
    

    def getAlive(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid_array[i][j]==1:
                    count +=1
        return count

    # Gets total count of dead cell
    def getDead(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid_array[i][j]==0:
                    count +=1
        return count






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
        self.ticks +=1
        return new_grid.reshape((size, size))

    
    def getTicks(self):
        return self.ticks
    
    
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



    def getAlive(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid_array[i][j]==1:
                    count +=1
        return count

    # Gets total count of dead cell
    def getDead(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid_array[i][j]==0:
                    count +=1
        return count






if __name__ == '__main__':
    size = int(input("Enter size of the board: "))
    states = int(input("Please enter state type \n 1. Blinker \n 2. Glider Gun \n 3. Random \n 4. Personal \n Please enter your choice: "))
    time_steps = int(input("Please enter number of steps to run the program: "))
    boardHistory = []
    historyRequired = False
    
    object_two = GameofLifeTwo(size)
    object_three = GameofLifeThree(size)

    if states == 3:
        grid = object_two.random()
        gridBoard = object_three.random()
    elif states == 1:
        grid = object_two.blinker()
        gridBoard = object_three.blinker()
    elif states == 2:
        grid = object_two.glider()
        gridBoard = object_three.glider()
    elif states == 4:
        grid = object_two.personal()
        gridBoard = object_three.personal()
    else:
        print("Sorry no pattern selected")

    t1= datetime.datetime.now() #Gives initial time when the simulation starts
    
    
    # Assignment two

    fig, ax = plt.subplots()
    mat = ax.matshow(grid)
    im = plt.imshow(grid, cmap ='Blues')
    ax.set_title('Conway Assignment Two')

    def plotData(d):
        alive = 0
        dead = 0
        dataFromBoard = object_two.conway_assignment_two()
        mat.set_data(dataFromBoard)
        im.set_data(dataFromBoard)
        if object_two.getTicks() > time_steps:
            plt.close()

        alive += object_two.getAlive()
        dead += object_two.getDead()
        return [mat], alive, dead
    
    

    asd = animation.FuncAnimation(fig, plotData, interval=50)

    def visualize(frameNum):
        alive = 0
        dead = 0
        global gridBoard, im
        gridBoard = object_three.conway_assignment_three(gridBoard)
        im1.set_data(gridBoard)

        if object_three.getTicks() > time_steps:
            plt.close()

        alive += object_three.getAlive()
        dead += object_three.getDead()

        return [mat1], alive, dead


    fig1, ax1 = plt.subplots()
    mat1 = ax1.matshow(gridBoard)
    im1 = plt.imshow(gridBoard, cmap ='Blues')
    ax1.set_title('Conway Assignment Three')
    data, alive, dead = visualize(1)

    _ = animation.FuncAnimation(fig1, visualize, interval=50)


    plt.show()


 