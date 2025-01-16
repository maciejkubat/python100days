import random

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letter = random.randint(8,10)
    num_symbols = random.randint(2,4)
    num_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(num_letter)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

    password = password_letters + password_symbols + password_numbers
    random.shuffle(password)
    passwd = ''.join(password)
    return passwd

#or you could just use shuffle