import turtle
import time
import random
import time

#screen resolution
scrWidth = 1520
scrHeight = 790

screen = turtle.Screen()


def Countdown():
    t = 30
    while t >= 0:
        time.sleep(1)    
        t -= 1 

def Background():
    screen.setup(width = scrWidth,height = scrHeight)
    #turtle.goto(-105, 0) #tọa độ của tâm background
    #screen.bgpic()
    screen.bgcolor('green')

Background()

def Status():
    turtle.speed()
    turtle.up()
    turtle.forward(550)
    turtle.right(90)
    turtle.forward(390)
    turtle.pd()
    turtle.backward(790)
    #chèn hình ảnh cột status ở góc

Status() 

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

hole_1 = turtle.Turtle()
hole_2 = turtle.Turtle()
hole_3 = turtle.Turtle()
hole_4 = turtle.Turtle()
hole_5 = turtle.Turtle()
hole_6 = turtle.Turtle()
hole_7 = turtle.Turtle()
hole_8 = turtle.Turtle()
hole_9 = turtle.Turtle()

#def addShape()
    #import shapes
screen.addshape('hole.gif')
screen.addshape('mole.gif')

#character
def setPos():
    hole_1.speed(0)
    hole_1.up()
    hole_1.goto(-452.5, 202.5)
    hole_1.down()
    hole_1.shape("hole.gif")

    hole_1.speed(0)
    hole_2.up()
    hole_2.goto(-105, 202.5)
    hole_2.down()
    hole_2.shape("hole.gif")

    hole_3.speed(0)
    hole_3.up()
    hole_3.goto(242.5, 202.5)
    hole_3.down()
    hole_3.shape("hole.gif")

    hole_4.speed(0)
    hole_4.up()
    hole_4.goto(-452.5, 0)
    hole_4.down()
    hole_4.shape("hole.gif")

    hole_5.speed(0)
    hole_5.up()
    hole_5.goto(-105, 0)
    hole_5.down()
    hole_5.shape("hole.gif")

    hole_6.speed(0)
    hole_6.up()
    hole_6.goto(242.5, 0)
    hole_6.down()
    hole_6.shape("hole.gif")

    hole_7.speed(0)
    hole_7.up()
    hole_7.goto(-452.5, -202.5)
    hole_7.down()
    hole_7.shape("hole.gif")

    hole_8.speed(0)
    hole_8.up()
    hole_8.goto(-105, -202.5)
    hole_8.down()
    hole_8.shape("hole.gif")

    hole_9.speed(0)
    hole_9.up()
    hole_9.goto(242.5, -202.5)
    hole_9.down()
    hole_9.shape("hole.gif")

def mole1():
    mole_1.speed(0)
    mole_1.showturtle()
    mole_1.up()
    mole_1.goto(-458, 255.5)
    mole_1.down()
    mole_1.shape("mole.gif")
    time.sleep(1)
   # mole_1.hideturtle()    


def mole2():
    mole_2.speed(0)
    mole_2.showturtle()
    mole_2.up()
    mole_2.goto(-110.5, 255.5)
    mole_2.down()
    mole_2.shape("mole.gif")
    time.sleep(1)
    #mole_2.hideturtle()

def mole3():
    mole_3.speed(0)
    mole_3.showturtle()
    mole_3.up()
    mole_3.goto(238, 255.5)
    mole_3.down()
    mole_3.shape("mole.gif")
    time.sleep(1)
    #mole_3.hideturtle()

def mole4():
    mole_4.speed(0)
    mole_4.showturtle()
    mole_4.up()
    mole_4.goto(-458, 53)
    mole_4.down()
    mole_4.shape("mole.gif")
    time.sleep(1)
    #mole_4.hideturtle()

def mole5():
    mole_5.speed(0)
    mole_5.showturtle()
    mole_5.up()
    mole_5.goto(-110.5, 53)
    mole_5.down()
    mole_5.shape("mole.gif")
    time.sleep(1)
    #mole_5.hideturtle()

def mole6():
    mole_6.speed(0)
    mole_6.showturtle()
    mole_6.up()
    mole_6.goto(238, 53)
    mole_6.down()
    mole_6.shape("mole.gif")
    time.sleep(1)
    #mole_6.hideturtle()

def mole7():
    mole_7.speed(0)
    mole_7.showturtle()
    mole_7.up()
    mole_7.goto(-457.5, -149.5)
    mole_7.down()
    mole_7.shape("mole.gif")
    time.sleep(1)
    #mole_7.hideturtle()

def mole8():
    mole_8.speed(0)
    mole_8.showturtle()
    mole_8.up()
    mole_8.goto(-109, -149.5)
    mole_8.down()
    mole_8.shape("mole.gif")
    time.sleep(1)
    #mole_8.hideturtle()

def mole9():
    mole_9.speed(0)
    mole_9.showturtle()
    mole_9.up()
    mole_9.goto(237.5, -149.5)
    mole_9.down()
    mole_9.shape("mole.gif")
    time.sleep(1)
    #mole_9.hideturtle()

setPos()

mole1()
mole2()
mole3()
mole4()
mole5()
mole6()
mole7()
mole8()
mole9()


#Mole appear randomly\
clock = 30
square = 0
def clicked(x,y):
    global square
    if x < -350 and x > -579 and y > 170 and y < 360:
        square = 1
    if x < 25 and x > -230 and y > 170 and y < 360:
        square = 2
    if x < 370 and x > 120 and y > 170 and y < 360:
        square = 3
    if x < -350 and x > -579 and y > -35 and y < 153:
        square = 4
    if x < 25 and x > -230 and y > -35 and y < 153:
        square = 5
    if x < 370 and x > 120 and y > -35 and y < 153:
        square = 6    
    if x < -350 and x > -579 and y > -250 and y < -45:
        square = 7
    if x < 25 and x > -230 and y > -250 and y < -45:
        square = 8
    if x < 370 and x > 120 and y > -250 and y < -45:
        square = 9
    else:
        square = 100
    #print(square)

clicked(5,1)
print(square)
##print(m1, m2, "ngoài")
#print("Day la ", square)
turtle.mainloop()


