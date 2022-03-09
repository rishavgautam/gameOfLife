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
        self.grid_array = [[0 for i in range(self.rows)] for j in range(self.columns)] #creating list of lists
        
        
        
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
        
    def getTicks(self):
        return self.ticks

    # Find neighbors of the alive cell and check if they are alive or not
    def findNeighbors_two(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]
        total -= self.grid_array[x][y]
        return total


    def findNeighbors_three(self, x, y):
        top = (x - 1) % self.rows
        bottom = (x + 1) % self.rows
        left = (y - 1) % self.columns
        right = (y + 1) % self.columns

        neighbors = self.grid_array[top][left]    + self.grid_array[top][y]    + self.grid_array[top][right] + \
                    self.grid_array[x][left]      +                              self.grid_array[x][right] + \
                    self.grid_array[bottom][left] + self.grid_array[bottom][y] + self.grid_array[bottom][right]
        return neighbors

    # Gets total count of alive cell
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
    
    fig, ax = plt.subplots()
    mat = ax.matshow(grid)
    im = plt.imshow(grid, cmap ='Blues')


    def gridHistory():
        for i in range(0, time_steps+1):
            dataFromBoard = object.conway_assignment_two()
            boardHistory.append(dataFromBoard)

    def plotData(d):
        alive = 0
        dead = 0
        dataFromBoard = object.conway_assignment_two()
        mat.set_data(dataFromBoard)
        im.set_data(dataFromBoard)
        if object.getTicks() > time_steps:
            plt.close()

        alive += object.getAlive()
        dead += object.getDead()
        return [mat], alive, dead
    
    data, alive, dead = plotData(1)
    

    asd = animation.FuncAnimation(fig, plotData, interval=50, save_count=50)
    plt.show()

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
 