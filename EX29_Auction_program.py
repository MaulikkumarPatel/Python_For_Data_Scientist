# from replit import clear
from EX29_auction_logo import logo

print(logo)
bids = {}
while True:
    name = input("Enter your name please: ")
    amount = int(input("Enter your bid £: "))
    bids[name] = amount
    option = input("Are there any other bidders? Type 'yes' or 'no'.")
    if option == 'no':
        print(f"The winner is {max(bids.keys())} with a bid of £{max(bids.values())}.")
        break
    else:
        # clear()
        continue
