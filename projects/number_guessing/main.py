# number guessing game - computer picks a number and user has to guess it

import random

# computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100")

attempts = 0

# keep asking until user gets it right
while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    # checking if guess is too low, too high or correct
    if guess < secret_number:
        print("Too low! Try higher")
    elif guess > secret_number:
        print("Too high! Try lower")
    else:
        print("Correct! You got it in", attempts, "attempts")
        break