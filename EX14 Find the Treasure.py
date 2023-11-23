while True:
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice = input("You're at a cross road, Where do you want to go? Type 'left' or 'right': ")

    if choice == 'left':
        two = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. "
                    "Type ""'swim' to swim across. : ")
        if two == 'wait':
            three = input("You arrived at island unharmed. There is a house with 3 doors. One red, one yellow, "
                          "one blue. Which door will you choose? ")
            if three == 'yellow':
                print("You found the treasure! You win!")
            elif three == 'red':
                print("Burned by fire. Game Over.")
            elif three == 'blue':
                print("Eaten by beasts. Game Over.")
            else:
                print("Game Over.")

        else:
            print("Attack by shark. Game Over")
    else:
        print("Fall in a hole. Game Over")
    option = input("Press any key to continue. q for Exit.")
    if option == 'q':
        break
    else:
        continue
