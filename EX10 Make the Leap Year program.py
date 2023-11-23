year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
else:
    print("Not leap year.")
    # 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600 not a leap years
    # 1600, 2000, 2400 Leap years
