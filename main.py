import random

def guess(x_number):
  """
  Chooses the random number,
  checks whether the guess is correct
  Provides comments to the user which guide them through the choices
  """
  random_number = random.randint(1, x_number)
  guess = 0

  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x_number}: '))
    if guess < random_number:
      if guess in range(random_number - 2, random_number):
        print('Guess again. A bit low!')
      elif guess in range (random_number - 3, random_number):
        print('Guess again. Low!')
      else:
        print("Guess again. Too low!")
    elif guess > random_number:
      if guess in range(random_number + 1, random_number + 3):
        print('Guess again! A bit high!') 
      elif guess in range(random_number + 3, random_number + 10):
        print('Guess again. High!')
      else:
        print('Guess again. Too high!')
  
  print(f'You got it. Random number was {random_number}')

guess(100)

def computer_guess(x_for_computer):
  """
  Provides guesses according to the user guidence
  """
  low = 1
  high = x_for_computer
  feedback = ''

  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

  print(f'Computer guessed correctly, {guess}')

# computer_guess(100)