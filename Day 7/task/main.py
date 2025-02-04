import random

# 1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
import hangman_art

lives = 6

# 3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    # 6: - Update the code below to tell the user how many lives they have left.
    print(f"You have {lives} lives left\n")
    guess = input("Guess a letter: ").lower()


    # 4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guessed_letters.__contains__(guess):
        print(f"You have already guessed {guess} before. Try another letter\n")
    guessed_letters.append(guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # 5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word and not guessed_letters.__contains__(guess):
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True

            # 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"The word was {chosen_word}! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("YOU WIN")

    # 2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
