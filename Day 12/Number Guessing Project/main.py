import art
import random

print(art.logo)

def choose_number():
    """The function returns a random number from 1 to 100 (inclusive)."""
    return random.randint(1,101)
def return_lives(level):
    """The function returns the corresponding number of lives for the user's selected difficulty level. Takes an input parameter corresponding to the first letter of the difficulty level H - Hard, M - Medium, E - Easy. Returns None if parameter not valid"""
    difficulty_levels = {"H": 5, "M": 7, "E": 10}
    if level in difficulty_levels:
        return difficulty_levels[level]

num_to_guess = choose_number()
difficulty = input("Choose your difficulty - Hard (H), Medium (M) or Easy (E): ").upper()
lives_remaining = return_lives(difficulty)
print(f"You have {lives_remaining} attempts to guess the number.")
for life in range(0,lives_remaining):
    guess = int(input("Choose a number between 1 and 100: "))
    if guess == num_to_guess:
        print(f"Wow! You guessed the right number! Well done!")
        break
    else:
        lives_remaining -= 1
        if lives_remaining > 0:
            if guess < num_to_guess:
                print(f"Too low!\nTry again, you have {lives_remaining} tries remaining")
            else:
                print(f"Too high!\nTry again, you have {lives_remaining} tries remaining")
        else:
            print(f"You are out of tries! Goodbye!")