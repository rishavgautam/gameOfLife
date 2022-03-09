import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size = 200

rows, cols = 0, 0


def get_neighbors(board, x, y):
    top = (x - 1) % size
    bottom = (x + 1) % size
    left = (y - 1) % size
    right = (y + 1) % size

    neighbors = board[top][left]    + board[top][y]    + board[top][right] + \
                board[x][left]      +                              board[x][right] + \
                board[bottom][left] + board[bottom][y] + board[bottom][right]
    return neighbors



def simulation(grid):
    rows = 0
    cols = 0

    def neighbor_fn(item):
        nonlocal rows, cols, grid
        neighbor = get_neighbors(grid, rows, cols)
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
    return new_grid.reshape((size, size))


# print(grid_array)

# glider
grid = np.full((size, size), 0)

grid[0][0] = 1
grid[1][1] = 1
grid[1][2] = 1
grid[2][0] = 1
grid[2][1] = 1


# grid = np.random.choice([0,1], (size, size))

def animate(frameNum):
    global grid,img
    grid = simulation(grid)
    img.set_data(grid)


fig, ax = plt.subplots()
img = plt.imshow(grid, cmap ='Blues')


_ = FuncAnimation(fig, animate, interval=10)
plt.show()
