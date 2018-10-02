from modules import *
from components import *
from func import *
from scene import *
import glob
import mario


def LEVEL():
    mainscene_board().buildBoard()
    glob.TIMER = time.time()
    time.sleep(.01)
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        mainscene_board().printboard(glob.board_pos)
        tty.setcbreak(sys.stdin.fileno())
        while True:
            if time.time() - glob.tmptimer > glob.levelTimer:
                # move Missiles
                for _ in glob.missiles:
                    _.moveMissile()
                # mainscene_board().printboard(glob.board_pos)
                for i in range(0, len(glob.enemyList)):
                    glob.enemyList[i].moveEnemy()
                glob.tmptimer = time.time()
                glob.spikeList[0].moveSpikes()
                mainscene_board().printboard(glob.board_pos)

            if mario.Mario.alive:
                if mario.Mario.alive == 2:
                    glob.aliveTimer = time.time()
                    mario.Mario.alive = 3
                elif mario.Mario.alive == 3:
                    if time.time() - glob.aliveTimer > 2:
                        mario.Mario.alive = 0
                        mario.Mario.POWER_DOWN()

            if isData():
                keyStroke = sys.stdin.read(1)
                if keyStroke == 'x':
                    os.system('pkill aplay')
                    mainscene_board().printboard(glob.board_pos)
                    break

                if keyStroke == 'd':
                    print('\a')
                    if glob.grid[mario.Mario.x][mario.Mario.y +
                                                1] != glob.grid[36][3]:
                        mario.Mario.y += 1
                        mario.Mario.addMario(mario.Mario.x, mario.Mario.y - 1)
                        mainscene_board().printboard(glob.board_pos)

                elif keyStroke == 'a':
                    print('\a')
                    if glob.grid[mario.Mario.x][mario.Mario.y -
                                                2] != glob.grid[36][3]:
                        if mario.Mario.y - 1 != glob.board_pos:
                            mario.Mario.y -= 1
                            mario.Mario.addMario(
                                mario.Mario.x, mario.Mario.y + 1)
                            mainscene_board().printboard(glob.board_pos)

                elif keyStroke == "e":
                    os.system('aplay data/sound/small_jump.wav&')
                    keyPressE()
                elif keyStroke == "q":
                    os.system('aplay data/sound/small_jump.wav&')
                    keyPressQ()
                elif keyStroke == 'w':
                    os.system('aplay data/sound/small_jump.wav&')
                    keyPressW()
                elif keyStroke == chr(32):
                    shoot()

                if mario.Mario.y - glob.board_pos > 25:
                    glob.board_pos = mario.Mario.y - 25

            if glob.LevelUp:
                os.system('pkill aplay')
                os.system('clear')
                # move flag down
                moveFlagDown()
                mainscene_board().printboard(glob.board_pos)
                if glob.level == 3:
                    os.system('aplay data/sound/world_clear.wav&')
                    break
                else:
                    mario.Mario.y = 6
                    os.system('clear')
                    print("         LEVEL 2 Releasing Soon          ")
                    time.sleep(5)
                    os.system('clear')
                    os.system('aplay data/sound/laugh.wav&')
                    time.sleep(.5)
                    os.system('clear')
                    print(
                        """             Just Joking!! :P It's Here! Try it and respect this NOOB's effort. A juice treat would also be appreciated.             """)
                    time.sleep(5)
                    takeBack()
                    glob.level = 2
                    break

            if moveCheck() or time.time() - glob.TIMER >= 130:
                if time.time() - glob.TIMER >= 130:
                    os.system(
                        'spd-say your times up')
                    time.sleep(1)
                glob.GAMEOVER = 1

            if glob.GAMEOVER:
                gameOver()
                os.system('clear')
                time.sleep(2)
                image_game_over = [
                    "  ___   _   __  __ ___    _____   _____ ___ ",
                    " / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \\",
                    "| (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /",
                    " \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\\"]
                for i in range(0, len(image_game_over)):
                    print(image_game_over[i])
                break

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
