import random

def guess(x_number):
  random_number = random.randint(1, x_number)
  guess = 0


  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x_number}: '))
    if guess < random_number:
      print("Guess again. Too low")
    elif guess > random_number:
      print('Guess again. Too high')
  
  print(f'You got it. Random number was {random_number}')

guess(100)