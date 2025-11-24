import sdl2
import sdl2.ext
import sdl2.sdlttf
from OOP.grid import Grid
from OOP.oop_render import render
from OOP.oop_events import event_handler
import sys


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


TILE_SIZE = 20
RANDOMIZE_PROBABILITY = 0.2





def main():
    grid_width = WINDOW_WIDTH // TILE_SIZE
    grid_height = WINDOW_HEIGHT // TILE_SIZE
    UI_BAR_HEIGHT = int(WINDOW_HEIGHT * 0.1)
    FONT_SIZE = int(UI_BAR_HEIGHT * 0.3)
    grid = Grid(grid_width, grid_height)
    
    generation = 0
    paused = True

    sdl2.ext.init()

    window = sdl2.ext.Window("PySDL2 Conway's Game of Life", size=(WINDOW_WIDTH, WINDOW_HEIGHT + UI_BAR_HEIGHT))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    running = True

    font_manager = sdl2.ext.FontManager(font_path='VCR_OSD_MONO_1.001.ttf', size=FONT_SIZE)

    renderer_obj = render(renderer, grid, font_manager,TILE_SIZE, WINDOW_HEIGHT)
    event_handler_obj = event_handler(grid, TILE_SIZE)

    while running:  

        # Events
        for event in sdl2.ext.get_events():
            event_handler_obj.handle_event(event)
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_SPACE:
                    paused = not paused
                elif event.key.keysym.sym == sdl2.SDLK_r:
                    generation = 0
                    paused = True
                elif event.key.keysym.sym == sdl2.SDLK_c:
                    generation = 0
                    paused = True



        # Render
        renderer.clear()
        renderer_obj.draw_grid()
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
    if len(sys.argv) < 5:
        print("To customize width, height, and tile size: python main.py <window_width> <window_height> <tile_size> <randomize_probability> (.1,.2,etc)")
        quit()
    else:
        WINDOW_WIDTH = int(sys.argv[1])
        WINDOW_HEIGHT = int(sys.argv[2])
        TILE_SIZE = int(sys.argv[3])
        RANDOMIZE_PROBABILITY = float(sys.argv[4])
    main()
