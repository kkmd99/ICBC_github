class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, fruit, weight):
        if weight < 0:
            raise ValueError("水果斤數需為大於等於 0 的整數")
        self.items.append((fruit, weight))

    def total(self):
        return sum(weight * fruit.price for fruit, weight in self.items)

class StrawberryDiscount:
    def apply(self, fruit):
        if fruit.name == "strawberry":
            fruit.price = fruit.price * 0.8   # 保留小數
        return fruit

class Full100Minus10:
    def apply(self, price):
        if price >= 100:
            price = price - 10
        return price
