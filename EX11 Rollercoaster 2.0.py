# Check the user's height is eligible for Roller-coaster or not and the price as per age.
# Height must be 120CM
# for under 11 £5, 12-18 £ 7, over 18 £ 12

# NEW update is you have to add one more option that customer want a picture or not. If yes then add £3 in bill.

# SOLUTION
print("Welcome to Roller-coater Ride!!")
height = int(input(f"Enter your height please: "))
bill = 0
if height >= 120:
    age = int(input("Please enter you age: "))
    if age <= 12:
        bill = 5
        print(f"You have to pay £ {bill}.")
    elif age <= 18:
        bill = 7
        print(f"You have to pay £ {bill}.")
    elif 45 <= age <= 55:
        print(f"Enjoy your free ride with us.")
    else:
        bill = 12
        print(f"You have to pay £ {bill}.")
    photo = input("Do you want a photo? Y or N: ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is £{bill}")
else:
    print("Sorry,you can note ride.")
