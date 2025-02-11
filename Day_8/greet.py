def greet():
    print(f"Hello")
    print(f"How are you today?")
    print(f"I am a computer program.")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today?")
    print(f"I am a computer program.")

greet_with_name("John")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(location="London", name="John")
