'''
Build a program that asks the user to enter the length and width of a 
room, in meters, then prints the room's area in both 
square meters and square feet.

Note: 1 square meter == 10.7639 square feet

'''


CONVERSION_TO_SQ_FT = 10.7639
print("Type 'mt' to caculate in square feet or type 'ft' to calculate in meter")
print("What measurement do you want?")
type = input()


print("What is the length of the room in meters?")
length = float(input())

# length_mtr = float(length)


print("What is the width of the room in meters?")
width = float(input())

# width_mtr = float(width)

if type == "mt":
    area_sq_mtr = length * width
    print(f"Area of the room is {area_sq_mtr:.2f} square meter")
elif type == "ft":
    area_sq_ft = length * width
    print(f"Area of the room is {area_sq_ft: .2f} square feet")
