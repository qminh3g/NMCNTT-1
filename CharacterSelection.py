from ImageAssets import *
from StartRacing import *

# Write code to get player name from here
playerName = 'Noobmaster69'


def TraceCharacterSelection(x, y):
    for i in range(6):
        CharList[i].speed(0)
        CharList[i].hideturtle()
        CharList[i].penup()
        CharList[i].shape(avatarsChose[i])
        CharList[i].goto(x, y)
        CharList[i].showturtle()
        x = x + 100

# This whole block of code is used to assign playerName to Character's name, not efficient but it works
# Once Character is selected it starts the game


def PlayerAssign0(x, y):
    NameList[0] = playerName
    StartGame()


def PlayerAssign1(x, y):
    NameList[1] = playerName
    StartGame()


def PlayerAssign2(x, y):
    NameList[2] = playerName
    StartGame()


def PlayerAssign3(x, y):
    NameList[3] = playerName
    StartGame()


def PlayerAssign4(x, y):
    NameList[4] = playerName
    StartGame()


def PlayerAssign5(x, y):
    NameList[5] = playerName
    StartGame()
