'''
Problem Statement:
-----------------

Build a program that displays when the user will retire and how many 
years she has to work till retirement.


Example:
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
'''

current_age = int(input("What is your age? \n"))
start_year = int(input("Which year did you start working? \n"))
retirement_age = int(input("At what age would you like to retire?\n"))

current_year = 2026
start_age  = current_year - start_year
working_years = current_year - start_year

retirement_year = current_year + (retirement_age - current_age)

print(f"It's {current_year}. You started working in {start_year}")
print(f"It's {current_year}. You will retire in {retirement_year}")
print(f"You have worked for {working_years} ")
print(f"You have only {retirement_age-current_age} years of work to go!")