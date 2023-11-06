#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 
bill = float(input("What is the total of the bill?\n"))

people = int(input("How many people attended?\n"))

tip = float(input("How much was the tip percentage?\n"))

# Calculate the total bill including the tip
bill_total = ((tip / 100) * bill) + bill

# Calculate how much each person should pay
bill_per_person = bill_total / people

# Use an f-string to construct the message and print it
print(f"Each person should pay: ${bill_per_person}")