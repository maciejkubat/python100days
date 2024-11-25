import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for candidate in range(5, int(math.sqrt(num)),6):
            if num % candidate == 0:
                return False
        return True

print(is_prime(73))
print(is_prime(75))
