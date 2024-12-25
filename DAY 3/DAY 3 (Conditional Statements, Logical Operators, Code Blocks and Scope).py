#DAY 3 (Conditional Statements, Logical Operators, Code Blocks and Scope)
#IF/ELSE
print("Welcome to the roller coaster!")
#height = int(input("Please enter your height\n"))
#if height>120:
   #print("You are eligible")
#else:
   #print("You are not eligible")
#OPERATORS(>. <, <=, >=, ==. !=)

print("To check if a number is even or odd")
#number = int(input("Enter any integer:\n"))
#if number%2==0:
    #print("The number is even")
#else:
    #print("The number is odd")

#OPERATORS(>. <, <=, >=, ==. !=)

#NESTED IF AND ELIF

print("Checking height with age")
# height = int(input("Please enter your height\n"))
# age = int(input("Please enter your age\n"))
# if height>120:
#     if age>=18:
#         print("Pay 12$")
#     else:
#         print("Pay 7$")
# else:
#     print("You are not eligible")

#TO COMMENT THE WHOLE CODE SELECT CODE AND PRESS CTRL+/

print("Checking height with age (under 12, b/w 12-18, over 18 using elif")
# height = int(input("Please enter your height\n"))
# age = int(input("Please enter your age\n"))
# if height>120:
#     if age<12:
#         print("Pay 5$")
#     elif age>=12 and age<=18:
#         print("Pay $7")
#     else:
#         print("Pay 12$")
# else:
#     print("You are not eligible")

#MULTIPLE IF
print("MULTIPLE IF STATEMENTS IN SUCCESSION")
# height = int(input("Please enter your height\n"))
# age = int(input("Please enter your age\n"))
# bill=0
# if height>120:
#     if age<12:
#         bill=5
#         print("Ticket price is 5$")
#     elif age>=12 and age<=18:
#         bill=7
#         print("Ticket price is $7")
#     else:
#         bill=12
#         print("Ticket price is 12$")
    
#     wants_photo = input("Do you want to have a photo take? Type y for yes and n for no. ")
#     if wants_photo == "y":
#         bill+=3
#         print(f"Your total bill is: {bill}")

# else:
#     print("You are not eligible")


#LOGICAL OPERATORS
# AND = BOTH SHOULD CORRECT
# OR = ONLY ONE CAN BE CORRECT
# NOT = REVERSE
print("Adding age 44-55 using logical operators to the existing code")
height = int(input("Please enter your height\n"))
age = int(input("Please enter your age\n"))
bill=0
if height>120:
    if age<12:
        bill=5
        print("Ticket price is 5$")
    elif age>=12 and age<=18:
        bill=7
        print("Ticket price is $7")
    elif 45<= age <=55: #compact shorthand way 
        print("Everything is going to be okay, Have a free ride on us!")
    else:
        bill=12
        print("Ticket price is 12$")
else:
    print("You are not eligible")