# Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

print("Welcome to the tip calculator!")
bill = float(input("How much was the total bill? "))
tip = int(input("How much tip you like to give? 10, 12 or 15? "))
splitBill = int(input("how many people to split the bill? "))

billResult = float((bill + (bill*(tip/100)))/splitBill)

print(f"Each person should pay : {billResult}")



# type() - returns the data type of a variable or value
# len() - returns the length of an integer