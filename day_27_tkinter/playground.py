# Playing around with *args, which are multiple positional arguments

def add(*nums):
    total = 0
    for n in nums:
        total += n
    return total


print(add(3, 7, 10))

# Now playing around with *kwargs which is a dictionary
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=3, multiply=3)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)