# rock paper scissors game against the computer

import random

print("Welcome to Rock Paper Scissors!")
print("----------------------------------")

# computer picks randomly from these three
options = ["rock", "paper", "scissors"]

while True:
    # taking input from user
    user_choice = input("Enter rock, paper or scissors (or quit to stop): ").lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    # checking if user typed something valid
    if user_choice not in options:
        print("Invalid choice! Please type rock, paper or scissors")
        continue

    # computer picks a random option
    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    # checking who won
    if user_choice == computer_choice:
        print("Its a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")