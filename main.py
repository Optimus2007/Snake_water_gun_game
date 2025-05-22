#snake water gun game
'''
snake = -1 , refer to as s
water = 0 , refer to as w
gun = 1 , refer to as g

'''

import random

computer = random.choice([-1, 0, 1])
a = input("Enter your choice: ")
b = { "s":-1 , "w":0, "g":1 }
reverseb = { -1:"s", 0:"w", 1:"g" }
c = b[a]
print("Computer chose: ", reverseb[computer])
if c == computer:
    print("Draw")
elif (c == -1 and computer == 0) or (c == 0 and computer == 1) or (c == 1 and computer == -1):
    print("You win")
else:
    print("You lose, try again")
# The game is a simple implementation of the classic game "Snake, Water, Gun"
