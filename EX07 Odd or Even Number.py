# Write the program to check the given number is ODD or EVEN

# SOLUTION

# First get the number from the user
number = int(input("Enter the number: "))

# Here we check the given number have any remainder or not. For Example, 10 % 2 = 0 so there is no remainder so
# number is even, how % works? if we check for number 10. it will split the number by 2,
# 2 + 2 + 2 + 2 + 2 = 0, here you can see there is no remainder so as a result given number 10 is even.
# 11 % 2 = 1, there is 1 as a remainder so the given number is odd.
# 2 + 2 + 2 + 2 + 2 + 1 = 1, here you can see that there is 1 number extra that is our
# remainder, as a result 11 is odd number.

if number % 2 == 0:
    print(f"The given number {number} is EVEN.")
else:
    print(f"The given number {number} is ODD.")


