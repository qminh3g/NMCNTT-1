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


def TraceResult():
    # Result List sorted

    for name in ResultsList:
        if name not in TrueResultsList:
            TrueResultsList.append(name)

    # Draw the results on the screen
    t.tracer(False)
    y = 150
    for i in range(6):
        t.tracer(False)
        t.hideturtle()
        t.penup()
        t.goto(-80, y)
        t.color('white')
        t.write(TrueResultsList[i], font=("Arial", 20, "bold"))
        y = y - 60
        t.update()


def TraceResultCharacter():
    # Sort CharList to draw them
    for name in CharListRanked:
        if name not in TrueCharListRanked:
            TrueCharListRanked.append(name)
    y = 150
    for i in range(6):
        t.tracer(False)
        TrueCharListRanked[i].speed(0)
        TrueCharListRanked[i].hideturtle()
        TrueCharListRanked[i].penup()
        TrueCharListRanked[i].goto(100, y)
        TrueCharListRanked[i].showturtle()
        y = y - 60
        t.update()


def TraceFinishLine():
    finishLineS.hideturtle()
    finishLineS.penup()
    finishLineS.speed(0)
    finishLineS.goto(520, 45)
    finishLineS.shape(finishLine)
    finishLineS.showturtle()


def TraceCharacter(x, y):
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
    screen.bgpic(Maps[mapChoice])
    TraceCharacter(x, y)
    TraceFinishLine()
    t.update()
    time.sleep(1)


def RaceStart():
    while True:
        for i in range(6):
            if CharList[i].xcor() >= 500:
                CharListRanked.append(CharList[i])
                ResultsList.append(NameList[i])
            # This block of code is used to determine speed of the characters, need optimizing
            t.tracer(False)
            CharList[i].forward(random.randint(10, 50))
            time.sleep(0.001)
            t.update()

        if CharList[i].xcor() > 720:
            break


def StartGame():
    DrawScreen()
    RaceStart()
    TraceResult()
    TraceResultCharacter()
