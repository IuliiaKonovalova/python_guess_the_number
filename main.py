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

# guess(100)

def computer_guess(x_for_computer):
  low = 1
  high = x_for_computer
  feedback = ''
  while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

  print(f'Computer guessed correctly, {guess}')

computer_guess(100)