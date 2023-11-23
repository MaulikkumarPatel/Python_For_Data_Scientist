# Swap two number

# a= 10
# b= 20

# Result

# a= 20
# b=10

# Solution

# First of all we will take input from user and store in two different variables.

a = input("a: ")
b = input("b: ")

# Here's what happens when this code is executed:
# 1 The current value of a is assigned to c.
# 2 The current value of b is assigned to a.
# 3 The value of c (which is the original value of a) is assigned to b.
# After this code has executed, the values of a and b have been swapped.

c = a
a = b
b = c

# Output

print("======== RESULT =========")
print("a = " + a)
print("b = " + b)
print("Numbers are swapped Successfully")