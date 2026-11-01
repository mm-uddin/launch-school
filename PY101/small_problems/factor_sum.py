'''
-------------------------------------------------------------------------------
Problem Statement:

Suppose you have an arbitrary natural number (the target) and a set of one or 
more additional natural numbers (the factors). Write a program that computes 
the sum of all numbers from 1 up to the target number that are also multiples 
of one of the factors. 

For instance, if the target is 20, and the factors are 3 and 5, that gives us 
the list of multiples 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples 
is 78.

If no factors are given, use 3 and 5 as the default factors.
------------------------------------------------------------------------------

// Step 1: Understanding the problem:


Input:
- target = 9 and

- factors = [2, 3] or could be only one [2] or could not be empty [] because
if no factors are given use [3, 5]

Output:
- Sum of unique multiples of factors

- all the numbers from 1 upto target number = [1, 2, 3, 4, 5, 6, 7, 8]
  basically a range of (1, 9). The last number of the range is not included
  and hence the target number is not included. We finish the checking up
  to the last natural number before the target. If the target is 9, we check
  up to 8.

- Now if factor is [2, 3], what are the multiples?

- multiples of 2 : [2, 4, 6, 8, 10,.,.,....n] (we do not need to check further 
  because we have crossed the target number already).

- multiples of 3: [3, 6, 9,.,.......n]

- Now we have to create a seperate list from the list
  of multiples up to the target number and sum the numbers
  in the list.

- The problem does not say, what we do when we find numbers
  that are multiple of both the factors. Like 6 is multiple
  of both 2 and 3. Ask should we count 6 once or twice. 
  The answer is: only the unique multiples,

- from the unique multiple list [2, 3, 4, 6, 8]  of
the sum is (2 + 3 + 4 + 6 + 8) =   23

- the function should return 23


// Step 2 Examples:
Example 1 (Standard with defaults):

Input:
- Target: 20
- Factors: None (Defaults to [3, 5]) 
- Unique multiples: 3, 5, 6, 9, 10, 12, 15, 18
- Calculation: 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78

Output:
- 78

Example 2 (Custom factors):

Input:
- Target: 10
- Factors: [2, 7]
- Unique multiples: 2, 4, 6, 7, 8
- Calculation: 2 + 4 + 6 + 7 + 8 = 27

Output:
- 27

Example 3 (Edge Case: Small target):

Input:
- Target: 1
- Factors: [3, 5]
- Unique multiples: None (Range is empty for (0,1))
- Calculation: 0

Output:
- 0


//Step 3. Data Structure:

-Input Parameters:
    - Target: Integer
    - Factors: List of integers (defaulting to [3, 5])

- Intermediate collection:
    - A list to store all numbers from 1 up to target - 1
      that satisfy the multiple condition.
- Output:
    - Integer (accumulated sum)

// Step 4. Algorithm:

1. Initialize Parameters:
- Set target to the given number.
- Set factors to the provided factors, or default to [3, 5] if the list
  is empty/ omitted

2. Initialize tracking:
- Create an empty collection multiples (or set a running sum tracker sum = 0).

3. Iterate Through Candidate Range:
- Loop through each integer candidate from 1 up to target - 1:
    - Loop through each factor in factors:
        - Check if candidate % factor == 0 (i.e. candidate is divisible 
          by factor)
        - If true:
            - Add candidate to multiples (or add to sum)
            - Break out of the inner factor loop to avoid counting
              duplicate multiples
4. Aggregate Result:
- Calculate the sum of all elements in multiples (or return the accumulated sum)
- Return the result.

'''

def factor_sum(target, factors = None):
    if factors is None or len(factors) == 0:
        factors = [3, 5]

    multiples = []
    for num in range(1, target):
        for factor in factors:
            if num % factor == 0 and num not in multiples:
                multiples.append (num)
    
    return sum(multiples)

print(factor_sum(20))
print(factor_sum(10, [2, 7]))
print(factor_sum(1))
