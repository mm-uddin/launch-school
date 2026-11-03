'''
Sum or Product of Consecutive Integers:
Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of all 
numbers between 1 and the entered integer, inclusive. 
Finally, share the result with them.


//Step 1: Understanding the problem:

- User enters an integer greater than zero
- then user enters whether he/she wants sum or product
- based on user's choice the program calculates sum or product
  from 1 up to (inclusive) the integer that user provided .
- finally return the resultant cumulative sum of the numbers or 
  cumulative product of the numbers. 

// Step 2. Example:

Example 1:
    - User enters 5
    - Choose 'sum'
    - result would be 1 + 2 + 3 + 4 + 5 = 15
    - return 15

Example 2:
    - User enters 5
    - choose 'product'
    - result would be: 1 * 2 * 3 * 4 * 5 = 120
    - return 120

Example 3 (edge cases):


// Step 3. Data Structure:

- Input :
    - Integer greater that zero

- Output:
    - Integer

    
// Step 4. Algoritm

1. Ask the user for the target number
- set target_number to user's number
2. Ask the user what do they want? sum or product?
- set the option to user's selection
3. create a variable called total and
assign it to 1

3. Based on the option selected by the user in step 3
either do sum or multiplication from 1 to up to the target number
and update total in every step

4. return total

'''

print("Tell us the target number greater than zero")
target = int(input())

print("What operation do you want?")
print("For sum input 's' and for product input 'p'")
option = input()

total = 0
if option == 's':
    for i in range(1, target + 1):
        total += i
    print(f"The total sum is {total}")
elif option == 'p':
    total = 1
    for i in range(1, target + 1):
        total *= i
    print(f"The total product is {total}")
else:
    print("Please select either 's' or 'p'")
