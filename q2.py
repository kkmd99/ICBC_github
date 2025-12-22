class Fruit:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class Cart:
	def __init__(self):
		self.items = []

	def add(self, fruit, weight):
		self.items.append((fruit, weight))

	def total(self):
		return sum(weight * fruit.price for fruit, weight in self.items)

apple = Fruit("apple", 8)
strawberry = Fruit("strawberry", 13)
mango = Fruit("mango", 20)
cart = Cart()
cart.add(apple, 1)
cart.add(strawberry, 3)
cart.add(mango, 2)
print(cart.total())
