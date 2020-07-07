from Europe_UNIT import *
import time


class Tile:
    def __init__(self, x, y):
        self.roughness = 1
        self.x = x
        self.y = y


    
def move(obj, tile):
    obj.x = tile.x
    obj.y = tile.y
    obj.turn -= tile.roughness
    print("qwe")

    
def show_obj(obj):
    status = {}
    status["name"] = obj.name
    status["health"] = obj.health
    status["x"] = obj.x
    status["y"] = obj.y
    
    for key in status.keys():
        value = status.get(key, "None")
        print("{} : {}\t".format(key, value), end = '')
    print()

def attack(obj, subj):
    print("{}이(가) {}을(를) 공격함.".format(obj.name, subj.name))


def main():
    showing_obj = None
    ally = Europe_LongSword_Man()
    ally.pia = "ally"
    ally.turn = ally.speed
    ally.x = 0
    ally.y = 0

    foe = Europe_LongBow_Man()
    foe.pia = "foe"
    foe.turn = foe.speed
    foe.x = 1
    foe.y = 0

    _tile = Tile(0,1)
    while True:
        a = int(input())
        if a == 1:
            print(1)
            test = ally
        elif a == 2:
            print(2)
            test = foe
        else:
            print(3)
            test = Tile(0, a-2)

        
        clicked_obj = test
        
        
        if isinstance(clicked_obj, UNIT):
            if clicked_obj.pia == "ally":
                show_obj(clicked_obj)
                showing_obj = clicked_obj
            
            elif clicked_obj.pia == "foe":
                try:
                    if showing_obj.pia == "ally":
                        print(2324)
                        attack(showing_obj, clicked_obj)
                    else: raise AttributeError
                except :
                        show_obj(clicked_obj)
                        showing_obj = clicked_obj
                
        elif isinstance(clicked_obj, Tile):
            obj = showing_obj
            tile = clicked_obj
            
            try:
                check = (obj.pia == "ally")
                
                if tile.x == obj.x:
                    check = check and abs(tile.y - obj.y) <= obj.range
                elif tile.y == obj.y:
                    check = check and abs(tile.y - obj.y) <= obj.range
                else: check = False
                
                check = check and (obj.turn - tile.roughness >= 0)
                
                if check:
                    move(obj, tile)
                else:
                    print("이동 안 됨")
                    
            except: pass


if __name__ == "__main__":
    main()
