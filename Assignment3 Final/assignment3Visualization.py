import numpy as np
import random
import datetime
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument("-si", "--size", help="Enter size of the board", type=int)
    parser.add_argument("-st", "--state", help="Please enter the state", type=int)
    parser.add_argument("-ts", "--time_steps", help="Enter time steps to run the program", type=int)

    args = parser.parse_args()


    size = args.size
    states = args.state
    time_steps = args.time_steps
    
    object_three = GameofLifeThree(size)

    if states == 3:
        gridBoard = object_three.random()
    elif states == 1:
        gridBoard = object_three.blinker()
    elif states == 2:
        gridBoard = object_three.glider()
    elif states == 4:
        gridBoard = object_three.personal()
    else:
        print("Sorry no pattern selected")

    t1= datetime.datetime.now() #Gives initial time when the simulation starts
    


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



    t2 = datetime.datetime.now()
    diff = t2.second - t1.second


    # Shows a graph of all the process30es carried out
    print("\n\n\n STATISTICS OF THE RUN \n =====================")
    print("Start time:", t1)
    print("End time:", t2)
    print("Total Duration:", diff*1000, "milliseconds")
    print("Total Alive:", alive)
    print("Total Dead:", dead)
    print("Number of frames processed", time_steps / diff)
 