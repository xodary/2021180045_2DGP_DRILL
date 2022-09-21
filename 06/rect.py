from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
while(1):
    
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.001)
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.001)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.001)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.001)
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.001)
    x = 0
    
    while (x < 360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + 250 * math.sin(math.pi / 180 * x),350 - 250 * math.cos(math.pi / 180 * x))
        x = x + 10 * math.pi / 180
        delay(0.001)
    x = 400close_canvas()
