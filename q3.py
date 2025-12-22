class Fruit:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class Cart:
	def __init__(self):
		self.items = []

	def add(self, fruit, weight):
		if weight < 0 :
			raise ValueError("水果斤数需为大于等于 0 的整数")
		self.items.append((fruit, weight))

	def total(self):
		return sum(weight * fruit.price for fruit, weight in self.items)

class StrawberryDiscount:
	def apply(self, fruit):
		if fruit.name == "strawberry":
			fruit.price = fruit.price * 0.8
		return fruit

strawberrydiscount = 1
apple = Fruit("apple", 8)
strawberry = Fruit("strawberry", 13)
mango = Fruit("mango", 20)

if strawberrydiscount == 1:
	strawberry = StrawberryDiscount().apply(Fruit("strawberry", 13))

cart = Cart()
#cart.add(apple, 1)
cart.add(strawberry, 1)
#cart.add(mango, 1)
print(cart.total())
