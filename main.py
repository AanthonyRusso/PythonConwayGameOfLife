import sdl2
import sdl2.ext


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


# THis is from a different project, will update once it is ready

def draw_body_outline(renderer, body):
    x = int(body.position.x - body.size.x * 0.5)
    y = int(body.position.y - body.size.y * 0.5)
    w = int(body.size.x)
    h = int(body.size.y)

    rect = sdl2.SDL_Rect(x, y, w, h)
    renderer.draw_rect(rect, sdl2.ext.Color(255, 255, 255))

def draw_body(renderer, body, color):
    x = int(body.position.x - body.size.x * 0.5)
    y = int(body.position.y - body.size.y * 0.5)
    w = int(body.size.x)
    h = int(body.size.y)

    rect = sdl2.SDL_Rect(x, y, w, h)
    renderer.fill(rect, color)


def main():
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



        # Render
        renderer.clear()


        renderer.present()

    sdl2.ext.quit()

if __name__ == "__main__":
    main()
