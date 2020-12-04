import turtle as t
import random
import time
from ResultScreen import *
from CharacterSelection import *
from ImageAssets import *
from StartGame import *
# This file is used to play the CharacterSelection Screen

screen.setup(1200, 645)


TraceCharacterSelection(-250, 0)

CharList[0].onclick(PlayerAssign0)
CharList[1].onclick(PlayerAssign1)
CharList[2].onclick(PlayerAssign2)
CharList[3].onclick(PlayerAssign3)
CharList[4].onclick(PlayerAssign4)
CharList[5].onclick(PlayerAssign5)

input()
