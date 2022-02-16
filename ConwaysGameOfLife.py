import pygame
import numpy as np
import random
import datetime
import time

class GameofLife(object):
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)

    def blinker(self):
        self.grid_array[3][3] = 1
        self.grid_array[3][4] = 1
        self.grid_array[3][5] = 1

    def glider(self):
        self.grid_array[4][3] = 1
        self.grid_array[5][4] = 1
        self.grid_array[5][5] = 1
        self.grid_array[4][5] = 1
        self.grid_array[3][5] = 1
    
    def personal(self):
        self.grid_array[1][0] = 1
        self.grid_array[2][1] = 1
        self.grid_array[2][2] = 1
        self.grid_array[1][2] = 1
        self.grid_array[0][2] = 1
        self.grid_array[3][2] = 1

    #Main logic of the program. Assigns whether a 
    def plotDataInBoard(self, alive_color, inactive_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, alive_color, [x_pos, y_pos, 
                    self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, inactive_color, [x_pos, y_pos, 
                    self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        
        #List of list
        #If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
        #If the cell is dead, then it springs to life only in the case that it has 3 live neighbors
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.findNeighbors(x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next

    # Find neighbors of the alive cell and check if they are alive or not
    def findNeighbors(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]
        total -= self.grid_array[x][y]
        return total

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
    x = int(input("Enter size of the board (>300): "))
    states = int(input("Please enter state type \n 1. Blinker \n 2. Glider Gun \n 3. Random \n 4. Personal \n Please enter your choice: "))
    time_steps = int(input("Please enter number of steps to run the program: "))

    width = x
    height = x
    size = (width, height)

    pygame.init()
    pygame.display.set_caption("Game of Life")
    screen = pygame.display.set_mode(size)

    black = (0, 0, 0)
    blue = (65,105,225)
    white = (255, 255, 255)

    scaler = 9
    offset = 0
    object = GameofLife(width,height, scaler, offset)

    if states == 3:
        object.random()
    elif states == 1:
        object.blinker()
    elif states == 2:
        object.glider()
    elif states == 4:
        object.personal()
    else:
        print("Sorry no pattern selected")

    run = True
    t1= datetime.datetime.now() #Gives initial time when the simulation starts
    ticks = 0
    alive = 0
    dead = 0
    while (ticks<time_steps):
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        object.plotDataInBoard(alive_color=blue, inactive_color=black, surface=screen)
        pygame.display.update()
        ticks +=1
        alive += object.getAlive()
        dead += object.getDead()
        time.sleep(0.06)

    t2 = datetime.datetime.now() #Final time when the simulation ends after N time steps
    pygame.quit()
    t_1 = t1.timestamp() * 1000
    t_2 = t2.timestamp() * 1000
    
    #Shows a graph of all the processes carried out
    print("\n\n\n STATISTICS OF THE RUN \n =====================")
    print("Start time:", t1)
    print("End time:", t2)
    print("Total Duration:", t_2-t_1, "milliseconds")
    print("Total Alive:", alive)
    print("Total Dead:", dead)
    print("Number of frames processed", ticks)