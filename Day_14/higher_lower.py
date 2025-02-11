import random
import game_data
import art
import os

def clear_console():
    os.system('clear')

def get_and_remove_random_choice(my_list):
    choice = random.choice(my_list)
    my_list.remove(choice)
    return choice

def return_winner(contestant_a, contestant_b):
    if contestant_a['follower_count'] > contestant_b['follower_count']:
        return 'A'
    else:
        return 'B'

def present_choice(choice):
    combined = f"{choice['name']}, a {choice['description']}, from {choice['country']}"
    return combined

def play_round(contestant_a, contestant_b):
    print(f"Compare A:{present_choice(contestant_a)}")
    print(art.vs)
    print(f"Compare B:{present_choice(contestant_b)}")
    winner = return_winner(contestant_a, contestant_b)
    user_choice = input("Who has more followers? Type 'A' or 'B'").capitalize()
    if user_choice == winner:
        return 'guess'
    elif user_choice == 'A' or user_choice == 'B':
        return 'miss'
    else:
        'wrong'

def play_game():
    score = 0
    choice_a = get_and_remove_random_choice(game_data.data)
    choice_b = get_and_remove_random_choice(game_data.data)
    print(art.logo)
    game_is_on = True
    while game_is_on:
        round_result = play_round(choice_a, choice_b)
        if round_result == 'guess':
            choice_a = choice_b
            choice_b = get_and_remove_random_choice(game_data.data)
            score += 1
            clear_console()
            print(art.logo)
            print(f"You guessed. Current score: {score}")
        elif round_result == 'miss':
            clear_console()
            print(art.logo)
            print(f"You missed. Your final score: {score}")
            game_is_on = False
        else:
            clear_console()
            print(art.logo)
            print(f"Wrong input. Your final score: {score}")
            game_is_on = False

play_game()
# 2 Present the data

# 3 User choice

