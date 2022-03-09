import numpy as np
import random
import datetime
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from soupsieve import select



class GameofLife(object):
    def __init__(self, width, height):
        self.columns = int(height)
        self.rows = int(width)
        self.size = (self.rows, self.columns)
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
    def conway_assignment_three(self):
        next = np.ndarray(shape=(self.size))
        
        #If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
        #If the cell is dead, then it springs to life only in the case that it has 3 live neighbors
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                
                neighbours = self.findNeighbors_three(x, y)
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
    x = int(input("Enter size of the board: "))
    states = int(input("Please enter state type \n 1. Blinker \n 2. Glider Gun \n 3. Random \n 4. Personal \n Please enter your choice: "))
    time_steps = int(input("Please enter number of steps to run the program: "))
    width = x
    height = x
    boardHistory = []
    
    object = GameofLife(width,height)

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


    def gridHistory():
        for i in range(0, time_steps+1):
            dataFromBoard = object.conway_assignment_three()
            boardHistory.append(dataFromBoard)
            return boardHistory

    gridHistory()


 