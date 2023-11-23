from HIgher_lower_Game_data_And_Logo import data_for_game as ds, logo, vs
import random

score = 0
account_b = random.choice(ds)
while True:
    account_a = account_b
    account_b = random.choice(ds)

    while account_a == account_b:
        account_b = random.choice(ds)
    print(logo)
    print(f"Compare A: {account_a['name']}, {account_a['description']},from {account_a['country']}")

    print(vs)

    print(f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    account_a_followers = account_a["follower_count"]
    account_b_followers = account_b["follower_count"]

    if account_a_followers > account_b_followers and guess == "a":
        score += 1
        print(f"You are right! Current score: {score}")
    elif account_a_followers < account_b_followers and guess == "b":
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score is {score}.")
        break
