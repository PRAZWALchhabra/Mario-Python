from modules import *
from components import *
import mario
import glob
import color

numpy.set_printoptions(linewidth=1000, threshold=numpy.nan)


class mainscene_board():

    def buildBoard(self):
        # create basic background
        # global glob.grid
        glob.grid[:] = "-"
        glob.grid[36:40:1, :] = "#"
        glob.grid[35, 700] = '@'
        glob.grid[36, 720] = 'O'
        glob.grid[36, 721] = '*'
        glob.grid[36, 722] = 'Y'

        # clouds
        for i in range(7, 900, 100):
            cloud(9, i)
        for i in range(60, 900, 100):
            cloud(7, i)

        # tunnels
        for i in range(80, 900, 150):
            tunnel(33, i)

        # mario.Mario
        mario.Mario.addMario(35, 6)

        # blocks
        for i in range(40, 400, 80):
            block(31, i)

        # random blocks
        block(26, 228)
        block(26, 238)
        block(26, 288)
        block(26, 410)
        block(24, 518)
        block(24, 528)

        sblock(26, 226)
        sblock(20, 230)
        sblock(20, 242)

        powerUpBox(20, 236)
        powerUpBox(24, 60)

        # coinBoxes
        CoinBoxes(28, 218)
        CoinBoxes(28, 220)
        CoinBoxes(30, 34)
        CoinBoxes(30, 28)
        CoinBoxes(30, 72)
        CoinBoxes(30, 74)
        CoinBoxes(30, 100)
        CoinBoxes(30, 106)
        CoinBoxes(30, 154)
        CoinBoxes(30, 170)

        # random tunnels
        tunnel(32, 350)

        # levelender
        LeftSteps(35, 450)
        RightSteps(16, 490)

        # flag
        flag().addflag(35, 550)

        # castle
        CASTLE(35, 570)

        # World wriiten at the top

        # emptyFalls
        #maxWidth is 4
        noGround(60, 4)
        noGround(485, 5)
        noGround(19, 5)
        noGround(180, 8)

        # spikes
        spike1 = spikes(23, 535)
        glob.spikeList.append(spike1)

        # add enemies OWLS
        e1 = enemy(35, 28)
        e2 = enemy(35, 54)
        e3 = enemy(35, 72)
        e4 = enemy(35, 98)
        e5 = enemy(35, 144)
        e6 = enemy(35, 213)
        e7 = enemy(35, 280)
        e8 = enemy(35, 332)
        e9 = enemy(35, 369)
        e10 = enemy(35, 376)
        e11 = enemy(35, 420)
        e12 = enemy(35, 440)
        e13 = enemy(35, 528)
        e14 = enemy(35, 540)
        e15 = enemy(23, 535)
        glob.enemyList.extend(
            [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15])

    def moveBrick(self):
        if glob.breakAbove:
            self.breakAbove()
        if mario.Mario.y % 2 == 0:
            self.moveBrickOdd()
        else:
            self.moveBrickEven()

    def breakAbove(self):
        glob.SCORE += 10
        if mario.Mario.y % 2 != 0:
            # time.sleep(1)
            glob.grid[mario.Mario.x - 2, mario.Mario.y -
                      1:mario.Mario.y + 1:1] = ['-', '-']
            glob.grid[mario.Mario.x - 1, mario.Mario.y -
                      1:mario.Mario.y + 1:1] = ['-', '-']
        else:
            glob.grid[mario.Mario.x -
                      1, mario.Mario.y:mario.Mario.y +
                      2:1] = ['-', '-']
            glob.grid[mario.Mario.x -
                      2, mario.Mario.y:mario.Mario.y +
                      2:1] = ["-", '-']

    def moveBrickOdd(self):
        if glob.brickAbove == 1:
            glob.grid[mario.Mario.x,
                      mario.Mario.y:mario.Mario.y + 2:1] = [')', '-']
            glob.grid[mario.Mario.x -
                      2, mario.Mario.y:mario.Mario.y +
                      2:1] = ["O", 'O']
        elif glob.brickAbove == 2:
            glob.grid[mario.Mario.x -
                      1, mario.Mario.y:mario.Mario.y +
                      2:1] = ['O', 'O']
            glob.grid[mario.Mario.x -
                      3, mario.Mario.y:mario.Mario.y +
                      2:1] = ['-', '-']

    def moveBrickEven(self):
        if glob.brickAbove == 1:
            glob.grid[mario.Mario.x, mario.Mario.y -
                      1:mario.Mario.y + 1:1] = ['-', '-']
            glob.grid[mario.Mario.x - 2, mario.Mario.y -
                      1:mario.Mario.y + 1:1] = ['O', 'O']
        elif glob.brickAbove == 2:
            glob.grid[mario.Mario.x - 1, mario.Mario.y -
                      1:mario.Mario.y + 1:1] = ['O', 'O']
            glob.grid[mario.Mario.x - 3, mario.Mario.y -
                      1:mario.Mario.y + 1:1] = ['-', '-']

    def printboard(self, index):
        os.system('clear')
        textAtTheTop().addTextAtTop()
        self.moveBrick()
        for row in range(40):
            for column in range(0 + index, 100 + index, 1):
                sys.stdout.write(color.getcolor(
                    glob.grid[row, column].decode(), row, column))
            sys.stdout.write("\n")
