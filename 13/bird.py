from pico2d import *
import game_framework
import game_world
from ball import Ball

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.6
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    width = 918//5
    height = 506//3

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 0: self.dir  = 1
        elif self.x > 1600: self.dir = -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw((int(self.frame) % 5)*Bird.width,
                                           506 - (int(self.frame) // 5 + 1)*Bird.height,
                                           Bird.width, Bird.height, 0, 'h', self.x, self.y, 150, 150)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5)*Bird.width,
                                           506 - (int(self.frame) // 5 + 1)*Bird.height,
                                           Bird.width, Bird.height, 0, '', self.x, self.y, 150, 150)


