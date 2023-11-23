# Make a calculator to get BMI value

# SOLUTION

# here we first get the values from user
height = input("Enter your height in M: ")
weight = input("Enter your weight in KG: ")

# here we have written the Equation to calculate the BMI value
# don't forget to convert input values in "weight into int data type and height into float data type"

# BMI = int(weight) / (float(height)*float(height))
BMI = int(weight) / float(height) ** 2

# if you don't want decimal number you must have to use change data type of BMI
print("Your BMI value is:", int(BMI))
