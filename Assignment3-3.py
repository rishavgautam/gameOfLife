import numpy as np
import random
import datetime
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from soupsieve import select



class GameofLife(object):
    def __init__(self, size):
        self.columns = int(size)
        self.rows = int(size)
        self.size = size
        # self.grid_array = [[0 for i in range(self.rows)] for j in range(self.columns)] #creating list of lists
        # self.grid_array = np.random.choice([0,1], (size, size))
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


    def simulation(self, grid):
        rows = 0
        cols = 0
    
        def neighbor_fn(item):
            nonlocal rows, cols, grid
            neighbor = self.get_neighbors(rows, cols)
            cols += 1
            if(cols % size == 0):
                rows += 1
                cols = 0
            return neighbor

        neighbors  = np.array(list(map(neighbor_fn, range(size ** 2))))
        grid_vec = grid.reshape(size ** 2)

        newly_born = (neighbors == 3) & (grid_vec == 0)
        survived = ((neighbors == 2) | (neighbors == 3)) & grid_vec == 1

        new_grid = np.full(size ** 2, 0)
        new_grid[newly_born | survived] = 1
        self.ticks +=1
        return new_grid.reshape((size, size))

    
    def getTicks(self):
        return self.ticks
    
    
    def get_neighbors(self, x, y):
        board = grid
        top = (x - 1) % size
        bottom = (x + 1) % size
        left = (y - 1) % size
        right = (y + 1) % size

        neighbors = board[top][left]    + board[top][y]    + board[top][right] + \
                    board[x][left]      +                              board[x][right] + \
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
    
    object = GameofLife(size)

    if states == 3:
        grid = object.random()
    elif states == 1:
        grid = object.blinker()
    elif states == 2:
        grid = object.glider()
    elif states == 4:
        grid = object.personal()
    else:
        print("Sorry no pattern selected")

    t1= datetime.datetime.now() #Gives initial time when the simulation starts
    
    
    

        
    def animate(frameNum):
        alive = 0
        dead = 0
        global grid, im
        grid = object.simulation(grid)
        im.set_data(grid)

        if object.getTicks() > time_steps:
            plt.close()

        alive += object.getAlive()
        dead += object.getDead()
        return [mat], alive, dead


    fig, ax = plt.subplots()
    mat = ax.matshow(grid)
    im = plt.imshow(grid, cmap ='Blues')

    data, alive, dead = animate(1)

    _ = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()

    # def plotData(d):
    #     alive = 0
    #     dead = 0
    #     dataFromBoard = object.conway_assignment_two()
    #     mat.set_data(dataFromBoard)
    #     im.set_data(dataFromBoard)
    #     if object.getTicks() > time_steps:
    #         plt.close()

    #     alive += object.getAlive()
    #     dead += object.getDead()
    #     return [mat], alive, dead
    
    # grid, alive, dead = plotData(1)
    

    # asd = animation.FuncAnimation(fig, plotData, interval=50, save_count=50)
    # plt.show()

    t2 = datetime.datetime.now() #Final time when the simulation ends after N time steps
    t_1 = t1.timestamp() 
    t_2 = t2.timestamp()
    diff = t_2-t_1


    # Shows a graph of all the process30es carried out
    print("\n\n\n STATISTICS OF THE RUN \n =====================")
    print("Start time:", t1)
    print("End time:", t2)
    print("Total Duration:", diff*1000, "milliseconds")
    print("Total Alive:", alive)
    print("Total Dead:", dead)
    print("Number of frames processed", time_steps / diff)
 