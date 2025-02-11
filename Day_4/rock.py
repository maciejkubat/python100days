import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps_list = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0,2)
if 0 < choice < len(rps_list) - 1:
    print(rps_list[choice])
print("Computer choose:")
print(rps_list[computer_choice])
if choice >= 3 or choice < 0:
    print("Wrong choice")
elif choice == 0 and computer_choice == 2:
    print ('You win!')
elif choice == 2 and computer_choice == 1:
    print('You win!')
elif choice == 1 and computer_choice == 0:
    print('You win!')
elif choice == computer_choice:
    print("It's a draw")
else:
    print('You loose. Sorry.')