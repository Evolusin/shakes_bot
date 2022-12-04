import cv2 as cv
from settings import Settings
from states import States
import time
import random


config = Settings()
states = States()
faze = config.state
quest_done = 0


time.sleep(2)
print("Launched")

while True:
    if faze == "mouse_pos":
        faze = states.s_mouse_pos

    elif faze == "debug":
        print(config.karczma_questnpc1['x'])
        print(config.karczma_questnpc1['y'])
        
    elif faze == "sleep":
        x = random.randrange(50,150)
        print(f"Zasypiam na {x} sekund")
        time.sleep(x)
        faze = "logowanie"

    elif faze == "logowanie":
        print(f"Ilosc zrobionych na ten moment questow {quest_done}")
        faze = states.logowanie()

    elif faze == "quest_check":
        faze = states.quest_check()

    elif faze == "do_karczmy":
        faze = states.do_karczmy()

    elif faze == "karczma":
        quest_done=quest_done+1
        faze = states.karczma()

    elif faze == "upgrade":
        faze = states.upgrade()
    
    elif faze == "eq_sell":
        faze = states.eq_sell()

    elif faze == "energry_status":
        faze = states.energry_status()
    
    elif faze == "exiting":
        faze = states.exiting()
        break

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
