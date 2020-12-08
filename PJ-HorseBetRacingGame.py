import time
import random
from ImageAssets import *
import turtle
import pygame
import os
from pygame import mixer
from random import randint
from playsound import playsound
from threading import Thread


scrWidth = 1200
scrHeight = 645


# turtle has to be declared globally, so these other functions can recognise them.
frameTitle = turtle.Turtle()
logo = turtle.Turtle()
title1 = turtle.Turtle()
title2 = turtle.Turtle()

startButton = turtle.Turtle()
optionsButton = turtle.Turtle()
instructionsButton = turtle.Turtle()
minigameButton = turtle.Turtle()
exitButton = turtle.Turtle()


def initBackground():
    # play music on separate thread (in background)
    #musicThread = Thread(target=playMusic)
    # musicThread.start()
    pygame.init()
    mixer.init()

    mixer.music.load(os.path.join("soundtrack", "menu_st2.mp3"))
    mixer.music.play(loops=-1)

    screen = turtle.Screen()
    screen.title("PET-BET RACING GAME")
    screen.setup(scrWidth, scrHeight)
    # insert background
    screen.bgpic('img/bg.gif')
    #import shapes
    screen.addshape("img/logo.gif")
    screen.addshape("img/title1.gif")
    screen.addshape("img/title2.gif")
    screen.addshape("img/cloud-sign.gif")
    screen.addshape("img/button.gif")
    screen.addshape("img/button1_en.gif")
    screen.addshape("img/button2_en.gif")
    screen.addshape("img/button3_en.gif")
    screen.addshape("img/button4_en.gif")
    screen.addshape("img/exit_en.gif")
    # insert title_frame

    frameTitle.speed(0)
    frameTitle.penup()
    frameTitle.setpos(115, 190)
    frameTitle.shape("img/cloud-sign.gif")
    # insert logo
    logo.speed(0)
    logo.penup()
    logo.setpos(-165, 210)
    logo.shape("img/logo.gif")
    # insert title1 "Pet"

    title1.speed(0)
    title1.penup()
    title1.setpos(80, 220)
    title1.shape("img/title1.gif")
    # insert title2 "bet racing"

    title2.speed(0)
    title2.penup()
    title2.setpos(120, 160)
    title2.shape("img/title2.gif")
    initMainMenu()


def clearButtons(x, y):
    turtle.hideturtle()
    startButton.hideturtle()
    optionsButton.hideturtle()
    instructionsButton.hideturtle()
    minigameButton.hideturtle()

# def startGame(x,y):

# StartGameButton is used to clear the screen after click on Start Game


def StartGameButton(x, y):
    turtle.hideturtle()
    startButton.hideturtle()
    optionsButton.hideturtle()
    instructionsButton.hideturtle()
    minigameButton.hideturtle()
    logo.hideturtle()
    title1.hideturtle()
    title2.hideturtle()
    exitButton.hideturtle()
    frameTitle.hideturtle()
    PlayGame(x, y)
# def instructions(x,y):


# def options(x,y):

# def minigame(x,y):
def exitGame(x, y):
    quit()


def initMainMenu():
    # insert title2 "bet racing"
    # insert "START" button
    startButton.speed(0)
    startButton.penup()
    startButton.setpos(0, 30)
    startButton.shape("img/button1_en.gif")

    # insert "INSTRUCTIONS" button
    instructionsButton.speed(0)
    instructionsButton.penup()
    instructionsButton.setpos(0, -60)
    instructionsButton.shape("img/button2_en.gif")

    # insert "OPTIONS" button
    optionsButton.speed(0)
    optionsButton.penup()
    optionsButton.setpos(0, -150)
    optionsButton.shape("img/button3_en.gif")

    # insert "MINIGAME" button
    minigameButton.speed(0)
    minigameButton.penup()
    minigameButton.setpos(0, -240)
    minigameButton.shape("img/button4_en.gif")

    # insert "EXIT" button
    exitButton.speed(0)
    exitButton.penup()
    if scrWidth > 1100 and scrHeight > 700:
        exitButton.setpos(550, 300)
    else:
        exitButton.setpos(300, 300)
    exitButton.shape("img/exit_en.gif")


#    startButton.onclick(startGame)
    startButton.onclick(StartGameButton)
#    optionsButton.onclick(options)
#    instructionsButton.onclick(instructions)
#    minigameButton.onclick(minigame)
    exitButton.onclick(exitGame)


def drawControlMenu():
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-370, -180)
    turtle.color("#1167b1")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(740)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(740)
    turtle.right(90)
    turtle.forward(130)
    turtle.end_fill()


def main():
    initBackground()
    initMainMenu()
    # drawControlMenu()


if __name__ == '__main__':
    main()

# From here downwards used to be StartRacing.py
# These coordinates to draw characters on the screen
y = 154
x = -570
random.seed(time.time())
# Result list
ResultsList = []
TrueResultsList = []
CharListRanked = []
TrueCharListRanked = []
StatusList = ['normal', 'normal', 'normal', 'normal', 'normal', 'normal']


def TraceWinLoseTable():
    if playerName == TrueResultsList[0]:
        WinTableS.speed(0)
        WinTableS.hideturtle()
        WinTableS.penup()
        WinTableS.shape(WinTable)
        WinTableS.goto(0, -200)
        WinTableS.showturtle()
        WinTableS.onclick(returnToMainMenu)
        # Need to write code to reward player here

    else:
        LoseTableS.speed(0)
        LoseTableS.hideturtle()
        LoseTableS.penup()
        LoseTableS.shape(LoseTable)
        LoseTableS.goto(0, -200)
        LoseTableS.showturtle()
        LoseTableS.onclick(returnToMainMenu)
        # Need to write code to deduct coins here


def TraceResult():

    turtle.clear()
    finishLineS.hideturtle()
    screen.bgpic(RankTable)

    # Draw the results on the screen
    y1 = 55
    y2 = 55

    for i in range(6):
        turtle.tracer(False)
        turtle.hideturtle()
        turtle.penup()

        turtle.color('white')
        if i <= 2:
            turtle.goto(-140, y1)
            turtle.write(TrueResultsList[i], font=("Arial", 12, "bold"))
            y1 = y1 - 70
        else:
            turtle.goto(100, y2)
            turtle.write(TrueResultsList[i], font=("Arial", 12, "bold"))
            y2 = y2 - 70
        turtle.update()


def TraceResultCharacter():
    # Sort CharList to draw them
    for name in CharListRanked:
        if name not in TrueCharListRanked:
            TrueCharListRanked.append(name)
    y1 = 60
    y2 = 60
    for i in range(6):
        turtle.tracer(False)
        TrueCharListRanked[i].speed(0)
        TrueCharListRanked[i].hideturtle()
        TrueCharListRanked[i].penup()
        if i <= 2:
            TrueCharListRanked[i].goto(-165, y1)
            y1 = y1 - 70
        else:
            TrueCharListRanked[i].goto(75, y2)
            y2 = y2 - 70
        TrueCharListRanked[i].showturtle()
        if i == 5:
            TraceWinLoseTable()

        turtle.update()


def TraceCharacter(x, y):
    potion1.speed(0)
    potion1.hideturtle()
    potion1.penup()
    potion1.shape(potion)
    potion1.goto(500, -260)
    potion1.showturtle()
    rocket1.speed(0)
    rocket1.hideturtle()
    rocket1.penup()
    rocket1.shape(rocket)
    rocket1.goto(450, -260)
    rocket1.showturtle()
    for i in range(6):
        CharList[i].speed(0)
        CharList[i].hideturtle()
        CharList[i].penup()
        CharList[i].shape(avatarsChose[i])
        CharList[i].goto(x, y)
        CharList[i].showturtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y - 20)
        turtle.color('red')
        turtle.write(NameList[i], font=("Arial", 20, "bold"))
        y = y - 60


def DrawScreen():
    turtle.tracer(False)
    screen.bgpic(mapChose)
    TraceCharacter(x, y)
    if mapSize == 'small':
        TraceFinishLineSmall()
    if mapSize == 'medium':
        TraceFinishLineMedium()
    if mapSize == 'large':
        TraceFinishLineLarge()
    turtle.update()
    time.sleep(1)


def RaceStart():

    while True:
        for i in range(6):

            if CharList[i].xcor() >= finishLineS.xcor():
                CharListRanked.append(CharList[i])
                ResultsList.append(NameList[i])
            # Result List sorted

            for name in ResultsList:
                if name not in TrueResultsList:
                    TrueResultsList.append(name)

            # This block of code is used to determine speed of the characters, need optimizing

            if CharList[i].xcor() >= 150:
                a = 1
                b = 3
                turtle.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                turtle.update()
            elif StatusList[i] == 'slow':
                CharList[i].forward(random.randint(1, 4))
            elif StatusList[i] == 'fast':
                CharList[i].forward(random.randint(3, 10))
            elif CharList[i].xcor() >= -200:
                a = 1
                b = 5
                turtle.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                turtle.update()
            elif CharList[i].xcor() >= -300:
                a = 1
                b = 7
                turtle.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                turtle.update()
            else:
                a = 1
                b = 10
                turtle.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                turtle.update()
            maxX = max(CharList[0].xcor(), CharList[1].xcor(), CharList[2].xcor(
            ), CharList[3].xcor(), CharList[4].xcor(), CharList[5].xcor())
            for i in range(6):
                if CharList[i].xcor() >= maxX:
                    target = i
                if NameList[i] == playerName:
                    targetFast = i

            def goSlower(x, y):
                potion2.speed(0)
                potion2.hideturtle()
                potion2.penup()
                potion2.shape(potion)
                potion2.goto(-570, CharList[target].ycor())
                potion2.showturtle()
                while True:
                    turtle.tracer(False)
                    potion2.forward(5)
                    time.sleep(0.001)
                    turtle.update()
                    if potion2.xcor() >= CharList[target].xcor():
                        potion2.hideturtle()
                        StatusList[target] = 'slow'
                        # Need to write code to deduct Potion
                        break

            def goFaster(x, y):
                rocket2.speed(0)
                rocket2.hideturtle()
                rocket2.penup()
                rocket2.shape(rocket)
                rocket2.goto(-570, CharList[targetFast].ycor())
                rocket2.showturtle()
                while True:
                    turtle.tracer(False)
                    rocket2.forward(5)
                    time.sleep(0.001)
                    turtle.update()
                    if rocket2.xcor() >= CharList[targetFast].xcor():
                        rocket2.hideturtle()
                        StatusList[targetFast] = 'fast'
                        # Need to write code to deduct Potion
                        break
            potion1.onclick(goSlower)
            rocket1.onclick(goFaster)
        if len(TrueResultsList) == 6:
            break


def StartGame():
    DrawScreen()
    RaceStart()
    TraceResult()
    TraceResultCharacter()


def TraceCharacterSelection(x, y):
    screen.bgpic('img/CharacterSelectScreen.gif')
    turtle.tracer(False)
    for i in range(6):
        CharList[i].speed(0)
        CharList[i].hideturtle()
        CharList[i].penup()
        CharList[i].shape(avatarsChose[i])
        CharList[i].goto(x, y)
        CharList[i].showturtle()
        x = x + 100
    turtle.update()

# This whole block of code is used to assign playerName to Character's name, not efficient but it works
# Once Character is selected it starts the game


def PlayerAssign0(x, y):
    NameList[0] = playerName
    TraceMapSelectionScreen()


def PlayerAssign1(x, y):
    NameList[1] = playerName
    TraceMapSelectionScreen()


def PlayerAssign2(x, y):
    NameList[2] = playerName
    TraceMapSelectionScreen()


def PlayerAssign3(x, y):
    NameList[3] = playerName
    TraceMapSelectionScreen()


def PlayerAssign4(x, y):
    NameList[4] = playerName
    TraceMapSelectionScreen()


def PlayerAssign5(x, y):
    NameList[5] = playerName
    TraceMapSelectionScreen()


# These functions make the butotns in Map size selection clickable


def TraceFinishLineSmall():
    finishLineS.hideturtle()
    finishLineS.penup()
    finishLineS.speed(0)

    finishLineS.goto(0, 45)
    finishLineS.shape(finishLine)
    finishLineS.showturtle()


def TraceFinishLineMedium():
    finishLineS.hideturtle()
    finishLineS.penup()
    finishLineS.speed(0)

    finishLineS.goto(260, 45)
    finishLineS.shape(finishLine)
    finishLineS.showturtle()


def TraceFinishLineLarge():
    finishLineS.hideturtle()
    finishLineS.penup()
    finishLineS.speed(0)

    finishLineS.goto(520, 45)
    finishLineS.shape(finishLine)
    finishLineS.showturtle()


def SetMaptoSmall(x, y):
    SmallButton.hideturtle()
    MediumButton.hideturtle()
    LargeButton.hideturtle()
    global mapSize
    mapSize = 'small'
    StartGame()


def SetMaptoMedium(x, y):
    SmallButton.hideturtle()
    MediumButton.hideturtle()
    LargeButton.hideturtle()
    global mapSize
    mapSize = 'medium'
    StartGame()


def SetMaptoLarge(x, y):
    SmallButton.hideturtle()
    MediumButton.hideturtle()
    LargeButton.hideturtle()
    global mapSize
    mapSize = 'large'
    StartGame()
# This function is used to Draw the map size selection screen


def TraceMapSelectionScreen():
    turtle.tracer(False)
    CharList[0].hideturtle()
    CharList[1].hideturtle()
    CharList[2].hideturtle()
    CharList[3].hideturtle()
    CharList[4].hideturtle()
    CharList[5].hideturtle()
    screen.bgpic('img/MapSelectionScreen.gif')
    SmallButton.speed(0)
    SmallButton.hideturtle()
    SmallButton.penup()
    SmallButton.shape(Small)
    SmallButton.goto(0, 100)
    SmallButton.showturtle()
    MediumButton.speed(0)
    MediumButton.hideturtle()
    MediumButton.penup()
    MediumButton.shape(Medium)
    MediumButton.goto(0, 0)
    MediumButton.showturtle()
    LargeButton.speed(0)
    LargeButton.hideturtle()
    LargeButton.penup()
    LargeButton.shape(Large)
    LargeButton.goto(0, -100)
    LargeButton.showturtle()
    turtle.update()
    SmallButton.onclick(SetMaptoSmall)
    MediumButton.onclick(SetMaptoMedium)
    LargeButton.onclick(SetMaptoLarge)


def PlayGame(x, y):
    screen.setup(1200, 645)
# This function is used to draw the characters on the screen to select
    TraceCharacterSelection(-250, 0)

    CharList[0].onclick(PlayerAssign0)
    CharList[1].onclick(PlayerAssign1)
    CharList[2].onclick(PlayerAssign2)
    CharList[3].onclick(PlayerAssign3)
    CharList[4].onclick(PlayerAssign4)
    CharList[5].onclick(PlayerAssign5)

    turtle.done()


def returnToMainMenu(x, y):
    turtle.tracer(False)
    turtle.clear()
    turtle.hideturtle()
    global ResultsList
    global TrueResultsList
    global CharListRanked
    global TrueCharListRanked
    global StatusList
    global NameList
    global Char1Name
    global Char2Name
    global Char3Name
    global Char4Name
    global Char5Name
    global Char6Name

    ResultsList = []
    TrueResultsList = []
    CharListRanked = []
    TrueCharListRanked = []

    StatusList = ['normal', 'normal', 'normal', 'normal', 'normal', 'normal']
    NameList = ['Tân', 'Thịnh', 'Tú', 'Huy', 'Ben', 'Minh']
    random.shuffle(NameList)
    Char1Name = NameList[0]
    Char2Name = NameList[1]
    Char3Name = NameList[2]
    Char4Name = NameList[3]
    Char5Name = NameList[4]
    Char6Name = NameList[5]

    for i in range(6):
        CharList[i].hideturtle()
    WinTableS.hideturtle()
    LoseTableS.hideturtle()
    potion1.hideturtle()
    rocket1.hideturtle()
    screen.bgpic('img/bg.gif')
    startButton.showturtle()
    optionsButton.showturtle()
    instructionsButton.showturtle()
    minigameButton.showturtle()
    logo.showturtle()
    title1.showturtle()
    title2.showturtle()
    exitButton.showturtle()
    frameTitle.showturtle()
    turtle.update()


turtle.done()
