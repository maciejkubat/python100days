import random
from random import randint

friends = ["Alice", "Bob", "Norman", "George", "Bill", "Ted", "Mike"]

picker = randint(0, len(friends) - 1)

print(f"{friends[picker]} pays the bill")

# option 2
print((random.choice(friends)))