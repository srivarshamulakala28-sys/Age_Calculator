# this program calculates how old a person is based on their birthday

from datetime import date

# asking the user to enter their birth year, month and day
birth_year = int(input("Enter your birth year (example: 2000): "))
birth_month = int(input("Enter your birth month (example: 6): "))
birth_day = int(input("Enter your birth day (example: 15): "))

# getting todays date automatically
today = date.today()

# creating the birthday from what user entered
birthday = date(birth_year, birth_month, birth_day)

# calculating the age by subtracting birth year from current year
age = today.year - birthday.year

# if birthday hasnt come yet this year then minus 1 from age
if (today.month, today.day) < (birthday.month, birthday.day):
    age = age - 1

print("Your age is:", age, "years")