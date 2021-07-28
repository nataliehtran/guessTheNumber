import random
atempts = 0

print("Welcome to the Guess the Number Guessing Game!")
easyOrHard = input("Would you like to play easy or hard mode?(easy/hard): ")
number = random.choice(range(1,101))

def hard():
  global atempts
  atempts = 5
  answer = int(input("You have 5 atempts! Please guess a number from 1-100: "))
  while answer != number and atempts != 0:
    if answer > number:
      print("It is smaller!")
      print("You have %d atempts" %atempts)
      atempts -= 1
      answer = int(input("Try again: "))
    elif answer < number:
      print("It is bigger!")
      print("You have %d atempts" %atempts)
      answer = int(input("Try again: "))
      atempts -= 1
  if answer == number:
    print("You win! The number was %d" %number)
  elif atempts == 0:
    print("You have 0 atempts left! You lost! The number was %d" %number)

def easy():
  global atempts
  atempts = 10
  answer = int(input("You have 10 atempts! Please guess a number from 1-100: "))
  while answer != number and atempts != 0:
    if answer > number:
      print("It is smaller!")
      print("You have %d atempts" %atempts)
      answer = int(input("Try again: "))
      atempts -= 1
    elif answer < number:
      print("It is bigger!")
      print("You have %d atempts" %atempts)
      answer = int(input("Try again: "))
      atempts -= 1
  if answer == number:
    print("You win! The number was %d" %number)
  elif atempts == 0:
    print("You have 0 atempts left! You lost! The number was %d" %number)

if easyOrHard == "easy":
  easy()
elif easyOrHard == "hard":
  hard()
else:
  print("Not one of the options")
