import math

c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)


def mul(a, b):
    return a * b


class Boozer:

    def __init__(self, name="Ivan", liters=99) -> None:
        self.name = name
        self.liters = liters

    name: str
    liters: int

    def get_liters(self):
        return self.liters

    def get_name(self):
        return self.name

    def booze(self):
        print("Noice! Feels good now")


boozer_object = Boozer()