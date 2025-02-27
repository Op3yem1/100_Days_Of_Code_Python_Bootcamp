#Higher or Lower Game plan:
import random
import art
import game_data

continue_playing = True
comparison_A = ''
comparison_B = ''
score = 0

def generate_selection(index):
    """The function returns a random selection from the list of dictionaries in game_data.data and returns a formatted statement such as 'Selena Gomez, a Musician from United States'."""
    selection = game_data.data[index]
    statement = f"{selection["name"]}, a {selection["description"]} from {selection["country"]}"
    return statement

def higher_or_lower(index_a,index_b):
    """Compares the follower count of B against A. If the second comparison has more followers, the function returns 'Higher' otherwise, it returns 'Lower' """
    followers_a = game_data.data[index_a]["follower_count"]
    followers_b = game_data.data[index_b]["follower_count"]
    if followers_b > followers_a:
        return "Higher"
    else:
        return "Lower"

while continue_playing:
    #Display logo
    print(art.logo)
    #Select random A to compare against random B. e.g Compare 'name', a 'description' from 'country'
    random_num = random.randrange(0, len(game_data.data) - 1)
    random_num2 = random.randrange(0, len(game_data.data) - 1)
    while random_num2 == random_num:
        random_num2 = random.randrange(0, len(game_data.data) - 1)

    if comparison_A == '':
        comparison_A = generate_selection(random_num)
        f_count_A = game_data.data[random_num]["follower_count"]
    else:
        comparison_A = comparison_B
        f_count_A = f_count_B
    print(f"Compare {comparison_A} - {f_count_A} million followers")

    #Display vs
    print(art.vs)

    comparison_B = generate_selection(random_num2)
    f_count_B = game_data.data[random_num2]["follower_count"]
    print(f"Against {comparison_B}")

    user_choice = input("Higher or Lower? ").title()
    result = higher_or_lower(random_num,random_num2)
    #If user choice correct, add +1 score, play again. Random B becomes random A. Select new random B to compare against.
    if user_choice == result:
        score += 1
        print(f"Correct! Your current score is {score}.")
    else:
        #If user choice incorrect, display you lose, terminate game. Show final score.
        print(f"Your final score is {score}")
        continue_playing = False