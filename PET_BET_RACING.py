from ImageAssets import *
import time
import turtle
import pygame
import os
import random
import csv
from pygame import  mixer
from random import randint

#screen resolution
scrWidth = 1200
scrHeight = 645
data = []
score = 0
lives = 0
isOver = "No"
moneyBet = 0

turtle.hideturtle()
# turtle has to be declared globally, so these other functions can recognise them.
frameTitle = turtle.Turtle()
logo = turtle.Turtle()
title1 = turtle.Turtle()
title2 = turtle.Turtle()
screen = turtle.Screen()
startButton = turtle.Turtle()
optionsButton = turtle.Turtle()
instructionsButton = turtle.Turtle()
minigameButton = turtle.Turtle()
exitButton = turtle.Turtle()
stat = turtle.Turtle()
coinUnit = turtle.Turtle()
insertText = turtle.Turtle()
tab = turtle.Turtle()
close = turtle.Turtle()
closeShop = turtle.Turtle()
closeBoard = turtle.Turtle()
shop = turtle.Turtle()
chest = turtle.Turtle()
rank = turtle.Turtle()
stand = turtle.Turtle()
back_layer = turtle.Turtle()
rocketItem = turtle.Turtle()
ticketItem = turtle.Turtle()
luckyCloverItem = turtle.Turtle()
potionItem = turtle.Turtle()
heartItem = turtle.Turtle()
insertTextPrice = turtle.Turtle()
insertTextRank = turtle.Turtle()
insertNotice = turtle.Turtle()
rankBoard = turtle.Turtle()
noticeBoard = turtle.Turtle()
description = turtle.Turtle()
insertTextDescription = turtle.Turtle()
inventory = turtle.Turtle()
rocketItem1 = turtle.Turtle()
ticketItem1 = turtle.Turtle()
luckyCloverItem1 = turtle.Turtle()
potionItem1 = turtle.Turtle()
heartItem1 = turtle.Turtle()
closeInventory = turtle.Turtle()
insertTextInventory = turtle.Turtle()
instructionBoard = turtle.Turtle()
closeInstruction = turtle.Turtle()
insertTextInstruction = turtle.Turtle()

#minigame's turtles
    #screen
bg = turtle.Turtle()

    #character
mole_1 = turtle.Turtle()
mole_2 = turtle.Turtle()
mole_3 = turtle.Turtle()
mole_4 = turtle.Turtle()
mole_5 = turtle.Turtle()
mole_6 = turtle.Turtle()
mole_7 = turtle.Turtle()
    #bomb
bomb_1 = turtle.Turtle()
bomb_2 = turtle.Turtle()
bomb_3 = turtle.Turtle()
bomb_4 = turtle.Turtle()
bomb_5 = turtle.Turtle()
bomb_6 = turtle.Turtle()
bomb_7 = turtle.Turtle()
    #heart
heart_1 = turtle.Turtle()
heart_2 = turtle.Turtle()
heart_3 = turtle.Turtle()

    #Stt
fm = turtle.Turtle()
sm = turtle.Turtle()
ds1 = turtle.Turtle()
ds2 = turtle.Turtle()
dsc = turtle.Turtle()
sttbg = turtle.Turtle()
closeMiniGame = turtle.Turtle()

    #Main game's turtles
SmallButton = turtle.Turtle()
MediumButton = turtle.Turtle()
LargeButton = turtle.Turtle()
potion1 = turtle.Turtle()
potion2 = turtle.Turtle()
rocket1 = turtle.Turtle()
rocket2 = turtle.Turtle()
WinTableS = turtle.Turtle()
LoseTableS = turtle.Turtle()

frameTitle.speed(0)
logo.speed(0)
title1.speed(0)
title2.speed(0)
startButton.speed(0)
optionsButton.speed(0)
instructionsButton.speed(0)
minigameButton.speed(0)
exitButton.speed(0)
stat.speed(0)
coinUnit.speed(0)
insertText.speed(0)
tab.speed(0)
close.speed(0)
closeBoard.speed(0)
closeShop.speed(0)
shop.speed(0)
chest.speed(0)
rank.speed(0)
stand.speed(0)
back_layer.speed(0)
rocketItem.speed(0)
ticketItem.speed(0)
luckyCloverItem.speed(0)
potionItem.speed(0)
heartItem.speed(0)
insertTextPrice.speed(0)
rankBoard.speed(0)
insertTextRank.speed(0)
insertNotice.speed(0)
noticeBoard.speed(0)
description.speed(0)
insertTextDescription.speed(0)
inventory.speed(0)
rocketItem1.speed(0)
ticketItem1.speed(0)
luckyCloverItem1.speed(0)
potionItem1.speed(0)
heartItem1.speed(0)
closeInventory.speed(0)
insertTextInventory.speed(0)
instructionBoard.speed(0)
closeInstruction.speed(0)
insertTextInstruction.speed(0)
closeMiniGame.speed(0)

frameTitle.penup()
logo.penup()
title1.penup()
title2.penup()
startButton.penup()
optionsButton.penup()
instructionsButton.penup()
minigameButton.penup()
exitButton.penup()
stat.penup()
coinUnit.penup()
insertText.penup()
tab.penup()
close.penup()
closeShop.penup()
closeBoard.penup()
shop.penup()
chest.penup()
rank.penup()
stand.penup()
back_layer.penup()
rocketItem.penup()
ticketItem.penup()
luckyCloverItem.penup()
potionItem.penup()
heartItem.penup()
insertTextPrice.penup()
rankBoard.penup()
insertTextRank.penup()
insertNotice.penup()
noticeBoard.penup()
description.penup()
insertTextDescription.penup()
inventory.penup()
rocketItem1.penup()
ticketItem1.penup()
luckyCloverItem1.penup()
potionItem1.penup()
heartItem1.penup()
closeInventory.penup()
insertTextInventory.penup()
instructionBoard.penup()
closeInstruction.penup()
insertTextInstruction.penup()



# create separate Channel objects for simultaneous playback
pygame.init()
mixer.init()
numberMusic = random.randint(1,4)
menu_st = pygame.mixer.Sound('soundtrack/menu_st' + str(numberMusic) + '.mp3')
clickSound = pygame.mixer.Sound('soundtrack/click.mp3')
instructionVoice_en = pygame.mixer.Sound('soundtrack/instruction_en.mp3')
instructionVoice_vi = pygame.mixer.Sound('soundtrack/instruction_vi.mp3')
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel3 = pygame.mixer.Channel(3)
sound = "1"
language = "en"

# sound tracks
def clickSound():
    if sound == "1":
        pygame.init()
        mixer.init()
        mixer.music.load(os.path.join("soundtrack","click.mp3"))
        mixer.music.play()

def instructionRead():
    if sound == "1":
        pygame.init()
        mixer.init()
        mixer.music.load(os.path.join("soundtrack","instruction_" + str(language) + ".mp3"))
        channel0.set_volume(0.1)
        mixer.music.play()

def stopInstructionRead():
    channel2.stop()
    channel0.set_volume(1.0)

def whackSound():
    if sound == "1":
        pygame.init()
        mixer.init()
        mixer.music.load(os.path.join("soundtrack","whack.mp3"))
        mixer.music.play()

def wrongSound():
    if sound == "1":
        pygame.init()
        mixer.init()
        mixer.music.load(os.path.join("soundtrack","wrong.mp3"))
        mixer.music.play()
        
#import shapes
def addShape():
    screen.addshape("img/logo.gif")
    screen.addshape("img/title1.gif")
    screen.addshape("img/title2.gif")
    screen.addshape("img/cloud-sign.gif")
    screen.addshape("img/button.gif")
    screen.addshape("img/button1_en.gif")
    screen.addshape("img/button1_vi.gif")
    screen.addshape("img/button2_en.gif")
    screen.addshape("img/button2_vi.gif")
    screen.addshape("img/button3_en.gif")
    screen.addshape("img/button3_vi.gif")
    screen.addshape("img/button4_en.gif")
    screen.addshape("img/button4_vi.gif")
    screen.addshape("img/exit_en.gif")
    screen.addshape("img/exit_vi.gif")
    screen.addshape("img/coin.gif")
    screen.addshape("img/stat.gif")
    screen.addshape("img/tab.gif")
    screen.addshape("img/close.gif")
    screen.addshape("img/shop_icon_en.gif")
    screen.addshape("img/shop_icon_vi.gif")
    screen.addshape("img/chest_en.gif")
    screen.addshape("img/chest_vi.gif")
    screen.addshape("img/rank_en.gif")
    screen.addshape("img/rank_vi.gif")
    screen.addshape("img/stand.gif")
    screen.addshape("img/back_layer.gif")
    screen.addshape("img/rocket.gif")
    screen.addshape("img/ticket.gif")
    screen.addshape("img/clover.gif")
    screen.addshape("img/potion.gif")
    screen.addshape("img/heart.gif")
    screen.addshape("img/rank_board_en.gif")
    screen.addshape("img/rank_board_vi.gif")
    screen.addshape("img/notice.gif")
    screen.addshape("img/description_board.gif")
    screen.addshape("img/inventory_en.gif")
    screen.addshape("img/inventory_vi.gif")
    screen.addshape("img/instruction_board_en.gif")
    screen.addshape("img/instruction_board_vi.gif")

def addShapeMinigame():
    screen.addshape('minigame_img/mole.gif')
    screen.addshape("minigame_img/bomb.gif")
    screen.addshape('minigame_img/background.gif')
    screen.addshape("minigame_img/0.gif")
    screen.addshape("minigame_img/1.gif")
    screen.addshape("minigame_img/2.gif")
    screen.addshape('minigame_img/3.gif')
    screen.addshape("minigame_img/4.gif")
    screen.addshape("minigame_img/5.gif")
    screen.addshape("minigame_img/6.gif")
    screen.addshape("minigame_img/7.gif")
    screen.addshape("minigame_img/8.gif")
    screen.addshape("minigame_img/9.gif")
    screen.addshape("minigame_img/sttbg.gif")
    screen.addshape("minigame_img/heart.gif")

screen.addshape('img/SMALL.gif')
screen.addshape('img/MEDIUM.gif')
screen.addshape('img/LARGE.gif')
screen.addshape('img/PotionMini.gif')
screen.addshape('img/RocketMini.gif')
screen.addshape('img/Rocket2.gif')
screen.addshape('img/WinTable.gif')
screen.addshape('img/LoseTable.gif')
    
def clearButtons():
    chest.shape("blank")
    rank.shape("blank")
    shop.shape("blank")
    startButton.shape("blank")
    optionsButton.shape("blank")
    instructionsButton.shape("blank")
    minigameButton.shape("blank")
    
def addShapeButtons():
    chest.shape("img/chest_" + str(language) + ".gif")
    rank.shape("img/rank_" + str(language) + ".gif")
    shop.shape("img/shop_icon_" + str(language) + ".gif")
    startButton.shape("img/button1_" + str(language) + ".gif")
    instructionsButton.shape("img/button2_" + str(language) + ".gif")
    optionsButton.shape("img/button3_" + str(language) + ".gif")
    minigameButton.shape("img/button4_" + str(language) + ".gif")
    exitButton.shape("img/exit_" + str(language) + ".gif")

def startGame(x,y):
    clickSound()
    if int(player.ticket) > 0:
        player.ticket = str(int(player.ticket) - 1)
        global moneyBet
        turtle.hideturtle()
        turtle.penup()
        frameTitle.hideturtle()
        logo.hideturtle()
        title1.hideturtle()
        title2.hideturtle()
        startButton.hideturtle()
        optionsButton.hideturtle()
        instructionsButton.hideturtle()
        minigameButton.hideturtle()
        exitButton.hideturtle()
        stat.hideturtle()
        coinUnit.hideturtle()
        insertText.hideturtle()
        tab.hideturtle()
        close.hideturtle()
        closeShop.hideturtle()
        closeBoard.hideturtle()
        shop.hideturtle()
        chest.hideturtle()
        rank.hideturtle()
        insertText.clear()
        moneyBet = screen.textinput("BETTING", "Enter the amount of coins you want to bet(multiple of 100): ")
        while int(moneyBet) > int(player.coin) or int(moneyBet) % 100 != 0 or int(moneyBet) <= 0:
            moneyBet = screen.textinput("BETTING", "Enter the amount of coins you want to bet(multiple of 100): ")
        PlayGame(x,y)

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
    global moneyBet
    if playerName == TrueResultsList[0]:
        WinTableS.speed(0)
        WinTableS.hideturtle()
        WinTableS.penup()
        WinTableS.shape('img/WinTable.gif')
        WinTableS.goto(0, -200)
        WinTableS.showturtle()
        WinTableS.onclick(returnToMainMenu)
        # Need to write code to reward player here
        if mapSize == 'small':
            moneyBet = int(moneyBet) * 2
        if mapSize == 'medium':
            moneyBet = int(moneyBet) * 3
        if mapSize == 'large':
            moneyBet = int(moneyBet) * 4
        player.coin = str(int(player.coin) + int(moneyBet))
        player.winRate = str(int(player.winRate) + 1)
        

    else:
        LoseTableS.speed(0)
        LoseTableS.hideturtle()
        LoseTableS.penup()
        LoseTableS.shape('img/LoseTable.gif')
        LoseTableS.goto(0, -200)
        LoseTableS.showturtle()
        LoseTableS.onclick(returnToMainMenu)
        # Need to write code to deduct coins here
        player.coin = str(int(player.coin) - int(moneyBet))
    updateCoin()

def TraceResult():

    turtle.clear()
    finishLineS.hideturtle()
    if mapChoice == 0:
        screen.bgpic('img/ForestRankTable.gif')
    if mapChoice == 1:
        screen.bgpic('img/BeachRankTable.gif')
    if mapChoice == 2:
        screen.bgpic('img/GalaxyRankTable.gif')
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
    potion1.shape('img/PotionMini.gif')
    potion1.goto(500, -260)
    potion1.showturtle()
    rocket1.speed(0)
    rocket1.hideturtle()
    rocket1.penup()
    rocket1.shape('img/RocketMini.gif')
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
    screen.bgpic(Maps[mapChoice])
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
                if int(player.potion) > 0:
                    potion2.speed(0)
                    potion2.hideturtle()
                    potion2.penup()
                    potion2.shape('img/PotionMini.gif')
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
                            player.potion = str(int(player.potion) - 1)
                            break

            def goFaster(x, y):
                if int(player.rocket) > 0:
                    rocket2.speed(0)
                    rocket2.hideturtle()
                    rocket2.penup()
                    rocket2.shape('img/Rocket2.gif')
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
                            # Need to write code to deduct Rocket
                            player.rocket = str(int(player.rocket) - 1)
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
    finishLineS.shape('img/FinishLine.gif')
    finishLineS.showturtle()


def TraceFinishLineMedium():
    finishLineS.hideturtle()
    finishLineS.penup()
    finishLineS.speed(0)

    finishLineS.goto(260, 45)
    finishLineS.shape('img/FinishLine.gif')
    finishLineS.showturtle()


def TraceFinishLineLarge():
    finishLineS.hideturtle()
    finishLineS.penup()
    finishLineS.speed(0)

    finishLineS.goto(520, 45)
    finishLineS.shape('img/FinishLine.gif')
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
    SmallButton.shape('img/SMALL.gif')
    SmallButton.goto(0, 100)
    SmallButton.showturtle()
    MediumButton.speed(0)
    MediumButton.hideturtle()
    MediumButton.penup()
    MediumButton.shape('img/MEDIUM.gif')
    MediumButton.goto(0, 0)
    MediumButton.showturtle()
    LargeButton.speed(0)
    LargeButton.hideturtle()
    LargeButton.penup()
    LargeButton.shape('img/LARGE.gif')
    LargeButton.goto(0, -100)
    LargeButton.showturtle()
    turtle.update()
    SmallButton.onclick(SetMaptoSmall)
    MediumButton.onclick(SetMaptoMedium)
    LargeButton.onclick(SetMaptoLarge)


def PlayGame(x, y):
# This function is used to draw the characters on the screen to select
    TraceCharacterSelection(-250, 0)

    CharList[0].onclick(PlayerAssign0)
    CharList[1].onclick(PlayerAssign1)
    CharList[2].onclick(PlayerAssign2)
    CharList[3].onclick(PlayerAssign3)
    CharList[4].onclick(PlayerAssign4)
    CharList[5].onclick(PlayerAssign5)



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
    flag = random.randint(1,4)
    screen.bgpic('img/bgmenu' + str(flag) + '.gif')
    turtle.update()
    frameTitle.showturtle()
    logo.showturtle()
    title1.showturtle()
    title2.showturtle()
    startButton.showturtle()
    optionsButton.showturtle()
    instructionsButton.showturtle()
    minigameButton.showturtle()
    exitButton.showturtle()
    stat.showturtle()
    coinUnit.showturtle()
    tab.showturtle()
    close.showturtle()
    closeShop.showturtle()
    closeBoard.showturtle()
    shop.showturtle()
    chest.showturtle()
    rank.showturtle()
    turtle.update()

def instructions(x,y):
    clickSound()
    clearButtons()
    instructionBoard.showturtle()
    instructionBoard.setpos(0,0)
    instructionBoard.shape("img/instruction_board_" + str(language) + ".gif")
    closeInstruction.setpos(425,238)
    insertTextInstruction.hideturtle()
    if language == "en":
        insertTextInstruction.setpos(-340,-130)
        insertTextInstruction.write("    Here at the Pet Kingdom, YOU - a gambler, needs to collect as many \ncoins as possible to prove your wealth. In order to do that, you need to\nenter a betting game where you can double, triple, or even quadruple\nyour coins. However, you need a ticket before entering the race.\n\n    The ticket can be bought in the shop along with other items that will\naid you in the game. Should you run out of coins, don't worry. Participate\nin our minigame, Whack all the moles - the culprít behind our crop\ndevastation and win back the coins. \n\n    Enjoy your time here, and good luck ... my gambler.", align="left", font=("Serifa BT", 15,"bold"))
    elif language == "vi":
        insertTextInstruction.setpos(-340,-150)
        insertTextInstruction.write("    Tại Vương Quốc Thú Cưng, BẠN - một con bạc, cần kiếm được nhiều \nxu nhất có thể để chứng tỏ sự giàu có của mình. Đề làm vậy, bạn cần \nphải tham gia vào trò chơi cá cược để có thể nhân đôi, nhân ba, thậm chí \nnhân bốn lần số xu của bạn. Tuy nhiên, bạn cần một chiếc thẻ trước khi \ntham gia trò chơi.\n\n    Thẻ có thể được mua tại cửa hàng cùng với những vật phẩm sẽ hỗ trợ \nbạn trong trò chơi. Nếu bạn phá sản, đừng lo. Bạn có thể tham gia \nminigame, Đập chuột chũi - những kẻ cướp đã phá hoại mùa màng để \ngiành lại số xu bị cướp mất.\n\n    Chúc bạn có trải nghiệm thật vui vẻ, và chúc may mắn...tay đánh bạc." , align="left", font=("Serifa BT", 15,"bold"))
    instructionRead()
    closeInstruction.showturtle()
    closeInstruction.shape("img/close.gif")
    closeInstruction.onclick(exitInstruction)
    turtle.update()
    
def exitInstruction(x, y):
    clickSound()
    stopInstructionRead()
    instructionBoard.shape("blank")
    closeInstruction.shape("blank")
    insertTextInstruction.clear()
    addShapeButtons()
    turtle.update()

def options(x,y):
    clickSound()
    back_layer.showturtle()
    global language
    global music
    global sound
    language = ""
    music = ""
    sound = ""
    while (language !=  "en" and language != "vi") or (music != "1" and music != "0") or (sound != "1" and sound != "0"):
        language = "en"
        music = "1"
        sound = "1"
        if language == "en":
            music = screen.textinput("Music","1(On)/0(Off):")
            sound = screen.textinput("Sound effect","1(On)/0(Off):")
            language = screen.textinput("Language","en(English)/ vi(Vietnamese):")
        elif language == "vi":
            music = screen.textinput("Nhạc","1(Bật)/0(Tắt):")
            sound = screen.textinput("Hiệu ứng âm thanh","1(Bật)/0(Tắt):")
            language = screen.textinput("Ngôn ngữ","en(Tiếng Anh)/ vi(Tiếng Việt):")
        if music == "0":
            pygame.mixer.pause()
        if music == "1":
            pygame.mixer.unpause()
        if sound == "0":
            sound = "0"
        if sound == "1":
            sound = "1"
    addShapeButtons()
    initMainMenu(player, resolution)
    back_layer.hideturtle()
    return
    close.onclick(clearTab)
    return
    turtle.update()

isClose = 0
def minigame(x,y):
    clickSound()
    global clock, lives, score, num, isClose
    #Set time and score
    clock = 30
    score = 0
    score_max = 15
    lives = int(player.heart) + 1
    #Set up background
    addShapeMinigame()
    bg.penup()
    bg.speed(0)
    bg.setpos(-68.5, 0) #coordinate of the middle of background
    bg.shape('minigame_img/background.gif')
    sttbg.penup()
    sttbg.speed(0)
    sttbg.setpos(492,0)
    sttbg.shape('minigame_img/sttbg.gif')
    closeMiniGame.shape("img/close.gif")
    closeMiniGame.penup()
    closeMiniGame.setpos(370,250)
    closeMiniGame.onclick(closeMG)
    #insert turtle bar
    while clock > 0 and lives > 0:
        if isClose == 1:
            isClose = 0
            break
        num = ["minigame_img/0.gif","minigame_img/1.gif","minigame_img/2.gif","minigame_img/3.gif","minigame_img/4.gif","minigame_img/5.gif","minigame_img/6.gif","minigame_img/7.gif","minigame_img/8.gif","minigame_img/9.gif"]
        t = random.randint(1,28)
        if t == 1 or t == 15 or t == 22:
            mole1()
        if t == 2 or t == 16 or t == 23:
            mole2()
        if t == 3 or t == 17 or t == 24:
            mole3()
        if t == 4 or t == 18 or t == 25:
            mole4()
        mole_4.onclick(plus)
        if t == 5 or t == 19 or t == 26:
            mole5()
        mole_5.onclick(plus)
        if t == 6 or t == 20 or t == 27:
            mole6()
        mole_6.onclick(plus)
        if t == 7 or t == 21 or t == 28:
            mole7()
        mole_7.onclick(plus)
        if t == 8:
            bomb1()
        if t == 9:
            bomb2()
        if t == 10:
            bomb3()
        if t == 11:
            bomb4()
        if t == 12:
            bomb5()
        if t == 13:
            bomb6()
        if t == 14:
            bomb7()
        clock = clock - 1
        score_item()
        dplives()
        min()
    #Cong coin cho nguoi choi  
    if score >= score_max:
        player.coin = str(int(player.coin) + 2000)
        updateCoin()
    if lives == 0 or lives == 1:
        player.heart = str(0)
    else:
        player.heart = str(int(lives)-1)
    score = 0
    clock = 30
    bg.shape("blank")

    #character
    mole_1.shape("blank")
    mole_2.shape("blank")
    mole_3.shape("blank")
    mole_4.shape("blank")
    mole_5.shape("blank")
    mole_6.shape("blank")
    mole_7.shape("blank")
    #bomb
    bomb_1.shape("blank")
    bomb_2.shape("blank")
    bomb_3.shape("blank")
    bomb_4.shape("blank")
    bomb_5.shape("blank")
    bomb_6.shape("blank")
    bomb_7.shape("blank")
    #heart
    heart_1.shape("blank")
    heart_2.shape("blank")
    heart_3.shape("blank")

    #Stt
    fm.shape("blank")
    sm.shape("blank")
    ds1.shape("blank")
    ds2.shape("blank")
    dsc.shape("blank")
    closeMiniGame.shape("blank")
    sttbg.shape("blank")
    turtle.update()
    

def closeMG(x,y):
    clickSound()
    global clock, score
    global isClose
    isClose = 1
    score_max = 15
    if score >= score_max:
        player.coin = str(int(player.coin) + 2000)
        updateCoin()
    if lives == 0 or lives == 1:
        player.heart = str(0)
    else:
        player.heart = str(int(lives) - 1)
    score = 0
    clock = 30
    turtle.tracer(False)
    bg.shape("blank")

    #character
    mole_1.shape("blank")
    mole_2.shape("blank")
    mole_3.shape("blank")
    mole_4.shape("blank")
    mole_5.shape("blank")
    mole_6.shape("blank")
    mole_7.shape("blank")
    #bomb
    bomb_1.shape("blank")
    bomb_2.shape("blank")
    bomb_3.shape("blank")
    bomb_4.shape("blank")
    bomb_5.shape("blank")
    bomb_6.shape("blank")
    bomb_7.shape("blank")
    #heart
    heart_1.shape("blank")
    heart_2.shape("blank")
    heart_3.shape("blank")

    #Stt
    fm.shape("blank")
    sm.shape("blank")
    ds1.shape("blank")
    ds2.shape("blank")
    dsc.shape("blank")
    closeMiniGame.shape("blank")
    sttbg.shape("blank")
    turtle.tracer(True)
    
def plus(x, y):
    whackSound()
    global score
    score = score + 1
    
def minus(x, y):
    wrongSound()
    global lives
    lives = lives - 1
    #print("day la lives", lives)
    
def heart1():
    heart_1.speed(0)
    heart_1.penup()
    heart_1.setpos(364,290)
    heart_1.shape("minigame_img/heart.gif")
    turtle.update()
    
def heart2():
    heart_2.speed(0)
    heart_2.penup()
    heart_2.goto(324,290)
    heart_2.shape("minigame_img/heart.gif")
    turtle.update()
    
def heart3():
    heart_3.speed(0)
    heart_3.penup()
    heart_3.setpos(284,290)
    heart_3.shape("minigame_img/heart.gif")
    turtle.update()
    
#Set Mole
def mole1():
    mole_1.speed(0)
    mole_1.up() 
    mole_1.goto(-297, 20)
    mole_1.down()
    mole_1.showturtle()
    mole_1.shape("minigame_img/mole.gif")
    mole_1.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_1.hideturtle()
    turtle.update()


def mole2():
    turtle.tracer(False)
    mole_2.speed(0)
    mole_2.up()
    mole_2.goto(8, 6)
    mole_2.down()
    mole_2.showturtle()
    mole_2.shape("minigame_img/mole.gif")
    mole_2.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_2.hideturtle()
    turtle.update()

def mole3():
    turtle.tracer(False)
    mole_3.speed(0)
    mole_3.up()
    mole_3.goto(-210, -79)
    mole_3.down()
    mole_3.showturtle()
    mole_3.shape("minigame_img/mole.gif")
    mole_3.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_3.hideturtle()
    turtle.update()

def mole4():
    turtle.tracer(False)
    mole_4.speed(0)
    mole_4.up()
    mole_4.goto(170, -82)
    mole_4.down()
    mole_4.showturtle()
    mole_4.shape("minigame_img/mole.gif")
    mole_4.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_4.hideturtle()
    turtle.update()

def mole5():
    turtle.tracer(False)
    mole_5.speed(0)
    mole_5.up()
    mole_5.goto(-329, -196)
    mole_5.down()
    mole_5.showturtle()
    mole_5.shape("minigame_img/mole.gif")
    mole_5.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_5.hideturtle()
    turtle.update()

def mole6():
    turtle.tracer(False)
    mole_6.speed(0)
    mole_6.up()
    mole_6.goto(-22, -182)
    mole_6.down()
    mole_6.showturtle()
    mole_6.shape("minigame_img/mole.gif")
    mole_6.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_6.hideturtle()
    turtle.update()

def mole7():
    turtle.tracer(False)
    mole_7.speed(0)
    mole_7.up()
    mole_7.goto(277, -206)
    mole_7.down()
    mole_7.showturtle()
    mole_7.shape("minigame_img/mole.gif")
    mole_7.onclick(plus)
    turtle.update()
    time.sleep(0.6)
    mole_7.hideturtle()
    turtle.update()

#Set bomb        
def bomb1():
    bomb_1.speed(0)
    bomb_1.up()
    bomb_1.goto(-297, 20)
    bomb_1.down()
    bomb_1.showturtle()
    bomb_1.shape("minigame_img/bomb.gif")
    bomb_1.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_1.hideturtle()
    turtle.update()
    
def bomb2():
    bomb_2.speed(0)
    bomb_2.up()
    bomb_2.goto(8, 6)
    bomb_2.down()
    bomb_2.showturtle()
    bomb_2.shape("minigame_img/bomb.gif")
    bomb_2.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_2.hideturtle()
    turtle.update()
    
def bomb3():
    bomb_3.speed(0)
    bomb_3.up()
    bomb_3.goto(-210, -79)
    bomb_3.down()
    bomb_3.showturtle()
    bomb_3.shape("minigame_img/bomb.gif")
    bomb_3.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_3.hideturtle()
    turtle.update()
    
def bomb4():
    bomb_4.speed(0)
    bomb_4.up()
    bomb_4.goto(170, -82)
    bomb_4.down()
    bomb_4.showturtle()
    bomb_4.shape("minigame_img/bomb.gif")
    bomb_4.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_4.hideturtle()
    turtle.update()
    
def bomb5():
    bomb_5.speed(0)
    bomb_5.up()
    bomb_5.goto(-329, -196)
    bomb_5.down()
    bomb_5.showturtle()
    bomb_5.shape("minigame_img/bomb.gif")
    bomb_5.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_5.hideturtle()
    turtle.update()
    
def bomb6():
    bomb_6.speed(0)
    bomb_6.up()
    bomb_6.goto(-22, -182)
    bomb_6.down()
    bomb_6.showturtle()
    bomb_6.shape("minigame_img/bomb.gif")
    bomb_6.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_6.hideturtle()
    turtle.update()
    
def bomb7():
    bomb_7.speed(0)
    bomb_7.up()
    bomb_7.goto(277, -206)
    bomb_7.down()
    bomb_7.showturtle()
    bomb_7.shape("minigame_img/bomb.gif")
    bomb_7.onclick(minus)
    turtle.update()
    time.sleep(0.6)
    bomb_7.hideturtle()
    turtle.update()
    
#STT
def min():
    global clock
    fmin()
    smin()
    
def fmin():
    global clock
    fm.speed(0)
    fm.penup()
    fm.setpos(470, 77.5)
    fmin1 = int(clock / 10)
    fm.shape(num[fmin1])
    turtle.update()

def smin():
    global clock
    sm.speed(0)
    sm.penup()
    sm.setpos(514, 77.5)
    smin1 = int(clock % 10)
    sm.shape(num[smin1])
    turtle.update()

def dplives():
    global lives
    if lives == 1:
        heart_3.hideturtle()
        heart_2.hideturtle()
        heart1()
    elif lives == 2:
        heart_3.hideturtle()
        heart1()
        heart2()
    elif lives == 3: 
        heart1()
        heart2()
        heart3()
    turtle.update()
    
def score_item():
    global score
    def s1():
        ds1.speed(0)
        ds1.up()
        ds1.goto(470, -72.5)
        ds1.down
        ds1.shape(num[int(score / 10)])
        turtle.update()
    def s2():
        ds2.speed(0)
        ds2.up()
        ds2.goto(514, -72.5)
        ds2.down
        ds2.shape(num[int(score % 10)])
        turtle.update()
    def s_center():
        dsc.speed(0)
        dsc.up()
        dsc.goto(492, -72.5)
        dsc.down
        dsc.shape(num[int(score % 10)])
        turtle.update()
    if score < 10:
        s_center()
    else:
        dsc.hideturtle()
        s1()
        s2()

def clearTab(x,y):
    clickSound()
    back_layer.hideturtle()
    tab.hideturtle()
    close.hideturtle()
    turtle.update()

def exitGame(x,y):
    clickSound()
    time.sleep(1)
    if player.id == len(playerData):
        player.createNewData(playerData)
    else:
        player.overwriteData(playerData)
    writeData()
    quit()
    
def addItemsShop():
    stand.shape("img/stand.gif")
    rocketItem.shape("img/rocket.gif")
    ticketItem.shape("img/ticket.gif")
    luckyCloverItem.shape("img/clover.gif")
    potionItem.shape("img/potion.gif")
    heartItem.shape("img/heart.gif")
    closeShop.shape("img/close.gif")
    turtle.update()
    
def removeItemsShop():
    insertTextPrice.clear()
    stand.shape("blank")
    rocketItem.shape("blank")
    ticketItem.shape("blank")
    luckyCloverItem.shape("blank")
    potionItem.shape("blank")
    heartItem.shape("blank")
    closeShop.shape("blank")
    turtle.update()
    
def rewriteTextShop():
    insertTextPrice.hideturtle()    
    insertTextPrice.setpos(-265, 38)     
    insertTextPrice.color("#66022D")
    insertTextPrice.write("2500US               4000US               4500US                1500US", align="left", font=("Serifa BT", 15,"bold"))
    insertTextPrice.setpos(-265, -113)
    insertTextPrice.write("2000U", align="left", font=("Serifa BT", 15,"bold"))
    turtle.update()
    
def openShop(x,y):
    clickSound()
    clearButtons()
    #back_layer.showturtle()
    stand.showturtle()
    closeShop.showturtle()
    rocketItem.showturtle()
    ticketItem.showturtle()
    potionItem.showturtle()
    heartItem.showturtle()
    luckyCloverItem.showturtle()
    potionItem.showturtle()
    stand.setpos(0,-50)
    rocketItem.setpos(-240,120)
    ticketItem.setpos(-70,120)
    luckyCloverItem.setpos(100,120)
    potionItem.setpos(270,120)
    heartItem.setpos(-240,-30)
    closeShop.setpos(375,210)
    addItemsShop()
    insertTextPrice.hideturtle()    
    insertTextPrice.setpos(-265, 38)     
    insertTextPrice.color("#66022D")
    insertTextPrice.write("2500US               4000US               4500US                1500US", align="left", font=("Serifa BT", 15,"bold"))
    insertTextPrice.setpos(-265, -113)
    insertTextPrice.write("2000U", align="left", font=("Serifa BT", 15,"bold"))
    turtle.listen()
    closeShop.onclick(exitShop)
    rocketItem.onclick(buyingItem1)
    ticketItem.onclick(buyingItem2)
    luckyCloverItem.onclick(buyingItem3)
    potionItem.onclick(buyingItem4)
    heartItem.onclick(buyingItem5)
    rocketItem.onclick(descriptionItem1, btn = 3)
    ticketItem.onclick(descriptionItem2, btn = 3)
    luckyCloverItem.onclick(descriptionItem3, btn = 3)
    potionItem.onclick(descriptionItem4, btn = 3)
    heartItem.onclick(descriptionItem5, btn = 3)
    turtle.mainloop()
    turtle.update()

def removeItemsInventory():
    rocketItem1.clear()
    ticketItem1.clear()
    luckyCloverItem1.clear()
    potionItem1.clear()
    heartItem1.clear()
    inventory.shape("blank")
    rocketItem1.shape("blank")
    ticketItem1.shape("blank")
    luckyCloverItem1.shape("blank")
    potionItem1.shape("blank")
    heartItem1.shape("blank")
    
    closeInventory.shape("blank")
    turtle.update()

def processInventory():
    x0 = xtemp = -240
    y0 = ytemp = 0
    _x = 0
    _y = 0
    nl = 0
    for i in range(1,6):
        if int(player.rocket) != 0 and i == 1:
            rocketItem1.showturtle()
            rocketItem1.setpos(x0 + _x, y0 + _y)
            _x += 160;
            rocketItem1.shape("img/rocket.gif")
            nl += 1
            rocketItem1.write("X " + str(player.rocket), align="left", font=("Serifa BT", 30,"bold"))
        if int(player.ticket) != 0 and i == 2:
            ticketItem1.showturtle()
            ticketItem1.setpos(x0 + _x, y0 + _y)
            _x += 160;
            ticketItem1.shape("img/ticket.gif")
            nl += 1
            ticketItem1.write("X " + str(player.ticket), align="left", font=("Serifa BT", 30,"bold"))
        if int(player.clover) != 0 and i == 3:
            luckyCloverItem1.showturtle()
            luckyCloverItem1.setpos(x0 + _x, y0 + _y)
            _x += 160;
            luckyCloverItem1.shape("img/clover.gif")
            nl += 1
            luckyCloverItem1.write("X " + str(player.clover), align="left", font=("Serifa BT", 30,"bold"))
        if int(player.potion) != 0 and i == 4:
            potionItem1.showturtle()
            potionItem1.setpos(x0 + _x, y0 + _y)
            _x += 160;
            potionItem1.shape("img/potion.gif")
            nl += 1
            potionItem1.write("X " + str(player.potion), align="left", font=("Serifa BT", 30,"bold"))
        if int(player.potion) != 0 and i == 5:
            heartItem1.showturtle()
            heartItem1.setpos(x0 + _x, y0 + _y)
            _x += 160;
            heartItem1.shape("img/heart.gif")
            nl += 1
            heartItem1.write("X " + str(player.heart), align="left", font=("Serifa BT", 30,"bold"))
        if nl % 4 == 0:
            _y -= 160
            _x = 0
    turtle.update()    

def openInventory(x,y):
    clickSound()
    clearButtons()
    inventory.showturtle()
    inventory.setpos(0,0)
    inventory.shape("img/inventory_" + str(language) + ".gif")
    processInventory()
    closeInventory.setpos(425,238)
    closeInventory.shape("img/close.gif")
    insertTextInventory.hideturtle()
    insertTextInventory.setpos(-220,-40)
#    insertTextInventory.write("x" + str(player.rocket) + "              x" + str(player.ticket)+ "               x" + str(player.clover) + "                  x" + str(player.potion), move=False, align="left", font=("Serifa BT", 15,"bold"))
    closeInventory.onclick(exitInventory)
    turtle.update()
    
def exitInventory(x, y):
    clickSound()
    removeItemsInventory()
    addShapeButtons()
    turtle.update()

def openRankingBoard(x,y):
    clickSound()
    clearButtons()
    insertTextRank.hideturtle()
    closeBoard.showturtle()
    rankBoard.showturtle()
    rankBoard.setpos(0,0)
    rankBoard.shape("img/rank_board_" + str(language) + ".gif")
    distance = 70
    sortData = []
    sortData = top10Player()
    insertTextRank.color("yellow")
    for i in range(0, 5):
        insertTextRank.setpos(-270, 180 - distance)
        if player.username == str(sortData[i][0]):
            if language == "en":
                nameIndicate = "--> YOU <--"
            elif language == "vi":
                nameIndicate = "--> BẠN <--"
        else:
            nameIndicate = ""
        if language == "en":
            insertTextRank.write(str(i+1)+ "  "  + str(sortData[i][0]) + "   WIN: " + str(sortData[i][1]) + "   COINS: " + str(sortData[i][3]) + "US" + "  " + nameIndicate, align="left", font=("Serifa BT", 15,"bold"))
        elif language == "vi":
            insertTextRank.write(str(i+1)+ "  "  + str(sortData[i][0]) + "   SỐ TRẬN THẮNG: " + str(sortData[i][1]) + "   XU: " + str(sortData[i][3]) + "US" + "  " + nameIndicate, align="left", font=("Serifa BT", 15,"bold"))
        distance += 70
    closeBoard.setpos(425,238)
    closeBoard.shape("img/close.gif")
    closeBoard.onclick(exitRankingBoard)
    turtle.update()

def clearRankBoard():
    insertTextRank.clear()
    rankBoard.shape("blank")
    closeBoard.shape("blank")
    turtle.update()
    
def exitRankingBoard(x, y):
    clickSound()
    clearRankBoard()
    addShapeButtons()
    sortData = []
    turtle.update()
    
    
def updateCoin():
    insertText.clear()
    insertText.hideturtle()    
    insertText.setpos(-485,222)     
    insertText.color("#654321")
    insertText.write(player.coin, move=False, align="left", font=("Serifa BT", 30,"normal"))
    insertText.setpos(-550,192)
    insertText.write(player.username, move=False, align="left", font=("Serifa BT", 15,"normal"))
    insertText.setpos(-550,172)
    if language == "en":
        insertText.write("Win: " + str(player.winRate), move=False, align="left", font=("Serifa BT", 15,"normal"))
    else:
        insertText.write("Thắng: " + str(player.winRate), move=False, align="left", font=("Serifa BT", 15,"normal"))
    turtle.update()
        
def buyingItem1(x,y):
    if (int(player.coin) - 2500) >= 0 and int(player.rocket) < 3:
        player.coin = str(int(player.coin) - 2500)
        player.rocket = str(int(player.rocket) + 1)
        if language == "en":
            item = "5th edition rocket"
        elif language == "vi":
            item = "Tên lửa thế hệ 5"
        updateCoin()
        value = "success"
        showNotice(value, item) #buy successfully or not successfully
    else:
        value = "fail"
        if language == "en":
            item = "5th edition rocket"
        elif language == "vi":
            item = "Tên lửa thế hệ 5"
        showNotice(value, item)
    turtle.update()
    
def buyingItem2(x,y):
    if (int(player.coin) - 4000) >= 0 and int(player.ticket) < 3:
        player.coin = str(int(player.coin) - 4000)
        player.ticket = str(int(player.ticket) + 1)
        if language == "en":
            item = "Racing ticket"
        elif language == "vi":
            item = "Vé đua"
        updateCoin()
        value = "success"
        showNotice(value, item) #buy successfully or not successfully
    else:
        value = "fail"
        if language == "en":
            item = "Racing ticket"
        elif language == "vi":
            item = "Vé đua"
        showNotice(value, item)
    turtle.update()

def buyingItem3(x,y):
    if (int(player.coin) - 4500) >= 0 and int(player.clover) < 1:
        player.coin = str(int(player.coin) - 4500)
        player.clover = str(int(player.clover) + 1)
        if language == "en":
            item = "Clover leaf"
        elif language == "vi":
            item = "Cỏ may mắn"
        updateCoin()
        value = "success"
        showNotice(value, item) #buy successfully or not successfully
    else:
        value = "fail"
        if language == "en":
            item = "Clover leaf"
        elif language == "vi":
            item = "Cỏ may mắn"
        showNotice(value, item)
    turtle.update()

def buyingItem4(x,y):
    if (int(player.coin) - 1500) >= 0 and int(player.potion) < 3:
        player.coin = str(int(player.coin) - 1500)
        player.potion = str(int(player.potion) + 1)
        updateCoin()
        value = "success"
        if language == "en":
            item = "Deadline potion"
        else:
            item = "Thần dược Deadline"
        showNotice(value,item) #buy successfully or not successfully
    else:
        value = "fail"
        if language == "en":
            item = "Deadline potion"
        else:
            item = "Thần dược Deadline"
        showNotice(value,item)
    turtle.update()

def buyingItem5(x,y):
    if (int(player.coin) - 2000) >= 0 and int(player.heart) < 3:
        player.coin = str(int(player.coin) - 2000)
        player.heart = str(int(player.heart) + 1)
        updateCoin()
        value = "success"
        if language == "en":
            item = "Lives"
        else:
            item = "Mạng"
        showNotice(value,item) #buy successfully or not successfully
    else:
        value = "fail"
        if language == "en":
            item = "Lives"
        else:
            item = "Mạng"
        showNotice(value,item)
    turtle.update()
    
def descriptionItem1(x,y):
    clickSound()
    insertTextPrice.clear()
    description.shape("img/description_board.gif")
    description.showturtle()
    description.setpos(0,0)
    insertTextDescription.hideturtle()
    insertTextDescription.setpos(0,50)
    insertTextDescription.color("red")
    if language == "en":
        insertTextDescription.write("5th edition Rocket", move=False, align="center", font=("Serifa BT", 20,"bold"))
    else:
        insertTextDescription.write("Tên lửa thế hệ 5", move=False, align="center", font=("Serifa BT", 20,"bold"))
    insertTextDescription.setpos(0,-20)
    insertTextDescription.color("white")
    if language == "en":
        insertTextDescription.write("Rocket boost your character's \n       speed by 0.25 seconds", move=False, align="center", font=("Serifa BT", 15,"bold"))
    else:
        insertTextDescription.write(" Tên lửa gia tăng tốc độ nhân vật  \n     của bạn trong 0.25 giây", move=False, align="center", font=("Serifa BT", 15,"bold"))
    turtle.update()
    time.sleep(1.5)
    insertTextDescription.clear()
    description.shape("blank")
    rewriteTextShop()
    turtle.update()
    
def descriptionItem2(x,y):
    clickSound()
    insertTextPrice.clear()
    description.shape("img/description_board.gif")
    description.showturtle()
    description.setpos(0,0)
    insertTextDescription.hideturtle()
    insertTextDescription.setpos(0,50)
    insertTextDescription.color("blue")
    if language == "en":
        insertTextDescription.write("Tickets", move=False, align="center", font=("Serifa BT", 20,"bold"))
    else:
        insertTextDescription.write("Vé đua", move=False, align="center", font=("Serifa BT", 20,"bold"))
    insertTextDescription.setpos(0,-20)
    insertTextDescription.color("white")
    if language == "en":
        insertTextDescription.write("1 ticket grants an entrance into the bet", move=False, align="center", font=("Serifa BT", 15,"bold"))
    else:
        insertTextDescription.write("1 vé đua cho bạn 1 lượt tham gia cá cược đua thú", move=False, align="center", font=("Serifa BT", 15,"bold"))
    turtle.update()
    time.sleep(1.5)
    insertTextDescription.clear()
    description.shape("blank")
    rewriteTextShop()
    turtle.update()

def descriptionItem3(x,y):
    clickSound()
    insertTextPrice.clear()
    description.shape("img/description_board.gif")
    description.showturtle()
    description.setpos(0,0)
    insertTextDescription.hideturtle()
    insertTextDescription.setpos(0,50)
    insertTextDescription.color("green")
    if language == "en":
        insertTextDescription.write("Lucky clover", move=False, align="center", font=("Serifa BT", 20,"bold"))
    else:
        insertTextDescription.write("Cỏ may mắn", move=False, align="center", font=("Serifa BT", 20,"bold"))
    insertTextDescription.setpos(0,-20)
    insertTextDescription.color("white")
    if language == "en":
        insertTextDescription.write("                    This lucky charm \n permanently increases your lucky by 10% \n             can only be purchased once.", move=False, align="center", font=("Serifa BT", 15,"bold"))
    else:
        insertTextDescription.write("                    Chiếc cỏ bốn lá này \n   có thể tăng chỉ số mắn cho người chơi \n     lên đến 10%, và chỉ có thể mua một lần.",move=False, align="center", font=("Serifa BT", 15,"bold"))
    turtle.update()
    time.sleep(2)
    insertTextDescription.clear()
    description.shape("blank")
    rewriteTextShop()
    turtle.update()

def descriptionItem4(x,y):
    clickSound()
    insertTextPrice.clear()
    description.shape("img/description_board.gif")
    description.showturtle()
    description.setpos(0,0)
    insertTextDescription.hideturtle()
    insertTextDescription.setpos(0,50)
    insertTextDescription.color("blue")
    if language == "en":
        insertTextDescription.write("The Deadline Potion", move=False, align="center", font=("Serifa BT", 20,"bold"))
    else:
        insertTextDescription.write("Thuốc Deadline", move=False, align="center", font=("Serifa BT", 20,"bold"))
    insertTextDescription.setpos(0,-40)
    insertTextDescription.color("white")
    if language == "en":
        insertTextDescription.write("A potion which temporarily slows down the speed of\n the pet currently in the 1st place for 0.25 second", move=False, align="center", font=("Serifa BT", 15,"bold"))
    else:
        insertTextDescription.write("    Đây là thuốc Deadline \n    làm tạm thời giảm tốc thú cưng \n  đang đứng đầu trong 0.25 giây", move=False, align="center", font=("Serifa BT", 15,"bold"))
    turtle.update()
    time.sleep(1.5)
    insertTextDescription.clear()
    description.shape("blank")
    rewriteTextShop()
    turtle.update()

def descriptionItem5(x,y):
    clickSound()
    insertTextPrice.clear()
    description.shape("img/description_board.gif")
    description.showturtle()
    description.setpos(0,0)
    insertTextDescription.hideturtle()
    insertTextDescription.setpos(0,50)
    insertTextDescription.color("red")
    if language == "en":
        insertTextDescription.write("Live", move=False, align="center", font=("Serifa BT", 20,"bold"))
    else:
        insertTextDescription.write("Mạng", move=False, align="center", font=("Serifa BT", 20,"bold"))
    insertTextDescription.setpos(0,-20)
    insertTextDescription.color("white")
    if language == "en":
        insertTextDescription.write("A player get an extra live \n          for the minigame", move=False, align="center", font=("Serifa BT", 15,"bold"))
    else:
        insertTextDescription.write("Người chơi có thêm 1 mạng \n        trong minigame", move=False, align="center", font=("Serifa BT", 15,"bold"))
    turtle.update()
    time.sleep(1.5)
    insertTextDescription.clear()
    description.shape("blank")
    rewriteTextShop()
    turtle.update()

def showNotice(value, item):
    clickSound()
    insertTextPrice.clear()
    clearButtons()
    insertNotice.showturtle()
    noticeBoard.showturtle()
    insertNotice.hideturtle()
    insertNotice.setpos(0,100)
    noticeBoard.setpos(0,0)
    noticeBoard.shape("img/notice.gif")
    insertNotice.color("white")
    if value == "success":
        if language == "en":
            insertNotice.write("PURCHASE SUCCESSFUL",align="center", font=("Serifa BT", 30,"bold"))
        else:
            insertNotice.write("MUA HÀNG THÀNH CÔNG",align="center", font=("Serifa BT", 30,"bold"))
        insertNotice.setpos(0,-70)
        if language == "en":
            insertNotice.write("Thank for purchasing " + item + " item!",align="center", font=("Serifa BT", 23,"normal"))
        else:
            insertNotice.write("Cám ơn bạn đã mua " + item + " item!",align="center", font=("Serifa BT", 23,"normal"))
    else :
        value = "fail"
        insertNotice.write("PURCHASE FAIL",align="center", font=("Serifa BT", 30,"bold"))
        insertNotice.setpos(0,-70)
        if language == "en":
            insertNotice.write("Fail, you don't have enough US to buy\n" + item + " item or your chest is full. \nPlease check your inventory!",align="center", font=("Serifa BT", 23,"normal"))
        else:
            insertNotice.write("Thất bại, bạn không có đủ US để mua \n" + item + " hoặc rương của bạn đã đầy. \nVui lòng kiểm tra lại rương!",align="center", font=("Serifa BT", 23,"normal"))
    turtle.update()
    time.sleep(1)
    insertNotice.clear()
    noticeBoard.shape("blank")
    rewriteTextShop()
    addShapeButtons()
    turtle.update()


def exitShop(x,y):
    clickSound()
    removeItemsShop()
    addShapeButtons()
    turtle.update()
    return

def initBackground(player, resolution):
    #play music on separate thread (in background)
    mixer.music.load(os.path.join("soundtrack","menu_st1.mp3"))
    mixer.music.load(os.path.join("soundtrack","menu_st2.mp3"))
    mixer.music.load(os.path.join("soundtrack","menu_st3.mp3"))
    channel0.play(menu_st, loops = -1)
    #screen setting
    screen.title("PET-BET RACING GAME")
    print(resolution.width,resolution.height)
    newWidth = int(resolution.width)
    newHeight = int(resolution.height)
    screen.setup(newWidth, newHeight)
    #insert background
    flag = random.randint(1,4)
    screen.bgpic('img/bgmenu' + str(flag) + '.gif')
    addShape()
    #insert title_frame
    frameTitle.setpos(115,190)
    frameTitle.shape("img/cloud-sign.gif")
    #insert logo
    logo.setpos(-165,210)
    logo.shape("img/logo.gif")
    #insert title1 "Pet"
    title1.setpos(80,220)
    title1.shape("img/title1.gif")
    #insert title2 "bet racing"
    title2.setpos(120,160)
    title2.shape("img/title2.gif")
    #insert stat
    stat.setpos(-440,230)
    stat.shape("img/stat.gif")
    #insert coin symbol
    coinUnit.setpos(-520,242)
    coinUnit.shape("img/coin.gif")
    insertText.hideturtle()    
    insertText.setpos(-485,222)     
    insertText.color("#654321")
    insertText.write(player.coin, move=False, align="left", font=("Serifa BT", 30,"normal"))
    insertText.setpos(-550,192)
    insertText.write(player.username, move=False, align="left", font=("Serifa BT", 15,"normal"))
    insertText.setpos(-550,172)
    if language == "en":
        insertText.write("Win: " + str(player.winRate), move=False, align="left", font=("Serifa BT", 15,"normal"))
    elif language == "vi":
        insertText.write("Thắng: " + str(player.winRate), move=False, align="left", font=("Serifa BT", 15,"normal"))
    turtle.update()
        
def initMainMenu(player, resolution):
    addShapeButtons()
    #insert chest icon
    chest.setpos(500,100)
    #insert rank icon
    rank.setpos(500,-20)
    #insert "SHOP" item
    shop.setpos(500,220)
    #insert "START" button
    startButton.setpos(0,30)
    #insert "INSTRUCTIONS" button
    instructionsButton.setpos(0,-60)
    #insert "OPTIONS" button
    optionsButton.setpos(0,-150)
    #insert "MINIGAME" button
    minigameButton.setpos(0,-240)
    #insert "EXIT" button
    if resolution.width >= 1100 and resolution.height >= 620:
        exitButton.setpos(480,300)
    else:
        exitButton.setpos(300,300)

    #insert back layer
    back_layer.shape("img/back_layer.gif")
    back_layer.hideturtle()
    
    startButton.onclick(startGame)
    optionsButton.onclick(options)
    instructionsButton.onclick(instructions)
    minigameButton.onclick(minigame)
    exitButton.onclick(exitGame)
    shop.onclick(openShop)
    chest.onclick(openInventory)
    rank.onclick(openRankingBoard)
    turtle.update()
    
def readData():
    data = []
    with open('data/player.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
def writeData():
    with open('data/player.csv','w', newline='') as f:
        writeFile= csv.writer(f)
        writeFile.writerow(['username','winRate','password','coin', 'rocket', 'ticket', 'clover', 'potion', 'heart'])
        for i in range(1,len(playerData)):
            writeFile.writerow([playerData[i][0], playerData[i][1], playerData[i][2], playerData[i][3], playerData[i][4], playerData[i][5], playerData[i][6], playerData[i][7], playerData[i][8]])

class Player:
    #constructor
    def __init__(self, id, username, winRate, password, coin, rocket, ticket, clover, potion, heart):
        self.id = id
        self.username = username
        self.winRate = winRate
        self.password = password
        self.coin = coin
        self.rocket = rocket
        self.ticket = ticket
        self.clover = clover
        self.potion = potion
        self.heart = heart
    def displayInfo(self):
        print(self.id, self.username, self.winRate, self.password, self.coin, self.rocket, self.ticket, self.clover, self.potion, self.heart)
    def renameUsername(self, username):
        self.username = username
    def updateCoin(self, coin):
        self.coin = coin
    def updateWinRate(self, winRate):
        self.winRate = winRate
    def updatePassword(self, password):
        self.password = password
    def overwriteData(self, playerData):
        playerData[self.id][1] = self.winRate
        playerData[self.id][2] = self.password
        playerData[self.id][3] = self.coin
        playerData[self.id][4] = self.rocket
        playerData[self.id][5] = self.ticket
        playerData[self.id][6] = self.clover
        playerData[self.id][7] = self.potion
        playerData[self.id][8] = self.heart
    def createNewData(self, playerData):
        playerData.append([self.username, self.winRate, self.password, self.coin, self.rocket, self.ticket, self.clover, self.potion, self.heart])


def top10Player():
    sortedData = []
    sortedData = readData()
    sortedData.pop(0)
    for i in range(0,len(sortedData)):
        sortedData[i][3] = int(sortedData[i][3])
    sortedData.sort(key = lambda l:l[3], reverse=True)
#    print("Player Data: ",playerData)
    return sortedData

class Resolution:
    #constructor
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
    def displayResolution(self):
        print(str(self.width) + " and " + str(self.height))
    def updateResolution(self, width, height):
        self.width = int(width)
        self.height = int(height)

def resolutionSetUp(resolution):
    screenSize = [[1200,645],[1200,645],[1370,736],[1600,900]]
    while resolution.width not in screenSize[1:4][0] and resolution.height not in screenSize[1:4][1]:
        code = turtle.numinput("Choose screen resolution","\n 0: default\n 1: 1200 x 645\n 2: 1370 x 736\n 3: 1600 x 900\nYour selection: ")
        if code > len(screenSize):
            code = 0
        resolution.width = screenSize[int(code)][0]
        resolution.height = screenSize[int(code)][1]

screen.bgpic('img/bg-1.gif')
#file processing
playerData = readData()
username = screen.textinput("Player Information:", "Enter your name: ")
password = screen.textinput("Player Information:", "Enter your password (numbers only): ")
winRate, coin, rocket, ticket, clover, potion, heart = 0, 0, 0, 0, 0, 0, 0
for i in range(1, len(playerData)):
    if playerData[i][0] == username:
        if playerData[i][2] != password:
            quit()
        else:
            id = i
            winRate = playerData[i][1]
            password = playerData[i][2]
            coin = playerData[i][3]
            rocket = playerData[i][4]
            ticket = playerData[i][5]
            clover = playerData[i][6]
            potion = playerData[i][7]
            heart = playerData[i][8]
            break       
    else:
        id = len(playerData)
resolution = Resolution(0, 0)
resolutionSetUp(resolution)
player = Player(id, username, winRate, password, coin, rocket, ticket, clover, potion, heart)
playerName = player.username
initBackground(player, resolution)
initMainMenu(player, resolution)
