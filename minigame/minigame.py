import turtle
import time
import random

score = 0
t = 30


isGhost1 = False
isGhost2 = False
isGhost3 = False
isGhost4 = False
isGhost5 = False

#screen resolution
scrWidth = 1200
scrHeight = 645

#turtle has to be declared globally, so the other functions can recognise them.
screen = turtle.Screen()

grave1 = turtle.Turtle()
grave2 = turtle.Turtle()
grave3 = turtle.Turtle()
grave4 = turtle.Turtle()
grave5 = turtle.Turtle()


ghost1 = turtle.Turtle()
ghost2 = turtle.Turtle()
ghost3 = turtle.Turtle()
ghost4 = turtle.Turtle()
ghost5 = turtle.Turtle()

def addShape ():
    #import shapes
    screen.addshape("img/grave.gif")
    screen.addshape("img/ghost.gif")
    

def initBackgroundMG():
    #screen setting
    screen.title("GHOST HUNTER")
    screen.setup(scrWidth,scrHeight)
    
    #insert background
    screen.bgpic('img/bg_mini.gif')
    addShape()

def setPos():
    ghost1.speed(5)
    ghost1.left(90)
    ghost1.hideturtle()
    ghost1.penup()
    ghost1.setpos(-480,0)
    ghost1.shape("img/ghost.gif")

    ghost2.speed(5)
    ghost2.left(90)
    ghost2.hideturtle()
    ghost2.penup()
    ghost2.setpos(-240,0)
    ghost2.shape("img/ghost.gif")

    ghost3.speed(5)
    ghost3.left(90)
    ghost3.hideturtle()
    ghost3.penup()
    ghost3.setpos(0,0)
    ghost3.shape("img/ghost.gif")

    ghost4.speed(5)
    ghost4.left(90)
    ghost4.hideturtle()
    ghost4.penup()
    ghost4.setpos(240,0)
    ghost4.shape("img/ghost.gif")

    ghost5.speed(5)
    ghost5.left(90)
    ghost5.hideturtle()
    ghost5.penup()
    ghost5.setpos(480,0)
    ghost5.shape("img/ghost.gif")

    grave1.speed(0)
    grave1.penup()
    grave1.setpos(-480,0)
    grave1.shape("img/grave.gif")
    
    grave2.speed(0)
    grave2.penup()
    grave2.setpos(-240,0)
    grave2.shape("img/grave.gif")

    grave3.speed(0)
    grave3.penup()
    grave3.setpos(0,0)
    grave3.shape("img/grave.gif")

    grave4.speed(0)
    grave4.penup()
    grave4.setpos(240,0)
    grave4.shape("img/grave.gif")

    grave5.speed(0)
    grave5.penup()
    grave5.setpos(480,0)
    grave5.shape("img/grave.gif")
    
def addScore1(x,y):
    global score
    score = score + 20
    print(score)
    ghost1.setpos(-480,0)
    ghost1.hideturtle()
    isGhost1 = False
    return isGhost1

def addScore2(x,y):
    global score
    score = score + 20
    print(score)
    ghost2.setpos(-240,0)
    ghost2.hideturtle()
    isGhost2 = False
    return isGhost1

def addScore3(x,y):
    global score
    score = score + 20
    print(score)
    ghost3.setpos(0,0)
    ghost3.hideturtle()
    isGhost3 = False
    return isGhost3
    
def addScore4(x,y):
    global score
    score = score + 20
    print(score)
    ghost4.setpos(240,0)
    ghost4.hideturtle()
    isGhost4 = False
    return isGhost4

def addScore5(x,y):
    global score
    score = score + 20
    print(score)
    ghost5.setpos(480,0)
    ghost5.hideturtle()
    isGhost5 = False
    return isGhost5

def countdown(t):
    isGhost1 = False
    isGhost2 = False
    isGhost3 = False
    isGhost4 = False
    isGhost5 = False
    while t: 
        if t % 1 == 0:
            code = random.randint(1,5)
            if isGhost1 == True:
                ghost1.setpos(-480,0)
                ghost1.hideturtle()
                isGhost1 = False
            if isGhost2 == True:
                ghost2.setpos(-240,0)
                ghost2.hideturtle()
                isGhost2 = False
            if isGhost3 == True:
                ghost3.setpos(0,0)
                ghost3.hideturtle()
                isGhost3 = False
            if isGhost4 == True:
                ghost4.setpos(240,0)
                ghost4.hideturtle()
                isGhost4 = False
            if isGhost5 == True:
                ghost5.setpos(480,0)
                ghost5.hideturtle()
                isGhost5 = False
            if code == 1:
                isGhost1 = True
                ghost1.showturtle()
                ghost1.forward(150)
            if code == 2:
                isGhost2 = True
                ghost2.showturtle()
                ghost2.forward(150)
            if code == 3:
                isGhost3 = True
                ghost3.showturtle()
                ghost3.forward(150)
            if code == 4:
                isGhost4 = True
                ghost4.showturtle()
                ghost4.forward(150)
            if code == 5:
                isGhost5 = True
                ghost5.showturtle()
                ghost5.forward(150)
            ghost1.onclick(addScore1)
            ghost2.onclick(addScore2)
            ghost3.onclick(addScore3)
            ghost4.onclick(addScore4)
            ghost5.onclick(addScore5)
        time.sleep(1) 
        t -= 1
initBackgroundMG()
setPos()
countdown(t)
    
    
