#DAY 8(Functions with inputs)
def greet():
    print("Marry")
    print("Christmas")
    print("Ho! Ho! Ho!")

greet()

#Function with input
def greeting(name): #parameter
    print("Hello " + name)
    print("Marry Chrsitmas")
    print("Ho! Ho! Ho!")

greeting("Angela") #argument
greeting("Isha")

#Positional v/s Keyword arguemnts.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's {location} Weather?")

greet_with("Kirti","Chicago")
greet_with("Chicago","Kirti") #positional
greet_with(location="Italy",name="Sonal") #keyword