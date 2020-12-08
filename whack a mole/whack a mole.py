import turtle
import time
import random

#screen resolution
scrWidth = 1200
scrHeight = 645
#Set time and score
clock = 30
score = 0

#screen
bg = turtle.Turtle()
screen = turtle.Screen()
   
#character
mole_1 = turtle.Turtle()
mole_2 = turtle.Turtle()
mole_3 = turtle.Turtle()
mole_4 = turtle.Turtle()
mole_5 = turtle.Turtle()
mole_6 = turtle.Turtle()
mole_7 = turtle.Turtle()
mole_8 = turtle.Turtle()
mole_9 = turtle.Turtle()
#hole
hole_1 = turtle.Turtle()
hole_2 = turtle.Turtle()
hole_3 = turtle.Turtle()
hole_4 = turtle.Turtle()
hole_5 = turtle.Turtle()
hole_6 = turtle.Turtle()
hole_7 = turtle.Turtle()
hole_8 = turtle.Turtle()
hole_9 = turtle.Turtle()

#Set up background
def Background():
    screen.setup(width = scrWidth,height = scrHeight)
    bg.goto(-68.5, 0) #coordinate of the middle of background
    bg.shape('background.gif')

def Status():
    turtle.speed(0)
    #insert turtle bar

def addShape():
    screen.addshape('mole.gif')
    screen.addshape('background.gif')

def clicked(x, y):
    global score
    score = score + 1
    print(score)

#Set Mole
def mole1():
    mole_1.speed(0)
    mole_1.showturtle()
    mole_1.up()
    mole_1.goto(-297, 20)
    mole_1.down()
    mole_1.shape("mole.gif")
    time.sleep(0.7)
    mole_1.onclick(clicked)
    mole_1.hideturtle()    

def mole2():
    mole_2.speed(0)
    mole_2.showturtle()
    mole_2.up()
    mole_2.goto(8, 6)
    mole_2.down()
    mole_2.shape("mole.gif")
    time.sleep(0.7)
    mole_2.onclick(clicked)
    mole_2.hideturtle()

def mole3():
    mole_3.speed(0)
    mole_3.showturtle()
    mole_3.up()
    mole_3.goto(-210, -79)
    mole_3.down()
    mole_3.shape("mole.gif")
    time.sleep(0.7)
    mole_3.onclick(clicked)
    mole_3.hideturtle()

def mole4():
    mole_4.speed(0)
    mole_4.showturtle()
    mole_4.up()
    mole_4.goto(170, -82)
    mole_4.down()
    mole_4.shape("mole.gif")
    time.sleep(0.7)
    mole_4.onclick(clicked)
    mole_4.hideturtle()

def mole5():
    mole_5.speed(0)
    mole_5.showturtle()
    mole_5.up()
    mole_5.goto(-329, -196)
    mole_5.down()
    mole_5.shape("mole.gif")
    time.sleep(0.7)
    mole_5.onclick(clicked)
    mole_5.hideturtle()

def mole6():
    mole_6.speed(0)
    mole_6.showturtle()
    mole_6.up()
    mole_6.goto(-22, -182)
    mole_6.down()
    mole_6.shape("mole.gif")
    time.sleep(0.7)
    mole_6.onclick(clicked)
    mole_6.hideturtle()

def mole7():
    mole_7.speed(0)
    mole_7.showturtle()
    mole_7.up()
    mole_7.goto(277, -206)
    mole_7.down()
    mole_7.shape("mole.gif")
    time.sleep(0.7)
    mole_7.onclick(clicked)
    mole_7.hideturtle()

def main():
    global clock
    while clock > 0: 
        t = random.randint(1,9)
        if t == 1:
            mole1()
        if t == 2:
            mole2()
        if t == 3:
            mole3()
        if t == 4:
            mole4()
        if t == 5:
            mole5()
        if t == 6:
            mole6()
        if t == 7:
            mole7()

        clock = clock - 1

addShape()
Background()
Status() 
main()
