import sdl2
import sdl2.ext
import sdl2.sdlttf
from grid import Grid
import sys


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


TILE_SIZE = 20





def main():
    grid_width = WINDOW_WIDTH // TILE_SIZE
    grid_height = WINDOW_HEIGHT // TILE_SIZE
    UI_BAR_HEIGHT = int(WINDOW_HEIGHT * 0.1)
    FONT_SIZE = int(UI_BAR_HEIGHT * 0.3)
    grid = Grid(grid_width, grid_height)
    grid.cells[9][10].is_alive = True
    grid.cells[10][10].is_alive = True
    grid.cells[11][10].is_alive = True
    grid.cells[11][9].is_alive = True
    grid.cells[10][8].is_alive = True
    for x, y in [(10, 9), (10, 10), (10, 11), (9, 11), (8, 10)]:
        grid.add_active_cell(x, y)
    
    generation = 0
    paused = True

    sdl2.ext.init()

    window = sdl2.ext.Window("PySDL2 Conway's Game of Life", size=(WINDOW_WIDTH, WINDOW_HEIGHT + UI_BAR_HEIGHT))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    running = True

    font_manager = sdl2.ext.FontManager(font_path='VCR_OSD_MONO_1.001.ttf', size=FONT_SIZE)




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
                    generation = 0
                elif event.key.keysym.sym == sdl2.SDLK_r:
                    grid.randomize(.3)
                    generation = 0
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
        if paused:
            text_surface = font_manager.render("Paused - Press SPACE to Resume", color = sdl2.ext.Color(255, 255, 255))
        else:
            text_surface = font_manager.render("Running - Press SPACE to Pause", color = sdl2.ext.Color(255, 255, 255))
        text_texture = sdl2.ext.Texture(renderer, text_surface)
        renderer.copy(text_texture, dstrect=(10, WINDOW_HEIGHT + 10, text_surface.w, text_surface.h))
        other_text_surface = font_manager.render("'C' to Clear | 'R' to Randomize", color = sdl2.ext.Color(255, 255, 255))
        other_text_texture = sdl2.ext.Texture(renderer, other_text_surface)
        renderer.copy(other_text_texture, dstrect=(10, WINDOW_HEIGHT + 20 + text_surface.h, other_text_surface.w, other_text_surface.h))

        generation_text_surface = font_manager.render(f"Generation: {generation}", color = sdl2.ext.Color(255, 255, 255))
        generation_text_texture = sdl2.ext.Texture(renderer, generation_text_surface)
        renderer.copy(generation_text_texture, dstrect=(WINDOW_WIDTH - generation_text_surface.w - 10, WINDOW_HEIGHT + 10, generation_text_surface.w, generation_text_surface.h))

        if not paused:
            grid.step()
            generation += 1


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
