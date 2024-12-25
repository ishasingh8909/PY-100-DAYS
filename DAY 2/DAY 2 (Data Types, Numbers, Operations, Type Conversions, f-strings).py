#DAY 2 (Data Types, Numbers, Operations, Type Conversions, f-strings)
#1. DATA TYPES (Str, Int, Float, Boolean)
#Str
print("Hello"[0])
print("Hello"[-1])
#Int = whole no.
print(12+12)
#Float
print(3.149)
#Boolean
print("True or False")
#2. TYPE CASTING AND CHECKING
#Type Conversion or Casting
print(len(str(12345))) 
print("123"+("123"))
print(int("123")+(int("123")))
#Type Checking
a= "Isha" 
print(type(a)) 
print(type(32))
print(type(3.2))
print(type(True))
#print("No. of letters in your name: " + str(len(input("Enter your name")))) #you can only concatinate str , as len is int it gives error without conversion
#3. MATHEMATICAL OPERATIONS
print(12+12) #addition
print(13-12) #substraction
print(12*12) #multiplication
print(27/12) #division <float>
print(27//12)#floor division <int>
print(12%2)  #Modulo, gives remainder
print(2**3)  #power
#PEMDAS = (), **, *. /, +, -
print(3*3+3/3-3)
#Change o/p to 3
print(3*(3+3)/3-3)

# Calculate the bmi using weight and height.
height = 1.65 
weight = 84
bmi = weight/height**2

print(bmi)

#4. NUMBER MANIPULATION
print(int(bmi)) #not optimal
print(round(bmi))
print(round(bmi, 2))

score = 0
score+=1
print(score)

#f-strings
score=0
height=1.8
is_winning = True

print(f"Your score is: {score}") #dosen't needs to change data types
print(f"Your score is: {score}, Your height is: {height}. Winning Status: {is_winning}")

#EXCEPT STR NO OTHER DATA TYPES CAN BE CONCATENATED

