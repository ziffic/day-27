def add(*arg):
    total = 0
    for n in arg:
        total += n
    return total


print(add(1, 2, 1, 1, 1))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiple"]
    print(n)


calculate(2, add=3, multiple=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colors")
        self.seats = kw.get("seats")
