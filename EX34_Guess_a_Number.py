import random

print(
    "Hello!!! \nWelcome to the Number Guessing Game. \nGuess a number between 1 to 100.\nNOTE: Easy level have 5 "
    "attempts to guess a number "
    "and 10 attempts for the Hard level.\nAll the best.")

game_mode = input("\nChoose a game level. Type 'easy' or 'hard': ")

answer = random.choice(range(1, 100))

total_guess = ""

if game_mode == "easy":
    total_guess = 10
else:
    total_guess = 5

while total_guess != 0:

    user_guess = int(input("\nMake a Guess: "))
    if answer == user_guess:
        print(f"You made a correct guess. {answer} is a right number. Great!!!")
        break
    elif user_guess > answer:
        print("Guess Number is High. Try lower number")
    elif user_guess < answer:
        print("Guess Number is Low. Try higher number")
    else:
        print("ENTER A NUMBERS ONLY")
    total_guess -= 1
    print(f"You have {total_guess} left to guess a correct number.")

if total_guess == 0:
    print("\nYour total number of guessing a number is finished. Better luck next time.")