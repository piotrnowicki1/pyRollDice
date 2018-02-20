# this will be an example of dice roll game
from random import randint

def leftDice():
  dice1 = randint(1,6)
  print(dice1)
  return dice1
  
def rightDice():
  dice2 = randint(1,6)
  print(dice2)
  return dice2

leftDice()
rightDice()
