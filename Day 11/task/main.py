"""Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:"""

import art
import random
print (art.logo)

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
players_cards = []
total_hand = 0
dealers_cards = []
dealers_hand = 0
your_turn = True

def hit():
    """Returns a random card from the deck"""
    picked_card = random.choice(list(cards))
    card_value = cards[picked_card]
    return card_value
def redefine_ace(ace,total):
    """If an Ace is drawn, the calculated total will determine if the Ace's value will be 11 or 1. If the Total exceeds 21 after drawing an Ace, the Ace value will be redefined to 1. """
    total += ace
    if total > 21:
        ace = 1
    else:
        ace = 11
    return ace
def check_blackjack(cards_to_check):
    """By passing in a list of cards, the function checks if the list contains a value of 10 (either from a Jack, Queen or King) and 11 (an Ace). If both cards are in the user's hand, then they have won as they have a blackjack."""
    if 11 in cards_to_check and 10 in cards_to_check:
        return True
    else:
        return False

for turn in range(0,2):
    go = hit()
    if go == 11:
        go = redefine_ace(ace=go,total=total_hand)
    total_hand += go
    players_cards.append(go)
    print(f"Your cards: {players_cards}. Total hand = {total_hand}")
    go = hit()
    dealers_hand += go
    dealers_cards.append(go)
    if turn != 1:
        print(f"Dealer's card 1: {dealers_cards}\n")

game_over = check_blackjack(dealers_cards)
if game_over:
    print(f"You lose! The dealer had a blackjack!")
else:
    game_over = check_blackjack(players_cards)
    if game_over:
        print(f"You win! You had a blackjack!")

if not game_over:
    player_choice = input("Hit or Stand?").lower()
    if player_choice == "hit":
        go = hit()
        if go == 11:
            go = redefine_ace(ace=go,total=total_hand)
        total_hand += go
        players_cards.append(go)

    print(f"Your hand: {total_hand}")
    print(f"Dealer's hand: {dealers_hand}\n")

    while dealers_hand < 16:
        go = hit()
        dealers_hand += go
        dealers_cards.append(go)

    if dealers_hand > 21:
        print(f"You win! The dealer had a bust with a value of {dealers_hand}!")
    else:
        if total_hand <= 21:
            if total_hand > dealers_hand:
                print(f"You win! Your hand equals {total_hand}")
            elif total_hand == dealers_hand:
                print(f"That's a push! You both have a value of {total_hand}")
            else:
                print(f"You lose! The dealer's hand exceeded yours with a value of {dealers_hand}")
        else:
            print(f"That's a bust! Your hand exceeded a value of 21")