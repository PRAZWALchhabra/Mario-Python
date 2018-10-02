from modules import *
import mario
import glob


# CLOUDS
class cloud(object):
    def __init__(self, x, y):
        self.cloud_char = "^"
        glob.grid[x:x + 2:1, y:y + 13:1] = self.cloud_char
        glob.grid[x - 1:x + 3:3, y + 1:y + 12:1] = self.cloud_char
        glob.grid[x - 2, y + 2:y + 11:1] = self.cloud_char
        glob.grid[x - 2, y + 5:y + 8:1] = "-"
        glob.grid[x - 1, y + 6] = "-"

# TUNNEL


class tunnel(object):
    # tunnel is 5x3
    def __init__(self, x, y):
        self.tunnel_char = "#"
        if random.choice([0, 1]):
            x -= 1
        glob.grid[x:x + 5:1, y + 1:y + 5:1] = self.tunnel_char
        glob.grid[x, y:y + 6:5] = self.tunnel_char

# NO GROUND


class noGround(object):
    # global glob.grid
    def __init__(self, y, width):
        self.empty_char = "-"
        glob.grid[36:40:1, y:y + width:1] = self.empty_char

# CASTLE


class CASTLE(object):
    # global glob.grid
    def __init__(self, x, y):
        self.castle_char = "H"
        glob.grid[x:x - 6:-1, y:y + 20:1] = self.castle_char
        glob.grid[x - 6:x - 10:-1, y + 5:y + 15:1] = self.castle_char
        glob.grid[x:x - 3:-1, y + 8:y + 12:1] = "*"

# FLAG


class flag:
    # height of flag is 3 bring both down at same rate and move untill y cord of both is 35
    # global glob.grid
    flag_char = "M"
    flag_char1 = "|"

    def addflag(self, x, y):
        glob.grid[x:x - 16:-1, y:y + 2:1] = self.flag_char1
        glob.grid[x - 15:x - 12:1, y + 2:y + 10:1] = self.flag_char

    def updateFlag(self, x, y):
        glob.grid[35:19:-1, 550:552:1] = self.flag_char1
        glob.grid[x - 15:x - 12:1, y + 2:y + 10:1] = self.flag_char


# BLOCKS
# PARENT BLOCK CLASS


class Block(object):
    def __init__(self):
        # global glob.grid
        self.block_char = "O"
        self.solidblock_char = "#"
        self.power_char = "$"

    def addsblock(self, x, y, z):
        glob.grid[x:x + 2:1, y:y + 2:1] = z


# Inherited Classes


class block(Block):
    def __init__(self, x, y):
        self.block_char = "O"
        glob.grid[x:x + 2:1, y:y + 12:1] = self.block_char


class sblock(Block):
    def __init__(self, x, y):
        self.block_char = "O"
        self.addsblock(x, y, self.block_char)


class solidblock(Block):
    def __init__(self, x, y):
        os.system('aplay data/sound/coin.wav&')
        self.solidblock_char = "#"
        self.addsblock(x, y, self.solidblock_char)


class powerUpBox(Block):
    def __init__(self, x, y):
        self.power_char = "$"
        self.addsblock(x, y, self.power_char)


class CoinBoxes(Block):
    def __init__(self, x, y):
        self.box_char = "*"
        self.addsblock(x, y, self.box_char)

# STEPS

# PARENT STEPS CLASS


class Steps(object):
    def __init__(self):
        self.step_char = "#"

# Inherited Classes


class LeftSteps(Steps):
    def __init__(self, x, y):
        self.step_char = "#"
        glob.grid[x:x - 4:-1, y:y + 35:1] = self.step_char
        glob.grid[x - 4:x - 8:-1, y + 7:y + 35:1] = self.step_char
        glob.grid[x - 8:x - 12:-1, y + 14:y + 35:1] = self.step_char
        glob.grid[x - 12:x - 16:-1, y + 21:y + 35:1] = self.step_char
        glob.grid[x - 16:x - 20:-1, y + 28:y + 35:1] = self.step_char


class RightSteps(Steps):
    def __init__(self, x, y):
        self.step_char = "#"
        glob.grid[x:x + 4:1, y:y + 7:1] = self.step_char
        glob.grid[x + 4:x + 8:1, y:y + 14:1] = self.step_char
        glob.grid[x + 8:x + 12:1, y:y + 21:1] = self.step_char
        glob.grid[x + 12:x + 16:1, y:y + 28:1] = self.step_char
        glob.grid[x + 16:x + 20:1, y:y + 35:1] = self.step_char

# TEXT PRINTED AT THE TOP


class textAtTheTop:
    def listOfxDigits(self, x, n):
        a = []
        tmp = 'a'
        for i in range(0, x):
            tmp = int(n % 10) + 48
            tmp = chr(tmp)
            a.append(tmp)
            n /= 10
        return a[::-1]

    def addTextAtTop(self):

        # Remove What was Printed Earlier

        # score
        glob.grid[2, 10 + glob.prevboard_pos:15 +
                  glob.prevboard_pos:1] = ['-', '-', '-', '-', '-']
        glob.grid[3, 10 + glob.prevboard_pos:16 +
                  glob.prevboard_pos:1] = ['-', '-', '-', '-', '-', '-']
        # Level
        glob.grid[2, 60 + glob.prevboard_pos:65 +
                  glob.prevboard_pos:1] = ['-', '-', '-', '-', '-']
        glob.grid[3, 61 + glob.prevboard_pos:64 +
                  glob.prevboard_pos:1] = ['-', '-', '-']
        # Time
        glob.grid[2, 80 + glob.prevboard_pos:84 +
                  glob.prevboard_pos:1] = ['-', '-', '-', '-']
        glob.grid[3, 81 + glob.prevboard_pos:84 +
                  glob.prevboard_pos:1] = ['-', '-', '-']
        # Coins
        glob.grid[2, 30 + glob.prevboard_pos:35 +
                  glob.prevboard_pos:1] = ['-', '-', '-', '-', '-']
        glob.grid[3, 31 + glob.prevboard_pos:34 +
                  glob.prevboard_pos:1] = ['-', '-', '-']

        # Print in next iteration

        # Score
        glob.grid[2, 10 + glob.board_pos:15 +
                  glob.board_pos:1] = ['M', 'A', 'R', 'I', '0']
        glob.grid[3, 10 + glob.board_pos:16 +
                  glob.board_pos:1] = self.listOfxDigits(6, glob.SCORE)
        # Level
        glob.grid[2, 60 + glob.board_pos:65 +
                  glob.board_pos:1] = ['W', '0', 'R', 'L', 'D']
        glob.grid[3, 61 + glob.board_pos:64 +
                  glob.board_pos:1] = ['1', '>', '1']
        # Time
        glob.grid[2, 80 + glob.board_pos:84 +
                  glob.board_pos:1] = ['T', 'I', 'M', 'E']
        glob.grid[3,
                  81 + glob.board_pos:84 + glob.board_pos:1] = self.listOfxDigits(3,
                                                                                  int(130 - (time.time() - glob.TIMER)))
        # Coins
        glob.grid[2, 30 + glob.board_pos:35 +
                  glob.board_pos:1] = ['C', '0', 'I', 'N', 'S']
        glob.grid[3, 31 + glob.board_pos:34 +
                  glob.board_pos:1] = self.listOfxDigits(3, glob.COINS)

        glob.prevboard_pos = glob.board_pos

# Missiles By MARIO


class missile():
    def __init__(self, x, y, *z):
        self.x = x
        self.y = y + 2
        self.move = 0

        if len(z) == 0:
            self.dir = 1
            self.missile_char = '+'
        else:
            self.dir = z[0]
            self.missile_char = z[1]

        if glob.grid[x, y] == glob.grid[1, 2]:
            glob.grid[x, y] = self.missile_char

    def moveMissile(self):
        if self.dir == 0:
            return
        if glob.grid[self.x, self.y + 1] == glob.grid[1, 2]:
            glob.grid[self.x, self.y + self.dir] = self.missile_char
            glob.grid[self.x, self.y] = '-'
            self.y += self.dir
            self.move += 1
        elif glob.grid[self.x, self.y + 1] == glob.grid[35, 700]:
            glob.SCORE += 5
            for i in glob.enemyList:
                if [self.x, self.y + 1] == [i.x, i.y]:
                    glob.grid[i.x, i.y] = '-'
                    i.dir = 0
                    break
            glob.grid[self.x, self.y] = '-'
            self.dir = 0
        if self.move >= 4:
            glob.grid[self.x, self.y] = '-'
            self.dir = 0
        self.move += 1

# Enemy CLASS


class enemy(object):
    def __init__(self, x, y):
        self.dir = -1
        self.x = x
        self.y = y
        glob.grid[self.x, self.y] = '@'

    def addEnemy(self):
        glob.grid[self.x, self.y] = '@'

    def moveEnemy(self):
        if glob.grid[self.x,
                     self.y + self.dir] != glob.grid[1,
                                                     2] or glob.grid[self.x + 1,
                                                                     self.y + self.dir] != glob.grid[36,
                                                                                                     3]:
            if self.dir != 0:
                if mario.Mario.powerType == 0:
                    if [self.x,
                        self.y + self.dir] == [mario.Mario.x,
                                               mario.Mario.y] or [self.x,
                                                                  self.y + self.dir] == [mario.Mario.x,
                                                                                         mario.Mario.y - 1]:
                        mario.Mario.POWER_DOWN()
                        return
                if mario.Mario.powerType != 0:
                    if [self.x,
                        self.y + self.dir] == [mario.Mario.x + 1,
                                               mario.Mario.y] or [self.x,
                                                                  self.y + self.dir] == [mario.Mario.x + 1,
                                                                                         mario.Mario.y - 1]:
                        self.dir = 1
                        mario.Mario.POWER_DOWN()
                        return
            self.dir *= -1
        else:
            self.y = self.y + self.dir
            glob.grid[self.x, self.y] = '@'
            glob.grid[self.x, self.y - self.dir] = '-'

# SPIKES FOR BOSS GHOST/ENEMY


class spikes():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.spike_char = "Y"
        self.state = 1
        glob.grid[self.x, self.y + 2] = self.spike_char
        glob.grid[self.x, self.y - 2] = self.spike_char
        glob.grid[self.x - 1, self.y - 2:self.y + 3:1] = self.spike_char

    def moveSpikes(self):
        if self.state == 2:
            glob.grid[self.x - 1, self.y - 1:self.y + 2:2] = '-'
            glob.grid[self.x - 2, self.y - 1:self.y + 2:1] = '-'
            glob.grid[self.x - 1, self.y - 2:self.y + 3:1] = self.spike_char
            self.state = 1
        else:
            glob.grid[self.x - 1, self.y - 2:self.y + 3:1] = '-'
            glob.grid[self.x - 1, self.y - 1:self.y + 2:2] = self.spike_char
            glob.grid[self.x - 2, self.y - 1:self.y + 2:1] = self.spike_char
            self.state = 2
