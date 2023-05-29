""""
Flow Chart:

1. Start code -> Display pixel art if you want
2. Ask for name & Bid
    -Store this in a dictionary. Continually add to the dictionary

4. Ask if anyone else wants to bid
    -If yes, clear the screen and run again
    -If no, loop through the dictionary and find the highest key and value. Mostly value.


"""

bids = {}
going = True
def clear():
    print("\n" * 50)


def find_winner():
    global winner
    for bidder in bids:
        amount = bids[bidder]
        winner = amount
        if amount > winner:
            winner = amount

def find_name():
    global name
    key_list = list(bids.keys())
    val_list = list(bids.values())
    position = val_list.index(winner)
    name = key_list[position]


def add_bidders():
    name = input("What is your name?: ")
    bid = input("Enter your bid: $")
    bids[name] = bid



while going:
    add_bidders()
    again = input('Would you like to add another person? (Yes/No): ').lower()
    if again == "no":
        going = False
    else:
        pass

find_winner()
find_name()
print(f'The winner is {name} who bid {winner} dollars.')