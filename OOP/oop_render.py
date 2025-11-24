import sdl2
class render:
    def __init__(self,renderer,grid,font_manager,tile_size,window_height):
        self.renderer = renderer
        self.grid = grid
        self.font_manager = font_manager
        self.tile_size = tile_size
        self.window_height = window_height
    def draw_grid(self):
        self.renderer.clear()
        for x, y in self.grid.active_cells:
            age = self.grid.cells[y][x].time_alive * 5
            if age > 255:
                age = 255
            self.renderer.fill((x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size),sdl2.ext.Color(255-age, 255-age, 255))
        for x in range(self.grid.width + 1):
            self.renderer.draw_line((x * self.tile_size, 0, x * self.tile_size, self.window_height),sdl2.ext.Color(40, 40, 40))
        for y in range(self.grid.height + 1):
            self.renderer.draw_line((0, y * self.tile_size, self.grid.width * self.tile_size, y * self.tile_size),sdl2.ext.Color(40, 40, 40)) 