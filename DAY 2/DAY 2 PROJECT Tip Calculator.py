print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $\n"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))
final_bill = (tip_percentage/100*total_bill+total_bill)/no_of_people
rounded_bill = round(final_bill, 2)
print(f"Each person should pay: {rounded_bill}")

#LOGIC 
# tip as % = tip/100
# total tip amount = %tip*bill
# final bill = total tip amount + bill