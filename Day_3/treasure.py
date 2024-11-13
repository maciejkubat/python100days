chest = '''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   |
             \________________\####/________________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.[uuu].-'    __/ \__ |
              |============= .'.'^'.'.=============|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

'''
print(chest)
print('Welcome to Treasure Island, your mission is to find a chest')
decision_1 = input("You wake up on a beach, you see two paths. Which one do you choose left or right?").lower()
if decision_1 == "right":
    print("You got eaten by gigantic spider. You die. Your adventure is over.")
elif decision_1 == "left":
    decision_2 = input("You venture deep into the island. You stumble on a lake. What do you do? Swim or wait?").lower()
    if decision_2 == "swim":
        print("You tried to swim. But you failed and ended up dead. Game over.")
    elif decision_2 == "wait":
        decision_3 = input("You wait and wait. And finally a set of magical doors appear. Which one do you choose red, blue or yellow?").lower()
        if decision_3 == "yellow":
            print("Yay! You found a treasure!")
        elif decision_3 == "red":
            print("Nope. You died. Game over.")
        elif decision_3 == "blue":
            print("Blue is nice. But nope. Game over.")
        else:
            print("You tried something else. But it did not work and you finished dead. Game over.")
    else:
        print("You tried something else. But it did not work and you finished dead. Game over.")
else:
    print("You tried something else. But it did not work and you finished dead. Game over.")
