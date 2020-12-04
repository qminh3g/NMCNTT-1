import time as t
import turtle
import pygame
import os
from pygame import mixer
from random import randint
from playsound import playsound
from threading import Thread
from PlayGame import *

scrWidth = 800
scrHeight = 650


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


def clearButtons():
    turtle.hideturtle()
    startButton.hideturtle()
    optionsButton.hideturtle()
    instructionsButton.hideturtle()
    minigameButton.hideturtle()

# def startGame(x,y):

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
    startButton.onclick(PlayGame)
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
