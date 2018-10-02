from modules import *
from scene import *
import mario
import glob
from components import *


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def whenBrickAbove():
    if mario.Mario.powerType != 0:
        glob.breakAbove = 1
        mainscene_board().printboard(glob.board_pos)
        os.system('aplay data/sound/brick_smash.wav&')
        glob.breakAbove = 0
        return
    os.system('spd-say ouch')
    glob.brickAbove = 1
    mario.Mario.x -= 1
    mainscene_board().printboard(glob.board_pos)
    time.sleep(.05)
    glob.brickAbove = 2
    mario.Mario.x += 1
    mainscene_board().printboard(glob.board_pos)
    glob.brickAbove = 0
    time.sleep(.05)

# SHOOT MISSILES


def shoot():
    if mario.Mario.powerType != 2:
        return
    os.system('aplay data/sound/fireball.wav&')
    m = missile(mario.Mario.x + 1, mario.Mario.y)
    glob.missiles.append(m)

# FINAL ANIMATION


def moveFlagDown():
    os.system('aplay data/sound/flagpole.wav&')
    tmpTimer = time.time()
    _ = 0
    while _ <= 13:
        if time.time() - tmpTimer > 0.3:
            glob.grid[20 + _:23 + _:1, 552:560:1] = '-'
            _ += 1
            flag().updateFlag(35 + _, 550)
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            tmpTimer = time.time()
            mainscene_board().printboard(glob.board_pos)

# TAKING BACK ANIMATION


def takeBack():
    _ = 525
    tmpTimer = time.time()
    while _ != 25:
        if time.time() - tmpTimer > 0.05:
            mainscene_board().printboard(_)
            print(
                "\n\n  ",
                Fore.GREEN,
                "def",
                Fore.YELLOW,
                "so_Thats_How_You_Reuse_Your_Code",
                Fore.WHITE,
                "():")
            print(
                "       ",
                Fore.YELLOW,
                "make_Player_Play_The_Same_Level_Again_And_Pray_the_player_doesnt_get_bored",
                Fore.WHITE,
                "()")
            print(
                "       ",
                Fore.YELLOW,
                "get_Marks_For_Making_Different_Levels",
                Fore.WHITE,
                "()")
            print("                 -a function made by a python NOOB")
            _ -= 5
            tmpTimer = time.time()
    time.sleep(5)
    mario.Mario.y = 6
    glob.board_pos = 0
    mainscene_board().printboard(glob.board_pos)


# Key Press Functions
def keyPressE():
    # set TIMERS
    timer = time.time()
    timer1 = time.time()
    xx = mario.Mario.x
    while xx - mario.Mario.x < 8:

        # move Enemies and Missiles while this code is running
        if time.time() - glob.tmptimer > glob.levelTimer:
            for i in range(0, len(glob.enemyList)):
                glob.enemyList[i].moveEnemy()
            glob.tmptimer = time.time()
            glob.spikeList[0].moveSpikes()
            mainscene_board().printboard(glob.board_pos)

        # timer of 0.1sec set for movement horizontally
        if time.time() - timer1 > .1:
            if glob.grid[mario.Mario.x][mario.Mario.y + 1] == glob.grid[36][3]:
                break
            if glob.grid[mario.Mario.x, mario.Mario.y +
                         1] == glob.grid[35, 700]:
                mario.Mario.POWER_DOWN()
                return
            mario.Mario.y += 1
            timer1 = time.time()
        # timer of 0.05 set for movement vertically 
        if time.time() - timer > .05:

            # break from loop when encounters an immovable character
            
            if glob.grid[mario.Mario.x -
                         1][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x -
                                                                            1][mario.Mario.y -
                                                                               1] == glob.grid[36][3]:
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[36][720] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[36][720]:
                whenBrickAbove()
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[20][236]:
                mario.Mario.POWER_UP()
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[36][721]:
                glob.SCORE += 5
                glob.COINS += 2
                solidblock(mario.Mario.x - 2,
                           mario.Mario.y - (mario.Mario.y % 2))
                break
            mario.Mario.x -= 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            timer = time.time()

    # Loop for returning back on ground
    while xx != mario.Mario.x:
        # move enemies and missiles
        if time.time() - glob.tmptimer > glob.levelTimer:
            for i in range(0, len(glob.enemyList)):
                glob.enemyList[i].moveEnemy()
            glob.tmptimer = time.time()
            glob.spikeList[0].moveSpikes()
            mainscene_board().printboard(glob.board_pos)
        
        # move horizontally 
        if time.time() - timer1 > .1:
            if glob.grid[mario.Mario.x][mario.Mario.y + 1] == glob.grid[36][3]:
                break
            if glob.grid[mario.Mario.x, mario.Mario.y +
                         1] == glob.grid[35, 700]:
                mario.Mario.POWER_DOWN()
                return

            mario.Mario.y += 1
            timer1 = time.time()
        
        # move Vertically
        if time.time() - timer > .05:
            # break at immovable characters
            if mario.Mario.powerType == 0:
                if glob.grid[mario.Mario.x + 1,
                             mario.Mario.y] == glob.grid[35,
                                                         700] or glob.grid[mario.Mario.x + 1,
                                                                           mario.Mario.y - 1] == glob.grid[35,
                                                                                                           700]:
                    for i in glob.enemyList:
                        if i.y == mario.Mario.y or i.y == mario.Mario.y - 1:
                            glob.grid[i.x][i.y] = '-'
                            glob.SCORE += 10
                            i.dir = 0
                            del i
                if glob.grid[mario.Mario.x +
                             1][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x +
                                                                                1][mario.Mario.y -
                                                                                   1] == glob.grid[36][3]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[20][236]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[36][720] or glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[36][720]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[36][721]:
                    break
            else:
                if glob.grid[mario.Mario.x + 2,
                             mario.Mario.y] == glob.grid[35,
                                                         700] or glob.grid[mario.Mario.x + 2,
                                                                           mario.Mario.y - 1] == glob.grid[35,
                                                                                                           700]:
                    for i in glob.enemyList:
                        if i.y == mario.Mario.y or i.y == mario.Mario.y - 1:
                            glob.grid[i.x, i.y] = '-'
                            glob.SCORE += 10
                            i.dir = 0
                            del i
                if glob.grid[mario.Mario.x +
                             2][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x +
                                                                                2][mario.Mario.y -
                                                                                   1] == glob.grid[36][3]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[20][236]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[36][720] or glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[36][720]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[36][721]:
                    break

            mario.Mario.x += 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            timer = time.time()


def keyPressQ():
    # set timers
    timer = time.time()
    timer1 = time.time()
    xx = mario.Mario.x
    while xx - mario.Mario.x < 8:
        if time.time() - glob.tmptimer > glob.levelTimer:
            for i in range(0, len(glob.enemyList)):
                glob.enemyList[i].moveEnemy()
            glob.tmptimer = time.time()
            glob.spikeList[0].moveSpikes()
            mainscene_board().printboard(glob.board_pos)

        # move horizontally
        if time.time() - timer1 > .1:
            if glob.grid[mario.Mario.x][mario.Mario.y - 2] == glob.grid[36][3]:
                break
            if mario.Mario.y - 1 == glob.board_pos:
                break
            if glob.grid[mario.Mario.x, mario.Mario.y -
                         1] == glob.grid[35, 700]:
                mario.Mario.POWER_DOWN()
                return
            mario.Mario.y -= 1
            timer1 = time.time()

        # move vertically
        if time.time() - timer > .05:
            if glob.grid[mario.Mario.x -
                         1][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x -
                                                                            1][mario.Mario.y -
                                                                               1] == glob.grid[36][3]:
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[36][720] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[36][720]:
                whenBrickAbove()
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[20][236]:
                mario.Mario.POWER_UP()
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[36][721]:
                glob.SCORE += 5
                glob.COINS += 2
                solidblock(mario.Mario.x - 2,
                           mario.Mario.y - (mario.Mario.y % 2))
                break
            mario.Mario.x -= 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            timer = time.time()
    while xx != mario.Mario.x:
        if time.time() - glob.tmptimer > glob.levelTimer:
            for i in range(0, len(glob.enemyList)):
                glob.enemyList[i].moveEnemy()
            glob.tmptimer = time.time()
            glob.spikeList[0].moveSpikes()
            mainscene_board().printboard(glob.board_pos)

        # move horizontally
        if time.time() - timer1 > .1:
            if glob.grid[mario.Mario.x][mario.Mario.y - 2] == glob.grid[36][3]:
                break
            if mario.Mario.y - 1 == glob.board_pos:
                break
            if glob.grid[mario.Mario.x, mario.Mario.y -
                         1] == glob.grid[35, 700]:
                mario.Mario.POWER_DOWN()
                return

            mario.Mario.y -= 1
            if mario.Mario.y - glob.board_pos > 25:
                glob.board_pos = mario.Mario.y - glob.board_pos - 24
            timer1 = time.time()

        # move vertically
        if time.time() - timer > .05:
            if mario.Mario.powerType == 0:
                if mario.Mario.powerType == 0:
                    if glob.grid[mario.Mario.x + 1,
                                 mario.Mario.y] == glob.grid[35,
                                                             700] or glob.grid[mario.Mario.x + 1,
                                                                               mario.Mario.y - 1] == glob.grid[35,
                                                                                                               700]:
                        for i in glob.enemyList:
                            if i.y == mario.Mario.y or i.y == mario.Mario.y - 1:
                                glob.grid[i.x][i.y] = '-'
                                glob.SCORE += 10
                                i.dir = 0
                                del i
                if glob.grid[mario.Mario.x +
                             1][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x +
                                                                                1][mario.Mario.y] == glob.grid[36][720] or glob.grid[mario.Mario.x +
                                                                                                                                     1][mario.Mario.y -
                                                                                                                                        1] == glob.grid[36][720] or glob.grid[mario.Mario.x +
                                                                                                                                                                              1][mario.Mario.y -
                                                                                                                                                                                 1] == glob.grid[36][3]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[20][236]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[36][721]:
                    break

            else:
                if glob.grid[mario.Mario.x + 2,
                             mario.Mario.y] == glob.grid[35,
                                                         700] or glob.grid[mario.Mario.x + 2,
                                                                           mario.Mario.y - 1] == glob.grid[35,
                                                                                                           700]:
                    for i in glob.enemyList:
                        if i.y == mario.Mario.y or i.y == mario.Mario.y - 1:
                            glob.grid[i.x, i.y] = '-'
                            glob.SCORE += 10
                            i.dir = 0
                            del i
                if glob.grid[mario.Mario.x +
                             2][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x +
                                                                                2][mario.Mario.y -
                                                                                   1] == glob.grid[36][3]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[20][236]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[36][720] or glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[36][720]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[36][721]:
                    break

            mario.Mario.x += 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            timer = time.time()


def keyPressW():

    # mario.Mario JUMP
    timer = time.time()
    xx = mario.Mario.x
    while xx - mario.Mario.x < 8:
        if time.time() - glob.tmptimer > glob.levelTimer:
            for i in range(0, len(glob.enemyList)):
                glob.enemyList[i].moveEnemy()
            glob.tmptimer = time.time()
            glob.spikeList[0].moveSpikes()
            mainscene_board().printboard(glob.board_pos)

        # move vertically
        if time.time() - timer > .05:
            if glob.grid[mario.Mario.x -
                         1][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x -
                                                                            1][mario.Mario.y -
                                                                               1] == glob.grid[36][3]:
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[36][720] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[36][720]:
                whenBrickAbove()
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[36][721]:
                glob.SCORE += 5
                glob.COINS += 2
                solidblock(mario.Mario.x - 2,
                           mario.Mario.y - (mario.Mario.y % 2))
                break
            elif glob.grid[mario.Mario.x - 1][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x - 1][mario.Mario.y - 1] == glob.grid[20][236]:
                mario.Mario.POWER_UP()
                break
            mario.Mario.x -= 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            timer = time.time()
    while xx != mario.Mario.x:
        if time.time() - glob.tmptimer > glob.levelTimer:
            for i in range(0, len(glob.enemyList)):
                glob.enemyList[i].moveEnemy()
            glob.tmptimer = time.time()
            glob.spikeList[0].moveSpikes()
            mainscene_board().printboard(glob.board_pos)

        # move vertically
        if time.time() - timer > .05:
            if mario.Mario.powerType == 0:
                if glob.grid[mario.Mario.x + 1,
                             mario.Mario.y] == glob.grid[35,
                                                         700] or glob.grid[mario.Mario.x + 1,
                                                                           mario.Mario.y - 1] == glob.grid[35,
                                                                                                           700]:
                    for i in glob.enemyList:
                        if i.y == mario.Mario.y or i.y == mario.Mario.y - 1:
                            glob.grid[i.x, i.y] = '-'
                            glob.SCORE += 10
                            i.dir = 0
                            del i
                if glob.grid[mario.Mario.x +
                             1][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x +
                                                                                1][mario.Mario.y -
                                                                                   1] == glob.grid[36][3]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[20][236]:
                    break
                elif glob.grid[mario.Mario.x + 1][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x + 1][mario.Mario.y - 1] == glob.grid[36][721]:
                    break

            else:
                if glob.grid[mario.Mario.x + 2,
                             mario.Mario.y] == glob.grid[35,
                                                         700] or glob.grid[mario.Mario.x + 2,
                                                                           mario.Mario.y - 1] == glob.grid[35,
                                                                                                           700]:
                    for i in glob.enemyList:
                        if i.y == mario.Mario.y or i.y == mario.Mario.y - 1:
                            glob.grid[i.x, i.y] = '-'
                            glob.SCORE += 10
                            i.dir = 0
                            del i

                if glob.grid[mario.Mario.x +
                             2][mario.Mario.y] == glob.grid[36][3] or glob.grid[mario.Mario.x +
                                                                                2][mario.Mario.y -
                                                                                   1] == glob.grid[36][3]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[20][236] or glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[20][236]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[36][720] or glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[36][720]:
                    break
                elif glob.grid[mario.Mario.x + 2][mario.Mario.y] == glob.grid[36][721] or glob.grid[mario.Mario.x + 2][mario.Mario.y - 1] == glob.grid[36][721]:
                    break

            mario.Mario.x += 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            timer = time.time()


def moveCheck():
    # Checks Aftermath of move and gets mario to the required position accordinly
    if mario.Mario.powerType == 0:
        if glob.grid[mario.Mario.x +
                     1][mario.Mario.y -
                        1] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                             1][mario.Mario.y] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                                                                                 1][mario.Mario.y] != glob.grid[20][236] and glob.grid[mario.Mario.x +
                                                                                                                                                                       1][mario.Mario.y -
                                                                                                                                                                          1] != glob.grid[36][721] and glob.grid[mario.Mario.x +
                                                                                                                                                                                                                 1][mario.Mario.y] != glob.grid[36][721]:
            timer = time.time()
            while mario.Mario.x < 39 and glob.grid[mario.Mario.x +
                                                   1][mario.Mario.y -
                                                      1] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                                                           1][mario.Mario.y] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                                                                                                               1][mario.Mario.y -
                                                                                                                                                  1] != glob.grid[36][720] and glob.grid[mario.Mario.x +
                                                                                                                                                                                         1][mario.Mario.y] != glob.grid[36][720]:
                if time.time() - glob.tmptimer > glob.levelTimer:
                    for i in range(0, len(glob.enemyList)):
                        glob.enemyList[i].moveEnemy()
                    glob.tmptimer = time.time()
                    mainscene_board().printboard(glob.board_pos)

                if time.time() - timer > .05:
                    mario.Mario.x += 1
                    mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
                    mainscene_board().printboard(glob.board_pos)
                    timer = time.time()
            if mario.Mario.x == 39:
                return 1
    else:
        if glob.grid[mario.Mario.x +
                     2][mario.Mario.y -
                        1] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                             2][mario.Mario.y] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                                                                                 2][mario.Mario.y] != glob.grid[36][720] and glob.grid[mario.Mario.x +
                                                                                                                                                                       2][mario.Mario.y -
                                                                                                                                                                          1] != glob.grid[36][720] and glob.grid[mario.Mario.x +
                                                                                                                                                                                                                 2][mario.Mario.y -
                                                                                                                                                                                                                    1] != glob.grid[36][721] and glob.grid[mario.Mario.x +
                                                                                                                                                                                                                                                           2][mario.Mario.y] != glob.grid[36][721]:
            timer = time.time()
            while mario.Mario.x < 38 and glob.grid[mario.Mario.x +
                                                   2][mario.Mario.y -
                                                      1] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                                                           2][mario.Mario.y] != glob.grid[36][3] and glob.grid[mario.Mario.x +
                                                                                                                                               2][mario.Mario.y -
                                                                                                                                                  1] != glob.grid[36][720] and glob.grid[mario.Mario.x +
                                                                                                                                                                                         2][mario.Mario.y] != glob.grid[36][720]:
                if time.time() - glob.tmptimer > glob.levelTimer:
                    for i in range(0, len(glob.enemyList)):
                        glob.enemyList[i].moveEnemy()
                    glob.tmptimer = time.time()
                    mainscene_board().printboard(glob.board_pos)

                if time.time() - timer > .05:
                    mario.Mario.x += 1
                    mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
                    mainscene_board().printboard(glob.board_pos)
                    timer = time.time()
        if mario.Mario.x == 38:
            return 1
    return 0


def gameOver():
    # When Player Gets Out
    os.system('spd-say "You are dead\n"')
    os.system('pkill aplay')
    os.system('aplay data/sound/death.wav&')
    ttt = time.time()
    xx = mario.Mario.x
    _ = 0
    while _ < 10:
        if time.time() - ttt > 0.05:
            mario.Mario.x -= 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            ttt = time.time()
            _ += 1
    ttt = time.time()
    while mario.Mario.x != xx:
        if time.time() - ttt > 0.07:
            mario.Mario.x += 1
            mario.Mario.addMario(mario.Mario.x, mario.Mario.y)
            mainscene_board().printboard(glob.board_pos)
            ttt = time.time()
    glob.GAMEOVER = 1
