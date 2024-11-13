print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif 45 <= age <= 55:
        print("You are going to be ok, ride is on us")
        bill = 0
    else:
        bill = 12
    picture = (input("Do you want a pic with that? (Yes,No) ").lower())
    if picture == "yes":
        bill += 3
    print(f"That will be ${bill}")
else:
    print("Sorry mate")