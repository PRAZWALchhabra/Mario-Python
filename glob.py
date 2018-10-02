from modules import *

gameMode = 1

# VARIABLES FOR PRINTING BOARD
board_pos = 0
prevboard_pos = 0

# CREATE GRID
grid = numpy.chararray((40, 1000))

# GAME STATES
GAMEOVER = 0
level = 1
LevelUp = 0

# 0 => No Brick Above
# 1 => Brick Above
# 2 => Trace back state 1
brickAbove = 0
breakAbove = 0

# timers
TIMER = 0
tmptimer = time.time()
levelTimer = 0.3
aliveTimer = 0

# score
SCORE = 0

# missiles
missiles = []

# Coins
COINS = 0

# Enemies
enemyList = []

# spikes
spikeList = []
