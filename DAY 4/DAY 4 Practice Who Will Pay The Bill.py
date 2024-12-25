friends = ["Alice","Bob", "Charlie", "David", "Emanuel"]
#udemy option 1
import random
random_index = random.randint(0,4)
print(friends[random_index])

#udemy option 2
print(random.choice(friends))

#MY CODE
bill_payer_name = random.randint(0,4)
if bill_payer_name == 0:
    print(friends[0])
elif bill_payer_name == 1:
    print(friends[1])
elif bill_payer_name == 2:
    print(friends[2])
elif bill_payer_name == 3:
    print(friends[3])
else:
    print(friends[4])