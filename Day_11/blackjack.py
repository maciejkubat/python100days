import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_score(card_list, who):
    print(f"{who} cards: {card_list}, current score: {sum(card_list)}")

def draw_a_card(card_list):
    drawn_card = random.choice(cards)
    card_list.append(drawn_card)
    card_sum = sum(card_list)
    if drawn_card == 11 and card_sum > 21:
        card_list[-1] = 1
    return card_list

def get_initial_cards():
    return [random.choice(cards), random.choice(cards)]

def blackjack():
    print(art.logo)
    player_cards = get_initial_cards()
    card_sum = sum(player_cards)
    computer_cards = get_initial_cards()
    computer_sum = sum(computer_cards)
    print_score(player_cards, "Player's")
    print(f"Computer's first card: {computer_cards[0]}")
    another_card = True
    while another_card:
        next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if next_card == "y":
            player_cards = draw_a_card(player_cards)
            card_sum = sum(player_cards)
            if card_sum > 21:
                print_score(player_cards, "Player's")
                print("You loose")
                another_card = False
            else:
                print_score(player_cards, "Player's")
        else:
            while computer_sum < 17:
                draw_a_card(computer_cards)
                computer_sum = sum(computer_cards)
            print_score(computer_cards, "Computer's")
            if computer_sum == 21 or (card_sum < computer_sum < 21):
                print("Computer wins!")
            elif computer_sum == card_sum:
                print("It's a draw")
            else:
                print("Player wins!")
            another_card = False

game_on = True
while game_on:
    another_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if another_game == "y":
        blackjack()
    else:
        print("Bye!")
        game_on = False