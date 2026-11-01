'''
-----------------------------------------------------------------
Create a simple tip calculator. 
- The program should prompt for a bill amount and a tip rate. 
- The program must compute the tip, then print both the tip 
  and the total amount of the bill. 
- You can ignore input validation and assume that 
  the user will enter valid numbers.
------------------------------------------------------------------

'''

def calculate_tip():
    print("What is the bill amount?")
    bill_amount = float(input())

    print("What percent do you want to pay as tip?")
    print("Just give the number. For ex: for 15% type 15")
    tip_rate = float(input()) / 100
    tip_amount = bill_amount * tip_rate

    total_bill = bill_amount + tip_amount

    print(f'The tip is ${tip_amount:.2f}' )
    print(f'The total is ${total_bill:.2f}')

calculate_tip()