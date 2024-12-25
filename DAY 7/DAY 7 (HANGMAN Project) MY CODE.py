stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |''']

#1. Picking random words and checking answers
import random

word_list = ["hangman","game","wordgame"] #1. (making a list to chose from) 

print(""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  """)

random_word = random.choice(word_list)  #1. (choosing random number )
print(random_word)

placeholder = "" #2. Placing placeholders wrt to the len of the word
word_length = len(random_word)
for i in range(word_length):
    placeholder += "_"
print(placeholder)

# for char in random_word:
#     user_input=input("Enter the character: ").lower()
#     if user_input == char:
#         print("Right")
#     else:
#         print("Wrong")                          #1. (Tells whether the input matches with the word or not)

#2. replacing blanks with guesses
# new_string = ""
# for char in random_word:
#     user_input=input("Enter the character: ").lower()
#     while user_input == char:
#         if user_input == char:
#             new_string += char
#         else:
#             new_string+="_"
#     print(new_string)               #2. Adds _ if words is not there, and the word itself if matches

# 3. checking if the player has won

game_over = False  #3. condn to execute the while loop
correct_list = [] 

lives = 6


while not game_over:
    print(f"*******************************************{lives}/6 LIVES LEFT*******************************************")
    user_input=input("Enter the character: ").lower()

    #if user has printed a letter they've already guessed.
    if user_input == correct_list:
        print(f"You've already guessed {user_input}")

    new_string = ""

    for char in random_word:
        if user_input == char:
            new_string += char
            correct_list.append(char) #a3. ppends the char which matches with the word
        elif char in correct_list: #3. adds the letters which are already there in the list as well
            new_string += char
        else:
            new_string+="_"
    print("Word to guess: " + new_string)

    #Let them know they have choosed a wrong word and will loose a live.


    if user_input not in random_word:
        lives -= 1
        print(f"You guessed {user_input}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(F"*******************************************IT WAS {random_word}! YOU LOSE*******************************************")
    
    if "_" not in new_string:
        game_over=True
        print(f"*******************************************YOU WIN*******************************************") 
    
    print(stages[lives])  #4. Keeping track of the player's lives

#5. Improving the User Experience
# 1 step: add all words in a py file and save it eg(hangman_words.py), now use import hangman_words, so now you can use hangman_words.word_list
# 2 step: In similar way import hangman_art as a module. [stages]
# 3 step: import logo from same hangman_art file [logo]