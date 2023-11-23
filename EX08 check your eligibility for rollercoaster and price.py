# Check the user's height is eligible for Roller-coaster or not and the price as per age.
# Height must be 120CM
# for under 11 £5, 12-18 £ 7, over 18 £ 12


print("Welcome to Roller-coater Ride!!")
height = int(input(f"Enter your height please: "))
if height >= 120:
    age = int(input("Please enter you age: "))
    if age <= 12:
        print("You have to pay £5.")
    elif age <= 18:
        print("You have to pay £7.")
    else:
        print("You have to pay £12.")
else:
    print("Sorry,you can note ride.")




