import sdl2
import sdl2.ext
from grid import Grid
import sys


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


TILE_SIZE = 20





def main():

    grid_width = WINDOW_WIDTH // TILE_SIZE
    grid_height = WINDOW_HEIGHT // TILE_SIZE
    grid = Grid(grid_width, grid_height)
    grid.cells[9][10].is_alive = True
    grid.cells[10][10].is_alive = True
    grid.cells[11][10].is_alive = True
    grid.cells[11][9].is_alive = True
    grid.cells[10][8].is_alive = True
    for x, y in [(10, 9), (10, 10), (10, 11), (9, 11), (8, 10)]:
        grid.add_active_cell(x, y)
    
    paused = True

    sdl2.ext.init()

    window = sdl2.ext.Window("PySDL2 Conway's Game of Life", size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    running = True




    while running:  

        # Events
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
            elif event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_SPACE:
                    paused = not paused
                elif event.key.keysym.sym == sdl2.SDLK_c:
                    grid.clear()
                elif event.key.keysym.sym == sdl2.SDLK_r:
                    grid.randomize(.3)
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                x, y = event.button.x // TILE_SIZE, event.button.y // TILE_SIZE
                grid.cells[y][x].is_alive = not grid.cells[y][x].is_alive
                if grid.cells[y][x].is_alive:
                    grid.add_active_cell(x,y)
                else:
                    if (x, y) in grid.active_cells:
                        grid.remove_active_cell(x,y)



        # Render
        renderer.clear()
        for x, y in grid.active_cells:
            renderer.fill((x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),sdl2.ext.Color(200, 200, 200))
        for x in range(grid.width + 1):
            renderer.draw_line((x * TILE_SIZE, 0, x * TILE_SIZE, WINDOW_HEIGHT),sdl2.ext.Color(40, 40, 40))
        for y in range(grid.height + 1):
            renderer.draw_line((0, y * TILE_SIZE, WINDOW_WIDTH, y * TILE_SIZE),sdl2.ext.Color(40, 40, 40))
        
        if not paused:
            grid.step()


        renderer.present()
        sdl2.SDL_Delay(100)

    sdl2.ext.quit()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("To customize width, height, and tile size: python main.py <window_width> <window_height> <tile_size>")
    else:
        WINDOW_WIDTH = int(sys.argv[1])
        WINDOW_HEIGHT = int(sys.argv[2])
        TILE_SIZE = int(sys.argv[3])
    main()
