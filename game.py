import tcod as libtcod
import sys



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
        self.room = [[Path() for i in range(self.width)] for j in range(self.height)]
    def draw(self, con, player):
        libtcod.console_set_default_foreground(con, libtcod.white)              #모름
        if player.x < 10: a = 0                                                 #player 기준 시야 범위 설정 
        else: a = player.x - 10
        if player.x > self.width - 11: b = self.width
        else: b = player.x + 10
        if player.y < 10: c = 0
        else: c = player.y - 10
        if player.y > self.height - 11: d = self.height
        else: d = player.y + 10
        for i in range(c, d):
            for j in range(a, b):
                libtcod.console_put_char(con, j, i, self.room[i][j].char, libtcod.BKGND_NONE)#그리기
        libtcod.console_blit(con, 0, 0, self.width, self.height, 0, 0, 0)       #모름
        libtcod.console_flush()                                                 #This is the part that presents everything on the screen. Pretty straightforward.모름
        for i in range(c, d):
            for j in range(a, b):
                libtcod.console_put_char(con, j, i, ' ', libtcod.BKGND_NONE)
        libtcod.console_put_char(con, player.x, player.y, player.ex_object.char, libtcod.BKGND_NONE)#원래 있던 자리 지움


class Entity(Solid):
    def __init__(self, x, y, char):
        self.char = char
        
        self.x = x
        self.y = y
        self.ex_object = screen.room[y][x]
        screen.room[y][x] = self
    hp = 10

    def move(self, dx, dy):####오류가 있을 수 있음.
        
        if self.x + dx > screen.width-1 or self.x + dx < 0:
            dx = 0
        if self.y + dy > screen.height-1 or self.y + dy < 0:
            dy = 0
        if not isinstance(screen.room[self.y+dy][self.x+dx],Solid):
            screen.room[self.y][self.x] = self.ex_object
            self.x += dx
            self.y += dy
            self.ex_object = screen.room[self.y][self.x]
            screen.room[self.y][self.x] = self
        
class Enemy(Entity):
    char = '+'

def main():


    ##GUI설정
    global screen
    screen = Screen(80, 50)
    

    for i in range(40):
        Enemy(i, i, '+')
    
    
    #libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) #폰트를 지정한 png파일로 바꿈
    libtcod.console_init_root(screen.width, screen.height, "qqqqqqqqqq", False) #창만들기(창 가로, 높이, "창의 이름", 전체화면 여부)
    ##

    ##객체 설정
    player = Entity(45, 35, '@')
    ##

    con = libtcod.console_new(screen.width, screen.height)                      #새로운 콘솔창 만들기
    
    key = libtcod.Key()                                                         #키보드 입력
    mouse = libtcod.Mouse()                                                     #마우스 입력

    ##반복문
    while not libtcod.console_is_window_closed():                               #창이 안 닫혔을 때


        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)        #뭔지 모름
        
        screen.draw(con, player)                                                #화면에 그리기

        ##키 관련
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
        ##
    ##
if __name__ == "__main__":                                                      #프로그램이 직접실행되었을 때
    main()






