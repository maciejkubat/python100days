import random

hangman_stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |    
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    
     |    
     |    
     |
    -----
    """
]

word_list = ["aardvark", "baboon", "camel"]
lives = len(hangman_stages)

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = "_" * len(chosen_word)
placeholder_list = list(placeholder)
print(placeholder)

game_not_over = True
while game_not_over:
    selected_letter = input("Guess a letter: ").lower()
    if selected_letter in placeholder_list:
        print(f"You've already guessed {selected_letter}")
    elif selected_letter in chosen_word:
        print("Correct!")
        if lives != len(hangman_stages):
            print(hangman_stages[lives])
        for index, letter in enumerate(chosen_word):
            if letter == selected_letter:
                placeholder_list[index] = selected_letter
    else:
        lives -= 1
        print(hangman_stages[lives])
        if lives == 0:
            game_not_over = False
            print("You lose!")
            break
    guessed_word = ''.join(placeholder_list)
    print(guessed_word)
    if guessed_word == chosen_word:
        game_not_over = False
        print("You win!")
        break

