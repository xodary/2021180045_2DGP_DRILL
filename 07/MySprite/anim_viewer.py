from pico2d import *
open_canvas(600, 400)
character = load_image('sprite.png')
background = load_image('background.png')

# 947 * 994
x = 0
y = 0
width = 80
height = 80

def walking():
    yPos = 50
    frame = -1
    for xPos in range(0, 200, 10):
        frame = (frame + 1) % 8 + 1
        rendering(frame, 0, xPos, yPos)

def running():
    xPos = 200
    yPos = 50
    frame = -1
    line = 6
    for xPos in range(200, 400, 20):
        frame = (frame + 1) % 7 + 6
        rendering(frame, line, xPos, yPos)

def jumping():
    xPos = 400
    yPos = 50
    frame = 0
    for frame in range(0, 12, 1):
        rendering(frame, 2, xPos, yPos)
        xPos = xPos + 10

def dead():
    xPos = 520
    yPos = 50
    rendering(7, 8, xPos, yPos)
    rendering(9, 0, xPos, yPos)

def ghost():
    xPos = 520
    yPos = 50
    frame = 0
    for xPos in range(520, 0, -10):
        rendering(frame, 10, xPos, yPos)
        frame = (frame + 1) % 10

def rendering(frame, line, x, y):
    clear_canvas()
    background.draw(300, 200)
    character.clip_draw(frame * width, 994 - 80 - line * height, width, height, x, y)
    update_canvas()
    delay(0.1)
    get_events()



while True:
    walking()
    running()
    jumping()
    dead()
    ghost()

close_canvas()

