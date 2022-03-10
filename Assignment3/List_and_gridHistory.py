import numpy as np
import random
import matplotlib.pyplot as plt 
import matplotlib.animation as animation



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
    
   
    
if __name__ == '__main__':
    size = int(input("Enter size of the board: "))
    states = int(input("Please enter state type \n 1. Blinker \n 2. Glider Gun \n 3. Random \n 4. Personal \n Please enter your choice: "))
    time_steps = int(input("Please enter number of steps to run the program: "))
    boardHistory = []
    historyRequired = False
    
    object_two = GameofLifeTwo(size)

    if states == 3:
        grid = object_two.random()
    elif states == 1:
        grid = object_two.blinker()
    elif states == 2:
        grid = object_two.glider()
    elif states == 4:
        grid = object_two.personal()
    else:
        print("Sorry no pattern selected")    
    

    def gridHistory():
        if historyRequired:
            for i in range(0, time_steps+1):
                dataFromBoard = object_two.conway_assignment_two()
                boardHistory.append(dataFromBoard)
                return boardHistory
        else:
            return 0

    
    print(gridHistory())


    
 