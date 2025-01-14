# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
# To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

#MY_CODE
def calculate_love_score(name1, name2):
    list_of_word = ["true","love"]
    true_total = 0
    for char in name1:
        if char in list_of_word[0]: 
            true_total+=1
    for char in name2:
        if char in list_of_word[0]: 
            true_total+=1

    love_total=0
    for char in name1:
        if char in list_of_word[1]: 
            love_total+=1
    for char in name2:
        if char in list_of_word[1]: 
            love_total+=1
    
    score = int(str(true_total)+str(love_total))
    print(score)

calculate_love_score("Kanye West","Kim Kardashian")

#UDEMY
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")    
