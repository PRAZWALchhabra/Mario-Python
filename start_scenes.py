from modules import *


################  HARD CODED BOARDS USING COLORAMA  ###########################


def printStartScreen1(gameMode):
    os.system('clear')
    print(Back.BLUE, "                                            ")
    print("     MARIO               WORLD     TIME      ")
    print(
        "     000000  ",
        Back.YELLOW,
        "",
        Back.BLUE,
        "x00     1--1                ")
    print("                                             ")
    print(
        "       ",
        Back.RED,
        ".                         .",
        Back.BLUE,
        "       ")
    print(
        "       ",
        Back.RED,
        " SUPER                     ",
        Back.BLUE,
        "       ")
    print(
        "       ",
        Back.RED,
        " MARIO BROS.               ",
        Back.BLUE,
        "       ")
    print(
        Back.BLUE,
        "      ",
        Back.RED,
        ".                         .",
        Back.BLUE,
        "       ")
    print("                  ©1985 NINTENDO             ")
    print("                                             ")
    if gameMode == 1:
        print("             -> 1 PLAYER GAME                ")
        print("                2 PLAYER GAME                ")
    else:
        print("                1 PLAYER GAME                ")
        print("             -> 2 PLAYER GAME                ")
    print("                                             ")
    print(Back.BLUE, "                 TOP- 000000                ")
    print("          :)                                 ")
    print("   :)     ||                                 ")
    print(Back.RED, "                                            ")
    print("                                            ", Style.RESET_ALL)


def printStartScreen2():
    os.system('clear')
    print(Back.BLACK, "                                            ")
    print("     MARIO               WORLD     TIME      ")
    print(
        "     000000  ",
        Back.YELLOW,
        "",
        Back.BLACK,
        "x00     1--1                ")
    print("                                             ")
    print("                                             ")
    print("                WORLD  1-1                   ")
    print("                                             ")
    print("                  :) x  1 <-ONE              ")
    print("                                CHANCE       ")
    print("                                        ONLY ")
    print("                                             ")
    print("                                             ")
    print("                                             ")
    print("                                             ")
    print("                                             ")
    print("                                             ")
    print("                                             ")
    print("                                            ", Style.RESET_ALL)
