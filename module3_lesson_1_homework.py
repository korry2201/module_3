class Item:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        if isinstance(other, Item2):
            return self.number + other.number
    def __sub__(self ,other):
        if isinstance(other, Item2):
            return self.number - other.number
    def __mul__(self, other):
        if isinstance(other, Item2):
            return self.number * other.number
    def __truediv__(self, other):
        if isinstance(other, Item2):
            return self.number / other.number

class Item2:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        if isinstance(other, Item):
            return self.number + other.number
    def __sub__(self ,other):
        if isinstance(other, Item):
            return self.number - other.number
    def __mul__(self, other):
        if isinstance(other, Item):
            return self.number * other.number
    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.number / other.number

item1 = Item(5)
item2 = Item2(3)
print(item1 + item2)
print(item1 - item2)
print(item1 * item2)
print(item1 / item2)