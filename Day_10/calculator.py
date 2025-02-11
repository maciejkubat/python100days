import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "error, div by 0"

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

print(art.calculator)

first_number = float(input("Enter first number: "))
operate = True
while operate:
    operator = input("Choose and operator '+','-','*','/': ")
    second_number = float(input("Input second number: "))
    result = operations[operator](first_number,second_number)
    print(f"{first_number}{operator}{second_number}={result}")
    do_continue = input("Do you want to continue?(yes/no)").lower()
    if do_continue == "yes":
        first_number = result
    else:
        first_number = float(input("Enter first number: "))
