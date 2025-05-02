# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import os

def clear_console():
    # Clears the console (works on Windows and Unix-based systems)
    print("\n" * 20)
    #os.system('cls')

def blind_auction():
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("Enter your name: ")
        bid = int(input("Enter your bid: £"))
        bids[name] = bid

        more_bidders = input("Are there others who need to bid? Type 'yes' or 'no': ").lower()
        if more_bidders == 'no':
            bidding_finished = True
        else:
            clear_console()

    highest_bid = max(bids.values())
    winner = [name for name, bid in bids.items() if bid == highest_bid][0]
    print(f"The winner is {winner} with a bid of £{highest_bid}!")

blind_auction()

