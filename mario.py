from modules import *
from scene import *
import glob


class player():
    """Character"""

    def __init__(self):
        self.alive = -1
        # powerType 0->no_power 1->Size 2->Size+Bullets
        self.powerType = 0
        self.x = 35
        self.y = 6
        self.px = 35
        self.py = 6

    def MOVE_FORWARD(self):
        self.y = self.y + 1

    def MOVE_BACKWARD(self):
        self.y = self.y - 1

    def POWER_UP(self):
        glob.SCORE += 50
        os.system('aplay data/sound/powerup.wav')
        if self.powerType == 0:
            self.powerType = 1
            self.alive = 1
        else:
            self.alive = 1
            self.powerType = 2
        if self.y < 200:
            glob.grid[24:26:1, 60:62:1] = "#"
        else:
            glob.grid[20:22:1, 236:238:1] = "#"

    def POWER_DOWN(self):
        if self.powerType == 0 and self.alive == -1:
            os.system('aplay data/sound/out.wav&')
            glob.GAMEOVER = 1
        elif self.powerType == 0 and self.alive == 0:
            self.alive = -1
        elif self.powerType != 0 and self.alive == 0:
            self.powerType = 0
        else:
            self.alive = 2
            self.powerType = 0

    def addMario(self, x, y):
        if self.y >= 550:
            glob.LevelUp = 1
        elif self.powerType == 0:
            if glob.grid[self.x,
                         self.y] == glob.grid[36,
                                              722] or glob.grid[self.x,
                                                                self.y - 1] == glob.grid[36,
                                                                                         722]:
                self.POWER_DOWN()
        elif self.powerType != 0:
            if glob.grid[self.x + 1,
                         self.y] == glob.grid[36,
                                              722] or glob.grid[self.x + 1,
                                                                self.y - 1] == glob.grid[36,
                                                                                         722]:
                self.POWER_DOWN()

        if self.powerType == 0:
            glob.grid[self.px, self.py - 1:self.py + 1:1] = ["-", "-"]
            glob.grid[self.x, self.y - 1:self.y + 1:1] = [":", ")"]
        elif self.powerType == 1:
            glob.grid[self.px, self.py - 1:self.py + 1:1] = ["-", "-"]
            glob.grid[self.px + 1, self.py - 1:self.py + 1:1] = ["-", "-"]
            glob.grid[self.x, self.y - 1:self.y + 1:1] = [":", ")"]
            glob.grid[self.x + 1, self.y - 1:self.y + 1:1] = ["|", "|"]
        else:
            glob.grid[self.px, self.py - 1:self.py + 1:1] = ["-", "-"]
            glob.grid[self.px + 1, self.py - 1:self.py + 1:1] = ["-", "-"]
            glob.grid[self.x, self.y - 1:self.y + 1:1] = [":", "}"]
            glob.grid[self.x + 1, self.y - 1:self.y + 1:1] = ["|", "|"]
        self.px = self.x
        self.py = self.y


Mario = player()
