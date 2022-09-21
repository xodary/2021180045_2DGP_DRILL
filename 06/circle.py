from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400 + 250 * math.sin(math.pi / 180 * x),350 - 250 * math.cos(math.pi / 180 * x))
    x = x + 10 * math.pi / 180
    delay(0.001)

close_canvas()
