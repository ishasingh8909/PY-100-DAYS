# DAY 4 (Randomization and Py Lists)
#RANDOM MODULE
import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float_no_0_to_1 = random.random()
print(random_float_no_0_to_1)

random_float_no_0_to_10 = random.random() * 10
print(random_float_no_0_to_10)

random_float = random.uniform(1,10)
print(random_float)

random_toss = random.randint(0,1)
if random_toss == 0:
    print("Heads")
else:
    print("Tails")

#LISTS

fruits = ["apple",'banana', "cherry", "orange"]
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits[0] = "anar"
print(fruits)

fruits.append("pear")
print(fruits)

fruits.extend(["guava", "mangoe", "plum"])
print(fruits)