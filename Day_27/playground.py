def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))  # 15


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

    def __str__(self):
        return f"{self.make} {self.model}"

my_car = Car(make="Nissan", model="GT-R")
print(my_car)  # Nissan GT-R