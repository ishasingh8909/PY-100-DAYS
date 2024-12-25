#MY CODE
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
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
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else: 
    print(scissor)

import random
computer_choice = random.randint(0,2)
print("Computer chose: ")  
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else: 
    print(scissor)

if computer_choice == user_choice:
    print("This is a draw")
elif (computer_choice == 0 and user_choice == 1) or (computer_choice == 2 and user_choice == 0) or (computer_choice == 1 and user_choice == 2):
    print("Congratulation! You Win")
elif user_choice>2 or user_choice<0:
    print("Invalid input")
else:
    print("Better luck next time! You Lose")

#udemy code
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissor = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# game_images = [rock,paper,scissor]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# if user_choice>=0 and user_choice<=2:
#     print(game_images[user_choice])

# computer_choice = random.randint(0,2)
# print("Computer chose:")  
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("Invalid Number")
# elif user_choice == 0 and computer_choice == 2:
#     print("You Win!")
# elif computer_choice> user_choice:
#     print("You Lose!")
# elif computer_choice< user_choice:
#     print("You Win!")
# elif user_choice == 2 and computer_choice == 0:
#     print("You Lose!")
# elif computer_choice == user_choice:
#     print("It's a draw")
