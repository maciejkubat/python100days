print("Welcome to tip calculator!")
total = input("What was the total bill? $")
total = float(total)
tip = input("How much tip would you like to give? 10, 12 or 15? ")
tip = float(tip)
no_of_people = input("How many people to split the bill? ")
no_of_people = float(no_of_people)

per_peron_bill = total * (1 + tip / 100) / no_of_people
per_person_bill = round(per_peron_bill,2)

print(f"Each person should pay: {per_person_bill}")