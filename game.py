import tcod as libtcod
import sys
import time
import threading


class System:
    pass
       
class Solid:
    pass


class Path:
    char = '.'

class Wall(Solid):
    pass

class Room:
    pass

class Item:
    pass


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.textline = []

        #스테이지 설정
        self.room = [[Path() for i in range(self.width)] for j in range(self.height)]

        
    def draw(self, player):
        libtcod.console_set_default_foreground(con, libtcod.white)
        
        #player 기준 시야 범위 설정
        if player.x < 10: a = 0                                                  
        else: a = player.x - 10
        if player.x > self.width - 11: b = self.width
        else: b = player.x + 10
        if player.y < 10: c = 0
        else: c = player.y - 10
        if player.y > self.height - 11: d = self.height
        else: d = player.y + 10

        #그리기
        for i in range(c, d):
            for j in range(a, b):
                libtcod.console_put_char(con, j, i+5, self.room[i][j].char, libtcod.BKGND_NONE)#그리기
                
        libtcod.console_blit(con, 0, 0, self.width, self.height+10, 0, 0, 0)
        libtcod.console_flush()                                                 #This is the part that presents everything on the screen. Pretty straightforward

        #원래 있던 자리 지우기
        for i in range(c, d):
            for j in range(a, b):
                libtcod.console_put_char(con, j, i+5, ' ', libtcod.BKGND_NONE)
        libtcod.console_put_char(con, player.x, player.y+5, player.ex_object.char, libtcod.BKGND_NONE)#원래 있던 자리 지움

        
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

class Room():
    pass


def main():

    global system
    system = System()
    #GUI설정
    
    global screen
    screen = Screen(80, 50)
    

    for i in range(40):
        Enemy(i, i, '+')
    
    libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) #폰트를 지정한 png파일로 바꾸기
    libtcod.console_init_root(screen.width, screen.height+10, "qqqqqqqqqq", False) #창만들기(창 가로,창 높이, 창의 이름, 전체화면 여부)

    #객체 설정
    player = Entity(45, 35, '@')

    #콘솔창 설정
    global con
    con = libtcod.console_new(screen.width, screen.height+10)                   #새로운 콘솔창 만들기
    key = libtcod.Key()                                                         #키보드 입력(상하좌우, 엔터 등)
    
    mouse = libtcod.Mouse()                                                     #마우스 입력

    
    #무한 반복문
    while not libtcod.console_is_window_closed():                               #창이 안 닫혔을 때

        key_char = chr(key.c)                                                   #키보드 입력(문자)

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        screen.draw(player)                                                     #화면에 그리기
        #키 실행
        if key.vk and screen.textline != []:
            screen.remove_text()
        if key.vk == libtcod.KEY_ESCAPE:
            return True                                                         #게임 종료
        elif key.vk == libtcod.KEY_ENTER and key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen()) #전체화면/창모드
        elif key.vk == libtcod.KEY_RIGHT:
            player.move(1,0)
        elif key.vk == libtcod.KEY_LEFT:
            player.move(-1,0)
        elif key.vk == libtcod.KEY_UP:
            player.move(0,-1)
        elif key.vk == libtcod.KEY_DOWN:
            player.move(0,1)
        elif key_char == 'q':
            screen.draw_text("asdasd")

if __name__ == "__main__":                                                      #프로그램이 직접실행되었을 때
    main()






