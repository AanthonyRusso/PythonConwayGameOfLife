from OOP.cell import Cell
import random
import sys
import time
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
        self.active_cells = set()
    def step(self):
        new_active_cells = set()
        candidates = set()
        next_state = {}

        for x, y in self.active_cells:
            for i in range(-1, 2):  
                for j in range(-1, 2):
                    dx = x + i
                    dy = y + j
                    if 0 <= dx < self.width and 0 <= dy < self.height:
                        candidates.add((dx, dy))
        for x,y in candidates:
            neighbors = self.check_neighbors(x,y)
            alive_neighbors = 0
            for neighbor in neighbors:
                if neighbor.is_alive:
                    alive_neighbors += 1
            if self.cells[y][x].is_alive:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    next_state[(x, y)] = False
                else:
                    next_state[(x, y)] = True
                    new_active_cells.add((x, y))
            else:
                if alive_neighbors == 3:
                    next_state[(x, y)] = True
                    new_active_cells.add((x, y))
                else:
                    next_state[(x, y)] = False
        for (x, y), state in next_state.items():
            if self.cells[y][x].is_alive == True:
                if state == True:
                    self.cells[y][x].time_alive += 1
                else:
                    self.cells[y][x].time_alive = 0
            self.cells[y][x].is_alive = state
        self.active_cells = new_active_cells
    def add_active_cell(self, x, y):
        if (x,y) not in self.active_cells:
            self.active_cells.add((x,y))
    def remove_active_cell(self, x, y):
        self.cells[y][x].time_alive = 0
        if (x,y) in self.active_cells:
            self.active_cells.discard((x,y))
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
        self.clear()
        for x in range(self.width):
            for y in range(self.height):
                self.cells[y][x].is_alive = random.random() < probability
                if self.cells[y][x].is_alive:
                    self.add_active_cell(x,y)
    def clear(self):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[y][x].is_alive = False
                self.cells[y][x].time_alive = 0
        self.active_cells = set()

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
    for x, y in [(10, 9), (10, 10), (10, 11), (9, 11), (8, 10)]:
        grid.add_active_cell(x, y)
    for row in grid.cells:
        print("".join(['█' if cell.is_alive else ' ' for cell in row]))
    time.sleep(.5)

    for _ in range(num_steps):
        print("\nNext Generation:\n")
        grid.step()
        for row in grid.cells:
            print("".join(['█' if cell.is_alive else ' ' for cell in row]))
        time.sleep(.5)
    