import random

from setuptools.windows_support import windows_only


def get_difficulty():
    while True:
        difficulty = input("Choose difficulty 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            no_guesses = 10
            return no_guesses
        elif difficulty == 'hard':
            no_guesses = 5
            return no_guesses


def get_number():
    while True:
        number = input("Make a guess: ")
        if number.isdigit():
            return int(number)

def number_guessing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number_to_guess = random.randint(1,100)
    print(f"Psst the number is {number_to_guess}")
    guesses_left = get_difficulty()
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left")
        player_guess = get_number()
        if player_guess == number_to_guess:
            print("You won!")
            break
        elif player_guess > number_to_guess:
            print("Too high")
        elif player_guess < number_to_guess:
            print("Too low")
        guesses_left -= 1
    if guesses_left == 0:
        print("No guesses left. You loose.")

number_guessing()
