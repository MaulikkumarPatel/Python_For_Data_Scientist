import random
import hangman_logo
import hangman_list

lives = 6

word_list = hangman_list.word_list
chosen_word = random.choice(word_list)
print(hangman_logo.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
chosen_word = list(chosen_word)

while display != chosen_word:
    print(display)
    guess = input("Guess a letter: ").lower()
    if lives == 0:
        print("Sorry, You lose the game.")
        break
    elif guess not in chosen_word:
        lives -= 1
        print(hangman_logo.stages[lives])
        # print(f"You have {lives} left to complete the game.")
        print(f"You choose {guess} is not in the word. You lose a life")
    elif guess in display:
        print(f"You have already choose {guess} letter. Please choose another.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
if display == chosen_word:
    print(f"{display} \n You guess the correct word. Congrats!!! \n You won the game.")
