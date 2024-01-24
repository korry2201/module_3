class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def __add__(self, other):                         #Магический метод __add__ - метод сложения
        if isinstance(other, Item):                   #Функция isinstance() - проверка к какому классу или типу данных принадлежит other
            return self.price + other.price           #other - условное обозначение другого экземпляра этого же класса
        elif isinstance(other, int):
            return self.price + other
        elif isinstance(other, float):
            return self.price + other

item1 = Item('Видеокамера', 15000, 3)
item2 = Item('Штатив', 8000, 2)
#total_price = item1 + item2
total_price = item1 + 1000
total_price_2 = item2 + 240,5
print(total_price, total_price_2)