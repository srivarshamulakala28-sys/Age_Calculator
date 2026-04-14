# testing rock paper scissors logic

import unittest

def check_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user wins"
    else:
        return "computer wins"

class TestRockPaperScissors(unittest.TestCase):

    def test_tie(self):
        self.assertEqual(check_winner("rock", "rock"), "tie")

    def test_user_wins(self):
        self.assertEqual(check_winner("rock", "scissors"), "user wins")

    def test_computer_wins(self):
        self.assertEqual(check_winner("scissors", "rock"), "computer wins")

if __name__ == "__main__":
    unittest.main()