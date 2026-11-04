'''
Problem Statement:
-------------------
Write a function that takes any year greater than 0 as input and returns True 
if the year is a leap year, or False if it is not.

problem statement part Part 2:
In the previous exercise, we assumed that the Gregorian calendar has been 
in continuous use since the year 1. However, the Gregorian calendar wasn't 
adopted until much later; prior to that, much of the world used the Julian 
calendar, which observed leap year every 4 years.

in 1752, England, Ireland, and the British colonies all switched to the 
Gregorian calendar. Update the function from the previous exercise so it 
uses the Julian calendar prior to 1752, and the Gregorian calendar 
starting in 1752.

Step 1. Understanding the problem:
- a function that takes any year as argument and returns true if the year
  is a leap year or returns false if it is not a leap year

  - if a year is divisible by 400, it is a leap year
  - if the year is divisible by 100 but not by 400, it is not a leap year
  - if the year is divisible by 4 but not by 100, it is a leap year.
  - All other years are not leap years.

Step 2. Examples
- print(is_leap_year(1200) == True)/ returns True
- print(is_leap_year(2023) == False)/ returns False

Step 3. Datastructures
- input : integer
- output: boolean True or False

Step 4. Algortihm
- If the year is divisible by 400, it is a leap year.
- If the year is divisible by 100 but not by 400, it is not a leap year.
- If the year is divisible by 4 but not by 100, it is a leap year.
- All other years are not leap years.

'''

def is_leap_year(year):
    if year < 1752 and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)