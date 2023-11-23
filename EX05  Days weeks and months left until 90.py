# Create a program that tells us,
# how many days, weeks, months we have left if we live until 90 years old.


# SOLUTION

# First of all we will ge the age from the user
age = input("What is your current age? ")

# Here we have convert age into days week and months
# Make sure first you get to remain age then after multiply it with days weeks and months

# age_days = (90 - int(age)) * 365
# age_week = (90 - int(age)) * 52
# age_months = (90 - int(age)) * 12

years_remain = 90 - int(age)
age_days = years_remain * 365
age_week = years_remain * 52
age_months = years_remain * 12

print(f"You have {age_days} days, {age_week} weeks, and {age_months} months left.")
