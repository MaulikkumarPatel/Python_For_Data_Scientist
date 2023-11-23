import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img = [rock, paper, scissors]
human_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if human_option >= 3 or human_option < 0:
    print("Invalid number")
else:

    print(f"You choose:\n")
    print(game_img[human_option])
    comp = random.randint(0, 2)
    print(f"Computer choose:\n")
    print(game_img[comp])
    if human_option == comp:
        print("The game is Draw")
    elif human_option == 0 and comp == 1:
        print("You lose the game")
    elif human_option == 0 and comp == 2:
        print("You Won the Game")
    elif human_option == 1 and comp == 0:
        print("You Won the Game")
    elif human_option == 1 and comp == 2:
        print("You lose the Game")
    elif human_option == 2 and comp == 0:
        print("You Won the Game")
    elif human_option == 2 and comp == 1:
        print("You Won the Game")
    else:
        print("Invalid input")
