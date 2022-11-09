from pico2d import *
import game_framework
import game_world

from grass import Grass
from bird import Bird
from boy import Boy

boy = None
birds = None
grass = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global birds, grass, boy
    boy = Boy()
    birds = [Bird(100 + (i%4) * 150, 200 + (i//4) * 150) for i in range(0, 10)]
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_objects(birds, 1)
    game_world.add_object(boy, 1)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # 강제로 성능 저하
    # delay(0.5)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas(1600, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
