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
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

hand_symbols = [rock,paper,scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice<=2 or user_choice<=0:
    print(hand_symbols[user_choice])   
else:
    print("INVALID INPUT")

import random
computer_choice = random.randint(0,2)
print("Computer Chose:")
print(hand_symbols[computer_choice])

if computer_choice == user_choice:
    print("This is a draw")
elif (computer_choice == 0 and user_choice == 1) or (computer_choice == 2 and user_choice == 0) or (computer_choice == 1 and user_choice == 2):
    print("Congratulation! You Win")
elif user_choice>2 or user_choice<0:
    print("Invalid input")
else:
    print("Better luck next time! You Lose")