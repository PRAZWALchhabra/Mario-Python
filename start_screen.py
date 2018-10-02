from modules import *
from func import *
from start_scenes import *
import threading
import glob


def GAME():
    old_settings = termios.tcgetattr(sys.stdin)

    printStartScreen1(1)
    try:
        tty.setcbreak(sys.stdin.fileno())
        while True:
            if isData():
                # read input keystroke from user
                keyStroke = sys.stdin.read(1)
                if keyStroke == 'q':
                    break
                if keyStroke == chr(32):
                    os.system('aplay data/sound/letsgo.wav&')
                    time.sleep(.01)
                    printStartScreen2()
                    break
                if keyStroke == 'w' and glob.gameMode == 2:
                    glob.gameMode = 1
                    printStartScreen1(1)
                if keyStroke == 's' and glob.gameMode == 1:
                    glob.gameMode = 2
                    printStartScreen1(2)
                else:
                    printStartScreen1(glob.gameMode)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
