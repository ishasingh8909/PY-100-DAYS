#MY CODE
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M or L: \n")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
# extra_cheese = input("Do you want extra cheese on your pizza? Y or N: \n")
# pizza_price = 0
# if size == "S":
#     pizza_price = 15
#     if pepperoni == "Y":
#         pizza_price += 2
#     if extra_cheese == "Y":
#         pizza_price +=1
# elif size == "M":
#     pizza_price = 20
#     if pepperoni == "Y":
#         pizza_price += 3
#     if extra_cheese == "Y":
#         pizza_price +=1
# elif size=="L": 
#     pizza_price = 25
#     if pepperoni == "Y":
#         pizza_price += 3
#     if extra_cheese == "Y":
#         pizza_price +=1
# else:
#     print("You printed a wrong input")

# print(f"Your Pizza Price is: {pizza_price}")


#UDEMY 
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L: \n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: \n")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else: 
    print("Enter correct value")

if pepperoni == "Y":
    if size == "S":
        bill+=2
    else: 
        bill+=3

if extra_cheese == "Y":
    bill +=1

print(f"You Pizza Bill Is: {bill}")