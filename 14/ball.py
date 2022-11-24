import random
from pico2d import *
import game_world
import server


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1000),\
                         random.randint(0, 1000)

    def draw(self):
        self.image.draw(self.x - server.background.window_left,
                        self.y - server.background.window_bottom, 40, 40)
        # draw_rectangle(*self.get_bb())
        # * - 튜플을 풀어헤친다

    def update(self):
        pass

    def Ball(self):
        image = None

    def get_bb(self):
        return self.x - server.background.window_left - 20,\
               self.y - server.background.window_bottom - 20, \
               self.x - server.background.window_left + 20, \
               self.y - server.background.window_bottom + 20

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

