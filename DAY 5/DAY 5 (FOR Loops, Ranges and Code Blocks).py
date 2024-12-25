# DAY 5 (FOR Loops, Ranges and Code Blocks)
#FOR LOOP
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scores = [23,56,89,53,14,12,15,65,48,76,21,12]
total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
    sum+=score #sum=sum+score
print(sum)

max_score = 0
for score in student_scores:
    if score>max_score:
        max_score = score
        
print(max_score)

#FOR LOOPS AND THE RANGE
for number in range(1,10):
    print(number)

print("Range with a gap of 2")
for number in range(1,10, 2):
    print(number)

print("Sum of numbers from 1-100")

sum=0
for number in range(1,101):
    sum+=number
print(sum)   


