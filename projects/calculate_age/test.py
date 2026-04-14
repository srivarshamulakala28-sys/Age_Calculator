# testing the calculate age logic

import unittest
from datetime import date

# copying the logic here to test it directly
def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    birthday = date(birth_year, birth_month, birth_day)
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age = age - 1
    return age

class TestCalculateAge(unittest.TestCase):

    def test_age_is_positive(self):
        age = calculate_age(2000, 1, 1)
        self.assertGreater(age, 0)

    def test_age_type_is_int(self):
        age = calculate_age(1995, 6, 15)
        self.assertIsInstance(age, int)

if __name__ == "__main__":
    unittest.main()
    