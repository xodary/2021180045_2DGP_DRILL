from pico2d import *


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:  # q에 뭔가 들어있다면
            event = self.q.pop()
            self.cur_state.exit(self)   # 현재 상태를 나가고,
            self.cur_state = next_state[self.cur_state][event] # 다음 상태 계산
            self.cur_state.enter(self, event)  # 다음 상태 들어감

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):  # 소년이 스스로 이벤트를 처리할 수 있게...
        # event는 키 이벤트... 이것을 내부 RD 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    def exit(self):
        print('EXIT IDLE')

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: #시간이 경과하면
            #이벤트를 발생시켜줘야한다. TIMER
            # self.q.insert(0, TIMER) # 객체 지향 프로그래밍 위배, q를 직접 액세스...
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        # self.dir 을 결정해야 함
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1

    def exit(self):
        print('ENTER RUN')
        # run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        # self.dir 을 결정해야 함
        self.frame = 0

    def exit(self):
        print('ENTER SLEEP')

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                 -3.141592 / 2, ' ', self.x + 25, self.y - 25, 100 ,100)
        elif self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                3.141592 / 2, ' ', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO_RUN')
        self.dir = self.face_dir
        self.y += 25

    def exit(self):
        print('ENTER AUTO_RUN')
        # run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir
        self.dir = 0
        self.y -= 25

    def do(self):
        self.frame = (self.frame + 1) % 8
        if self.x <= 0:
            self.dir = 1
        elif self.x >= 800:
            self.dir = -1
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 200, 200)

RD, LD, RU, LU, TIMER, A = range(6)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): A
}
next_state = {
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, A: IDLE},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, A: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, A: AUTO_RUN},
    AUTO_RUN: {RD: RUN, LD: RUN, A: IDLE, RU: AUTO_RUN, LU: AUTO_RUN}
}