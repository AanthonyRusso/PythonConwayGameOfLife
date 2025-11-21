import sdl2
import sdl2.ext
from grid import Grid

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


# THis is from a different project, will update once it is ready
TILE_SIZE = 20

GRID_WIDTH = WINDOW_WIDTH // TILE_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // TILE_SIZE



def main():
    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    grid.cells[9][10].is_alive = True
    grid.cells[10][10].is_alive = True
    grid.cells[11][10].is_alive = True
    grid.cells[11][9].is_alive = True
    grid.cells[10][8].is_alive = True
    
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
                    grid.randomize(.1)
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                x, y = event.button.x // TILE_SIZE, event.button.y // TILE_SIZE
                grid.cells[y][x].is_alive = not grid.cells[y][x].is_alive



        # Render
        renderer.clear()
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell = grid.cells[y][x]
                color = sdl2.ext.Color(255, 255, 255) if cell.is_alive else sdl2.ext.Color(0, 0, 0)
                rect = sdl2.SDL_Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                renderer.fill(rect, color)
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
    main()
