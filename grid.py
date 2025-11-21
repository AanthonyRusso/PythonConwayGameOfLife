from cell import Cell
import random
import sys
import time
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
    def step(self):
        new_state = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                neighbors = self.check_neighbors(x,y)
                alive_neighbors = 0
                for neighbor in neighbors:
                    if neighbor.is_alive:
                        alive_neighbors += 1
                if self.cells[y][x].is_alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_state[y][x].is_alive = False
                    else:
                        new_state[y][x].is_alive = True
                else:
                    if alive_neighbors == 3:
                        new_state[y][x].is_alive = True
        self.cells = new_state
    def check_neighbors(self,x,y):
        neighbors = []
        for i in range (-1,2):
            for j in range (-1,2):
                if i == 0 and j == 0:
                    continue
                dx = x + i
                dy = y + j
                if 0 <= dx < self.width and 0 <= dy < self.height:
                    neighbors.append(self.cells[dy][dx])
        return neighbors
    def randomize(self, probability=0.5):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[y][x].is_alive = random.random() < probability
    def clear(self):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[y][x].is_alive = False

if __name__ == "__main__":

    num_steps = 1

    if len(sys.argv) > 1:
        num_steps = int(sys.argv[1])

    grid = Grid(20,20)
    grid.cells[9][10].is_alive = True
    grid.cells[10][10].is_alive = True
    grid.cells[11][10].is_alive = True
    grid.cells[11][9].is_alive = True
    grid.cells[10][8].is_alive = True
    for row in grid.cells:
        print("".join(['█' if cell.is_alive else ' ' for cell in row]))
    time.sleep(.5)

    for _ in range(num_steps):
        print("\nNext Generation:\n")
        grid.step()
        for row in grid.cells:
            print("".join(['█' if cell.is_alive else ' ' for cell in row]))
        time.sleep(.5)
    