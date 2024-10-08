from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        #생성자를 이용해 초기 상태 정의
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.xpos, self.y = random.randint(100, 400), 90
        self.frame = random.randint(0, 7)
    def update(self):
        self.xpos += 2
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100, self.xpos, self.y,100,100)

class Ball:
    def __init__(self):
        self.size = random.randint(0, 1)
        if self.size == 1:
            self.image = load_image('ball41x41.png')
        else:
            self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(20, 780), random.randint(500, 600)
        self.speed = random.randint(1, 3)
    def update(self):
        if self.size == 1:
            self.y = max(80-self.speed * 5, self.y - self.speed)
        else:
            self.y = max(60-self.speed * 3,self.y - self.speed)
    def draw(self):
        if self.size == 1:
            self.image.clip_draw(0, 0, 41, 41, self.x, self.y, 41, 41)
        else:
            self.image.clip_draw(0,0,21,21, self.x, self.y,21,21)
def update_world():
    for o in world:
        o.update()

def rander_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def reset_world():
    global running, grass, team, world
    running = True
    world=[]
    grass = Grass()# 클래스로 객체 생성
    world.append(grass)# world에 집어넣기
    team = [Boy() for i in range(11)]
    world += team
    rain = [Ball() for i in range(20)]
    world += rain
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

reset_world()
while running:
    handle_events()
    update_world()
    rander_world()
    delay(0.01)

close_canvas()
