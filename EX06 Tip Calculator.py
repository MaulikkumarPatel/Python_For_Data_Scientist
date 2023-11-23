# write a program to add a tip and divide it by given user

# SOLUTION

print("Welcome to the tip calculator!")
# first we will get the amount from the user and note that it could be in decimal as well
bill = float(input("What was the total bill? £"))

# Now we will get the percentage of tip that you want to give.
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))

# Now get the number of users
share = int(input("How many people to split the bill?"))

# First divide the tip by 100 and multiply it with bill, so you get the tip amount now.
# Further, add the tip amount with bill.
calculation = tip / 100 * bill + bill

# Now divide the total amount by total person
total = (calculation / share)

#  Now get the amount it 2 decimal number
final_amount = round(total, 2)
print("Each person should pay: £{:0.2f}".format(total))


