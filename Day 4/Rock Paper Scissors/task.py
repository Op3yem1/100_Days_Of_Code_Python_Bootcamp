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

#Start here
# I've used a for loop which was taught in later lessons so the user can play best of three.

game_options = [rock, paper, scissors]
for turn in range(0,3):
    computer_choice = random.choice(game_options)
    user_choice = input("Choose from rock, paper or scissors: ").lower()
    if user_choice == "rock":
        user_choice = game_options[0]
    elif user_choice == "paper":
        user_choice = game_options[1]
    elif user_choice == "scissors":
        user_choice = game_options[2]
    #displays the diagrams
    print(f"You played {user_choice}")
    print(f"I played {computer_choice}")

    if computer_choice == user_choice:
        print("DRAW")
    else:
        if user_choice == game_options[0]:
            if computer_choice == game_options[1]:
                print("You lose!")
            elif computer_choice == game_options[2]:
                print("You win!")
        elif user_choice == game_options[1]:
            if computer_choice == game_options[2]:
                print("You lose!")
            elif computer_choice == game_options[0]:
                print("You win!")
        elif user_choice == game_options[2]:
            if computer_choice == game_options[0]:
                print("You lose!")
            elif computer_choice == game_options[1]:
                print("You win!")
        else:
            print("Are you sure you spelled that correctly?")