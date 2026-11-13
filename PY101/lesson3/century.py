'''
Problem Staement:
----------------
Write a function that takes a year as input and returns the century. 
The return value should be a string that begins with the century number, 
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True


1 = 1st century
99 = 1st century
100 = 1st century
101 = 2nd century
200 = 2nd century
201 = 3rd century

2000 // 100 = 20
5/100


if num[-1] == 2:
    nd
elif num [-1] == 3:
    rd
elif num[-1: -3] is in ['10', '11', '12']:
    th     
elif num[-1] == 1:
    st
else:
   th

'''
import math

def what_century(year):
    return math.ceil(year / 100)

def century_suffix(num):
    num = str(num)
    suffix = ''
    if num[-2:] in ['10', '11', '12', '13']:
        suffix = 'th'
    elif num[-1] == '1':
        suffix = 'st'
    elif num[-1] == '2':
        suffix = 'nd'
    elif num[-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'


    return suffix


def century(year):
    given_century = what_century(year)
    return str(given_century) + century_suffix(given_century)

print(century(2000) == "20th") 
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
