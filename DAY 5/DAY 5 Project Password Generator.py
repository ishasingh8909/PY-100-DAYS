import random
print("Welcome to the PyPassword Generator!")
alpha_range = int(input("How many letters would you like in your password?\n"))
symbol_range = int(input("How many symbols would you like?\n"))
num_range = int(input("How many numbers would you like?\n"))
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["~","!","@","#","$","%","^","&","_","-","+","=","{","[","}"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
#EASY LEVEL
# password = ""
# for char in  range(0,alpha_range):  
#     password+=random.choice(alpha)
# for char in range(0, symbol_range):
#     password+=random.choice(symbols)
# for char in range(0, num_range):
#     password+=random.choice(numbers)
# print(password)

#HARD LEVEL
password_list = []
for char in  range(0,alpha_range):  
    password_list.append(random.choice(alpha))
for char in range(0, symbol_range):
    password_list.append(random.choice(symbols))
for char in range(0, num_range):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

#converting this list into a password string
password=""
for char in password_list:
    password+=char
print(f"Your final password is: {password}")