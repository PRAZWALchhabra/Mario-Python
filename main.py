from modules import *
from func import *
from start_screen import *
from level import *


GAME()
os.system('aplay data/sound/main_theme.wav&')
time.sleep(2)
LEVEL()
if glob.level == 2:
    time.sleep(1)
    os.system('clear')
    print("     SO THAT WAS EASY!!!!     ")
    time.sleep(2)
    glob.LevelUp = 0
    glob.levelTimer = 0.1
    glob.level = 2
    glob.TIMER = time.time() + 10
    glob.board_pos = 0
    LEVEL()
print("\n\n    YOUR SCORE  ->  ", glob.SCORE, "\n\n")
