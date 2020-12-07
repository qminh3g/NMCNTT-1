from ImageAssets import *
import random
import turtle as t
import time

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
        # Need to write code to reward player here

    else:
        LoseTableS.speed(0)
        LoseTableS.hideturtle()
        LoseTableS.penup()
        LoseTableS.shape(LoseTable)
        LoseTableS.goto(0, -200)
        LoseTableS.showturtle()
        # Need to write code to deduct coins here


def TraceResult():

    t.clear()
    finishLineS.hideturtle()
    screen.bgpic(RankTable)

    # Draw the results on the screen
    y1 = 55
    y2 = 55

    for i in range(6):
        t.tracer(False)
        t.hideturtle()
        t.penup()

        t.color('white')
        if i <= 2:
            t.goto(-140, y1)
            t.write(TrueResultsList[i], font=("Arial", 12, "bold"))
            y1 = y1 - 70
        else:
            t.goto(100, y2)
            t.write(TrueResultsList[i], font=("Arial", 12, "bold"))
            y2 = y2 - 70
        t.update()


def TraceResultCharacter():
    # Sort CharList to draw them
    for name in CharListRanked:
        if name not in TrueCharListRanked:
            TrueCharListRanked.append(name)
    y1 = 60
    y2 = 60
    for i in range(6):
        t.tracer(False)
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

        t.update()


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
        t.hideturtle()
        t.penup()
        t.goto(x, y - 20)
        t.color('red')
        t.write(NameList[i], font=("Arial", 20, "bold"))
        y = y - 60


def DrawScreen():
    t.tracer(False)
    screen.bgpic(mapChose)
    TraceCharacter(x, y)
    if mapSize == 'small':
        TraceFinishLineSmall()
    if mapSize == 'medium':
        TraceFinishLineMedium()
    if mapSize == 'large':
        TraceFinishLineLarge()
    t.update()
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
                t.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                t.update()
            elif StatusList[i] == 'slow':
                CharList[i].forward(random.randint(1, 4))
            elif StatusList[i] == 'fast':
                CharList[i].forward(random.randint(3, 10))
            elif CharList[i].xcor() >= -200:
                a = 1
                b = 5
                t.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                t.update()
            elif CharList[i].xcor() >= -300:
                a = 1
                b = 7
                t.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                t.update()
            else:
                a = 1
                b = 10
                t.tracer(False)
                CharList[i].forward(random.randint(a, b))
                time.sleep(0.001)
                t.update()
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
                    t.tracer(False)
                    potion2.forward(5)
                    time.sleep(0.001)
                    t.update()
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
                    t.tracer(False)
                    rocket2.forward(5)
                    time.sleep(0.001)
                    t.update()
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
    t.tracer(False)
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
    t.update()
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

    t.done()
