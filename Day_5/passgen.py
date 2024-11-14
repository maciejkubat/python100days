import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letter = int(input("How many letters you would like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

pass_length = num_letter + num_symbols + num_numbers
password=[]
letters_used = 0
symbols_used = 0
numbers_used = 0
while len(password) < pass_length:
    choice = random.randint(1,3)
    if choice == 1 and letters_used < num_letter:
        letter = random.choice(letters)
        password.append(letter)
        letters_used += 1
    if choice == 2 and symbols_used < num_symbols:
        symbol = random.choice(symbols)
        password.append(symbol)
        symbols_used += 1
    if choice == 3 and numbers_used < num_numbers:
        number = random.choice(numbers)
        password.append(number)
        numbers_used += 1
print("Your password")
passwd = ''.join(password)
print(passwd)

#or you could just use shuffle