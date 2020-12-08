import random
import turtle as t


# Get the image assets
bo1 = 'img/Characters/bo1.gif'
bo2 = 'img/Characters/bo2.gif'
bo3 = 'img/Characters/bo3.gif'
bo4 = 'img/Characters/bo4.gif'
bo5 = 'img/Characters/bo5.gif'
bo6 = 'img/Characters/bo6.gif'

cho1 = 'img/Characters/cho1.gif'
cho2 = 'img/Characters/cho2.gif'
cho3 = 'img/Characters/cho3.gif'
cho4 = 'img/Characters/cho4.gif'
cho5 = 'img/Characters/cho5.gif'
cho6 = 'img/Characters/cho6.gif'

meo1 = 'img/Characters/meo1.gif'
meo2 = 'img/Characters/meo2.gif'
meo3 = 'img/Characters/meo3.gif'
meo4 = 'img/Characters/meo4.gif'
meo5 = 'img/Characters/meo5.gif'
meo6 = 'img/Characters/meo6.gif'

ngua1 = 'img/Characters/ngua1.gif'
ngua2 = 'img/Characters/ngua2.gif'
ngua3 = 'img/Characters/ngua3.gif'
ngua4 = 'img/Characters/ngua4.gif'
ngua5 = 'img/Characters/ngua5.gif'
ngua6 = 'img/Characters/ngua6.gif'

finishLine = 'img/FinishLine.gif'

ForestMap = 'img/ForestMap.gif'
BeachMap = 'img/BeachMap.gif'
GalaxyMap = 'img/GalaxyMap.gif'


# Get maps
mapChoice = random.randint(0, 2)
Maps = [ForestMap, BeachMap, GalaxyMap]

# Get Characters' Avatars and randomize them
bo = [bo1, bo2, bo3, bo4, bo5, bo6]
meo = [meo1, meo2, meo3, meo4, meo5, meo6]
ngua = [ngua1, ngua2, ngua3, ngua4, ngua5, ngua6]
cho = [cho1, cho2, cho3, cho4, cho5, cho6]
random.shuffle(bo)
random.shuffle(cho)
random.shuffle(ngua)
random.shuffle(meo)
avatarsChoice = random.randint(0, 3)
Avatars = [bo, meo, cho, ngua]
avatarsChose = Avatars[avatarsChoice]

# Character Turtle()
finishLineS = t.Turtle()
Char1 = t.Turtle()
Char2 = t.Turtle()
Char3 = t.Turtle()
Char4 = t.Turtle()
Char5 = t.Turtle()
Char6 = t.Turtle()

CharList = [Char1, Char2, Char3, Char4, Char5, Char6]

# Characters' names and randomize name list
NameList = ['Tân', 'Thịnh', 'Tú', 'Huy', 'Ben', 'Minh']
random.shuffle(NameList)
Char1Name = NameList[0]
Char2Name = NameList[1]
Char3Name = NameList[2]
Char4Name = NameList[3]
Char5Name = NameList[4]
Char6Name = NameList[5]


# Add shapes and screen setup
screen = t.Screen()
for Characters in bo:
    screen.addshape(Characters)
for Characters in meo:
    screen.addshape(Characters)
for Characters in cho:
    screen.addshape(Characters)
for Characters in ngua:
    screen.addshape(Characters)

screen.addshape(finishLine)
