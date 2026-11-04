'''
Problem statement:
-----------------
Write a function that computes the sum of all numbers between 1 and some 
other number, inclusive, that are multiples of 3 or 5. For instance, if 
the supplied number is 20, 

the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.

//step 1. Understand the problem:
- a function that computes sum of all numbers betweeen 1 and upto
the another number (inclusive) which are multiples of 3 or 5.

//step 2. Examples:
- if 
the supplied number is 20, 

the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

// step 3. Data structures.
input:
- target: an integer
output:
- sum: an integer

// Step 4. Algorithm

- 1.create a list and name it multiples 
- 2. check for every number from 1 to upto the target number inclusive
- 3. if the number is divisible by 3 or 5 and is not included in multiples,
append it to multiples

- 4. return sum of the multiples 

'''
def multisum(target_num):
    multiples = []
    for i in range(1, target_num + 1):
        if (i % 3 == 0 or i % 5 == 0):
            multiples.append(i)
    return sum(multiples)




# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)