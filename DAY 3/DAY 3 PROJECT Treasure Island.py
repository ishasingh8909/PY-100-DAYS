print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
road_direction = input('You\'re at a CrossRoad. Where do you want to go?\n Type "left" or "right".\n').lower()
if road_direction == "left":
    cross_lake = input("You have come to a lake.\n Type wait to wait for a boat. Type swim to swim across.").lower()
    if cross_lake == "wait":
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors,\n One red, one yellow, and one blue. Which colour do you choose?").lower()
        if door_color == "red":
            print("It's a room full of fire. Game Over")
        elif door_color == "yellow":
            print("You found the Treasure. You Win!")
        elif door_color == "blue":
            print("You entered a room of Beasts. Game Over.")
        else:
            print("You have choosed an unexisting door. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
        
else:
    print("You fell into a hole. Game Over.")

# print("Welcome to the Treasure Island.")
# print("Your mission is to find the treasure.")
# road_direction = input('You\'re at a CrossRoad. Where do you want to go?\n Type "left" or "right".').islower()
# if road_direction == "left":
#     cross_lake = input("You have come to a lake.\n Type wait to wait for a boat. Type swim to swim across.").islower()
# else:
#     print("You fell into a hole. Game Over.")
        
