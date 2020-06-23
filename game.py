import tcod as libtcod
import sys



class Solid():
    pass

class Enemy(Solid):
    char = '+'

'''asdasdasdsadasdasda'''

class Path():
    char = '.'

class Wall(Solid):
    pass

class Room():
    pass

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.room = [[]*self.width]*self.height
        #self.room = [[Path() for i in range(self.width)]]*self.height
        self.room = [[Path() for i in range(self.width)] for j in range(self.height)]
    def draw(self, con, player):
        #self.room[player.y][player.x] = player
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
                libtcod.console_put_char(con, j, i, self.room[i][j].char, libtcod.BKGND_NONE)
        #libtcod.console_put_char(con, player.x, player.y, self.room[player.y][player.x].char, libtcod.BKGND_NONE)#플레이어 그리기
        libtcod.console_blit(con, 0, 0, self.width, self.height, 0, 0, 0)       #모름
        '''for y in range(screen_height):
            for x in range(screen_width):
                libtcod.console_put_char(0, x, y, screen_draw[y][x], libtcod.BKGND_NONE)'''
        libtcod.console_flush()                                                 #This is the part that presents everything on the screen. Pretty straightforward.모름
        #screen.room[player.y][player.x] = player.ex_object
        for i in range(c, d):
            for j in range(a, b):
                libtcod.console_put_char(con, j, i, ' ', libtcod.BKGND_NONE)
        libtcod.console_put_char(con, player.x, player.y, player.ex_object.char, libtcod.BKGND_NONE)#원래 있던 자리 지움



class Entity(Solid):
    def __init__(self, char):
        self.char = char
        
    x = 30
    y = 45
    hp = 10
    ex_object = Enemy()
    def put(self, x, y):
        self.ex_object = screen.room[x][y]
        screen.room[x][y] = self

    def move(self, dx, dy):####오류가 있을 수 있음.
        
        if self.x + dx > screen.width and self.x + dx <= 0:
            dx = 0
        if self.y + dy > screen.height and self.y + dy <= 0:
            dy = 0
        if not type(screen.room[self.x+dx][self.y+dy]) == type(Enemy()):####오류 수정 안 됨. Solid 객체의 하위인 Entity와 Enemy, Wall
            screen.room[self.y][self.x] = self.ex_object
            self.x += dx
            self.y += dy
            self.ex_object = screen.room[self.y][self.x]
            screen.room[self.y][self.x] = self
        '''a = 0
        for i in range(len(screen.room)):
            a = screen.room[i].count(self.char)
        print(a)'''
        

def main():


    ##GUI설정
    global screen
    screen = Screen(80, 50)
    

###screen.room이 잘 작동하나 테스트
    for i in range(40):
        #Enemy().put(i,i)###################오류 수정 안 됨. Enemy는 Entity를 부모로 상속받아야하는데 Entity에 Enemy가 필요함
        screen.room[i][i] = Enemy()
    '''
    a = []
    for i in range(len(screen.room)):
        a.append([])
        for j in range(len(screen.room[i])):
            a[i].append(screen.room[i][j].char)

    print(a)'''
###
    
    
    #libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) #폰트를 지정한 png파일로 바꿈
    libtcod.console_init_root(screen.width, screen.height, "qqqqqqqqqq", False) #창만들기(창 가로, 높이, "창의 이름", 전체화면 여부)
    ##

    ##객체 설정
    player = Entity('@')
    #player.put(3,5)
    ##

    con = libtcod.console_new(screen.width, screen.height)                      #새로운 콘솔창 만들기
    
    key = libtcod.Key()                                                         #키보드 입력
    mouse = libtcod.Mouse()                                                     #마우스 입력


    ##반복문
    while not libtcod.console_is_window_closed():                               #창이 안 닫혔을 때


###Entity.move 테스트

        '''for i in range(0,5):
            for j in range(0,5):
                print((screen.room[i][j].char), end = '')
            print()
        print("\n\n\n")'''
###

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)        #뭔지 모름
        
        screen.draw(con, player)                                                #화면에 그리기

        ##키 관련
        if key.vk == libtcod.KEY_ESCAPE:
            #sys.exit()                                                         #이걸로도 가능함
            return True                                                         #원래 이건데 이걸로 하면 창이 안 닫힘
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






