import sdl2

class event_handler:
    def __init__(self, grid, tile_size):
        self.grid = grid
        self.tile_size = tile_size

    def handle_event(self, event):
        if event.type == sdl2.SDL_QUIT:
            return False
        elif event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_c:
                self.grid.clear()
            elif event.key.keysym.sym == sdl2.SDLK_r:
                self.grid.randomize(0.2)
        elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            x, y = event.button.x, event.button.y
            grid_x = x // self.tile_size
            grid_y = y // self.tile_size
            if 0 <= grid_x < self.grid.width and 0 <= grid_y < self.grid.height:
                if self.grid.cells[grid_y][grid_x].is_alive:
                    self.grid.remove_active_cell(grid_x, grid_y)
                else:
                    self.grid.add_active_cell(grid_x, grid_y)
                self.grid.cells[grid_y][grid_x].is_alive = not self.grid.cells[grid_y][grid_x].is_alive