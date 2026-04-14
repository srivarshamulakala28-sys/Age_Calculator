# testing the number guessing game logic

import unittest
import random

class TestGuessingGame(unittest.TestCase):

    def test_random_number_in_range(self):
        # checking that the random number is always between 1 and 100
        number = random.randint(1, 100)
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 100)

    def test_guess_too_low(self):
        secret = 50
        guess = 30
        result = "Too low" if guess < secret else "correct"
        self.assertEqual(result, "Too low")

    def test_guess_too_high(self):
        secret = 50
        guess = 80
        result = "Too high" if guess > secret else "correct"
        self.assertEqual(result, "Too high")

    def test_correct_guess(self):
        secret = 50
        guess = 50
        result = "Correct" if guess == secret else "wrong"
        self.assertEqual(result, "Correct")

if __name__ == "__main__":
    unittest.main()