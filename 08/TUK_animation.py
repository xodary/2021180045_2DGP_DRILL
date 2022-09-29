from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirX
    global dirY
    global line

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                line = 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
                line = 0
            elif event.key == SDLK_UP:
                if line == 3 or line == 1:
                    line = 1
                else:
                    line = 0
                dirY += 1
            elif event.key == SDLK_DOWN:
                if line == 3 or line == 1:
                    line = 1
                else:
                    line = 0
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                if dirY == 0:
                    line = 3
            elif event.key == SDLK_LEFT:
                dirX += 1
                if dirY == 0:
                    line = 2
            elif event.key == SDLK_UP:
                if dirX == 0:
                    if line == 1:
                        line = 3
                    else:
                        line = 2
                dirY -= 1
            elif event.key == SDLK_DOWN:
                if dirX == 0:
                    if line == 1:
                        line = 3
                    else:
                        line = 2
                dirY += 1


open_canvas(TUK_WIDTH, TUK_HEIGHT)
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0
line = 3

while running:
    clear_canvas()
    grass.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * line, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dirX * 5
    if x < 0 or x > TUK_WIDTH:
        x -= dirX * 5
    y += dirY * 5
    if y < 0 or y > TUK_HEIGHT:
        y -= dirY * 5

    delay(0.01)

close_canvas()

