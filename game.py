import tcod as libtcod
import sys
import time
import threading
import random


class System:
    pass

       
class Solid:
    pass


class Path:
    char = '.'


class Nothing:
    char = ' '


class Wall(Solid):
    pass


class Room:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.width = random.randint(5,10)
        self.height = random.randint(5,10)
        
        


class Item:
    pass


class Screen:
    def __init__(self):
        self.width = width
        self.height = height
        self.textline = []

        #스테이지 설정
        self.room = [[Nothing() for i in range(self.width)] for j in range(self.height)]
        
    def draw(self, player, left, right, up, down):
        libtcod.console_set_default_foreground(con, libtcod.white)
        
        #그리기
        for i in range(down, up):
            for j in range(left, right):
                libtcod.console_put_char(con, j, i+5, self.room[i][j].char, libtcod.BKGND_NONE)
                
        libtcod.console_blit(con, 0, 0, self.width, self.height+10, 0, 0, 0)
        #This is the part that presents everything on the screen. Pretty straightforward
        libtcod.console_flush()

        #원래 있던 자리 지우기
        for i in range(down, up):
            for j in range(left, right):
                libtcod.console_put_char(con, j, i+5, ' ', libtcod.BKGND_NONE)

        #원래 있던 자리 지움22222
        libtcod.console_put_char(con, player.x, player.y+5, player.ex_object.char, libtcod.BKGND_NONE)

    def draw_text(self, text):
        self.textline.append(text)
        ###print(self.textline)
        for i, s in enumerate(text):
            libtcod.console_put_char(con, i, len(self.textline)-1, s, libtcod.BKGND_NONE)
            
    def remove_text(self):
        if self.textline != []:
            for i in range(30):
                libtcod.console_put_char(con, i, len(self.textline)-1, ' ', libtcod.BKGND_NONE)
            self.textline.pop()
            ####print(self.textline)
        

class Entity(Solid):
    def __init__(self, x, y, char): 
        self.char = char
        
        self.x = x 
        self.y = y
        self.ex_object = screen.room[y][x]
        screen.room[y][x] = self
    hp = 10

    def move(self, dx, dy):
        
        if self.x + dx > screen.width-1 or self.x + dx < 0:
            dx = 0
        if self.y + dy > screen.height-1 or self.y + dy < 0:
            dy = 0
        if isinstance(screen.room[self.y+dy][self.x+dx],Solid):
            screen.draw_text("You can't move there")
        else:
            screen.room[self.y][self.x] = self.ex_object
            self.x += dx
            self.y += dy
            self.ex_object = screen.room[self.y][self.x]
            screen.room[self.y][self.x] = self

        
class Enemy(Entity):
    char = '+'


def generate_stage(width, height):
    stage = [(i, j) for i in range(width) for j in range(height)]
    room_number = random.randint(3, 6)
    room = [[] for i in range(room_number)]
    for i in range(room_number):
        x, y = random.choice(stage)
        


def main():
    global system
    system = System()
    
    #GUI설정
    global screen
    screen = Screen(60, 40)

    #Entity.move 함수 테스트
    for i in range(40):
        Enemy(i, i, '+')
        
    #폰트를 지정한 png파일로 바꾸기
    libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    #창만들기(창 너비,창 높이, 창 이름, 전체화면 여부)
    libtcod.console_init_root(screen.width, screen.height+10, "qqqqqqqqqq", False)

    #객체 설정
    player = Entity(45, 35, '@')

    #새로운 콘솔창 만들기
    global con
    con = libtcod.console_new(screen.width, screen.height+10)
    
    #키보드 입력(상하좌우, 엔터 등)
    key = libtcod.Key()
    #마우스 입력
    mouse = libtcod.Mouse()

    
    #무한 반복문
    while not libtcod.console_is_window_closed():
        
        #키보드 입력(문자)
        key_char = chr(key.c)

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        
        
        #player 기준 시야 범위 설정
        if player.x < 10: left = 0                                                  
        else: left = player.x - 10
        if player.x > screen.width - 11: right = screen.width
        else: right = player.x + 10
        if player.y < 10: down = 0
        else: down = player.y - 10
        if player.y > screen.height - 11: up = screen.height
        else: up = player.y + 10
        
        #화면에 그리기
        ##screen.draw(player, left, right, up, down)
        screen.draw(player, 0, screen.width, screen.height, 0)
        
        
        #텍스트 삭제
        if key.vk and screen.textline != []:
            screen.remove_text()
            
        #게임 종료
        if key.vk == libtcod.KEY_ESCAPE:
            return True
        #전체화면/창모드
        elif key.vk == libtcod.KEY_ENTER and key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        #플레이어 이동
        elif key.vk == libtcod.KEY_RIGHT:
            player.move(1,0)
        elif key.vk == libtcod.KEY_LEFT:
            player.move(-1,0)
        elif key.vk == libtcod.KEY_UP:
            player.move(0,-1)
        elif key.vk == libtcod.KEY_DOWN:
            player.move(0,1)
        #draw_text함수 테스트
        elif key_char == 'q':
            screen.draw_text("asdasd")

if __name__ == "__main__":
    main()






