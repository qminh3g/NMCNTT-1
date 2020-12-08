#screen resolution
scrWidth = 1200
scrHeight = 645
#Set time and score
clock = 15
score = 0
lives = 3
score_max = 25

def whackamole():
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
    #Set up background
    def Background():
        bg.up()
        bg.speed(0)
        screen.setup(width = scrWidth,height = scrHeight)
        bg.goto(-68.5, 0) #coordinate of the middle of background
        bg.down()
        bg.shape('minigame_img/background.gif')

    def Status():
        sttbg.up()
        sttbg.speed(0)
        sttbg.goto(492,0)
        sttbg.down()
        sttbg.shape('minigame_img/sttbg.gif')
        #insert turtle bar

    def addShape():
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
        
    def plus(x, y):
        global score
        score = score + 1
        print(score)
    def minus(x, y):
        global lives
        lives = lives - 1
        #print("day la lives", lives)
    def heart1():
        heart_1.speed(0)
        heart_1.up()
        heart_1.goto(364,290)
        heart_1.down()
        heart_1.shape("minigame_img/heart.gif")
    def heart2():
        heart_2.speed(0)
        heart_2.up()
        heart_2.goto(324,290)
        heart_2.down()
        heart_2.shape("minigame_img/heart.gif")    
    def heart3():
        heart_3.speed(0)
        heart_3.up()
        heart_3.goto(284,290)
        heart_3.down()
        heart_3.shape("minigame_img/heart.gif")    
    #Set Mole
    def mole1():
        mole_1.speed(0)
        mole_1.up()
        mole_1.goto(-297, 20)
        mole_1.down()
        mole_1.showturtle()
        mole_1.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_1.onclick(plus)
        mole_1.hideturtle()    

    def mole2():
        mole_2.speed(0)
        mole_2.up()
        mole_2.goto(8, 6)
        mole_2.down()
        mole_2.showturtle()
        mole_2.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_2.onclick(plus)
        mole_2.hideturtle()

    def mole3():
        mole_3.speed(0)
        mole_3.up()
        mole_3.goto(-210, -79)
        mole_3.down()
        mole_3.showturtle()
        mole_3.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_3.onclick(plus)
        mole_3.hideturtle()

    def mole4():
        mole_4.speed(0)
        mole_4.up()
        mole_4.goto(170, -82)
        mole_4.down()
        mole_4.showturtle()
        mole_4.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_4.onclick(plus)
        mole_4.hideturtle()

    def mole5():
        mole_5.speed(0)
        mole_5.up()
        mole_5.goto(-329, -196)
        mole_5.down()
        mole_5.showturtle()
        mole_5.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_5.onclick(plus)
        mole_5.hideturtle()

    def mole6():
        mole_6.speed(0)
        mole_6.up()
        mole_6.goto(-22, -182)
        mole_6.down()
        mole_6.showturtle()
        mole_6.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_6.onclick(plus)
        mole_6.hideturtle()

    def mole7():
        mole_7.speed(0)
        mole_7.up()
        mole_7.goto(277, -206)
        mole_7.down()
        mole_7.showturtle()
        mole_7.shape("minigame_img/mole.gif")
        time.sleep(0.4)
        mole_7.onclick(plus)
        mole_7.hideturtle()
#Set bomb        
    def bomb1():
        bomb_1.speed(0)
        bomb_1.up()
        bomb_1.goto(-297, 20)
        bomb_1.down()
        bomb_1.showturtle()
        bomb_1.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_1.onclick(minus)
        bomb_1.hideturtle()    
    def bomb2():
        bomb_2.speed(0)
        bomb_2.up()
        bomb_2.goto(8, 6)
        bomb_2.down()
        bomb_2.showturtle()
        bomb_2.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_2.onclick(minus)
        bomb_2.hideturtle()
    def bomb3():
        bomb_3.speed(0)
        bomb_3.up()
        bomb_3.goto(-210, -79)
        bomb_3.down()
        bomb_3.showturtle()
        bomb_3.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_3.onclick(minus)
        bomb_3.hideturtle()
    def bomb4():
        bomb_4.speed(0)
        bomb_4.up()
        bomb_4.goto(170, -82)
        bomb_4.down()
        bomb_4.showturtle()
        bomb_4.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_4.onclick(minus)
        bomb_4.hideturtle()
    def bomb5():
        bomb_5.speed(0)
        bomb_5.up()
        bomb_5.goto(-329, -196)
        bomb_5.down()
        bomb_5.showturtle()
        bomb_5.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_5.onclick(minus)
        bomb_5.hideturtle()
    def bomb6():
        bomb_6.speed(0)
        bomb_6.up()
        bomb_6.goto(-22, -182)
        bomb_6.down()
        bomb_6.showturtle()
        bomb_6.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_6.onclick(minus)
        bomb_6.hideturtle()
    def bomb7():
        bomb_7.speed(0)
        bomb_7.up()
        bomb_7.goto(277, -206)
        bomb_7.down()
        bomb_7.showturtle()
        bomb_7.shape("minigame_img/bomb.gif")
        time.sleep(0.6)
        bomb_7.onclick(minus)
        bomb_7.hideturtle()
    #STT
    def min():
        global clock
        fm = turtle.Turtle()
        sm = turtle.Turtle()

        def fmin():
            fm.speed(0)
            fm.up()
            fm.goto(470, 77.5)
            fm.down()
            fm.shape(num[fmin1])
        def smin():
            sm.speed(0)
            sm.up()
            sm.goto(514, 77.5)
            sm.down()
            sm.shape(num[smin1])
        fmin1 = int(clock / 10)
        smin1 = int(clock % 10)

        fmin()
        smin()    
        time.sleep(1)
        #cai tien
        fm.hideturtle()
        sm.hideturtle()
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
    def score_item():
        global score
        def s1():
            ds1.speed(0)
            ds1.up()
            ds1.goto(470, -72.5)
            ds1.down
            ds1.shape(num[int(score / 10)])
        def s2():
            ds2.speed(0)
            ds2.up()
            ds2.goto(514, -72.5)
            ds2.down
            ds2.shape(num[int(score % 10)])
        def s_center():
            dsc.speed(0)
            dsc.up()
            dsc.goto(492, -72.5)
            dsc.down
            dsc.shape(num[int(score % 10)])
        if score < 10:
            s_center()
        else:
            dsc.hideturtle()
            s1()
            s2()
    def main():
        global clock, lives, score, score_max, num
        while clock > 0 and score < score_max and lives > 0: 
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
            if t == 5 or t == 19 or t == 26:
                mole5()
            if t == 6 or t == 20 or t == 27:
                mole6()
            if t == 7 or t == 21 or t == 28:
                mole7()
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
        '''
        if score == score_max:
            player.coin = player.coin + #so tien
        '''            
    addShape()
    Background()
    Status() 
    main()
whackamole()