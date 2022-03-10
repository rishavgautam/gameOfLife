import numpy as np
import random
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument("-si", "--size", help="Enter size of the board", type=int)
    parser.add_argument("-st", "--state", help="Please enter the state", type=int)
    parser.add_argument("-ts", "--time_steps", help="Enter time steps to run the program", type=int)
    parser.add_argument('--feature', "--board_history", default=False, action='store_true')
    args = parser.parse_args()
    
    size = args.size
    states = args.state
    time_steps = args.time_steps


    boardHistory = []
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
        for i in range(time_steps):
            dataFromBoard = object_two.conway_assignment_two()
            boardHistory.append(dataFromBoard)
        return boardHistory
       

    if args.feature:
        print(gridHistory())
    else:
        print(0)


    
 