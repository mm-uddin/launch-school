'''
Problem Statement:
------------------
Write a function that determines the mean (average) of the three scores 
passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'

Tested values are all between 0 and 100. 
There is no need to check for negative values or values greater than 100.

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

'''

def get_grade(num1, num2, num3):
    average_mark = (num1 + num2 + num3) // 3
    grade = ''
    if average_mark >= 90 and average_mark <= 100 :
        grade = "A"
    elif average_mark >= 80 and average_mark < 90 :
        grade = "B"
    elif average_mark >= 70 and average_mark < 80 :
        grade = "C"
    elif average_mark >= 60 and average_mark < 70 :
        grade = "D"
    else:
        grade = "F"
    return grade

print(get_grade(0, 0, 100))
