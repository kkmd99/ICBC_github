class Fruit:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class Cart:
	def __init__(self):
		self.items = []

	def add(self, fruit, weight):
		if weight < 0 :
			raise ValueError("水果斤數需為大於等於 0 的整數")
		self.items.append((fruit, weight))

	def total(self):
		return sum(weight * fruit.price for fruit, weight in self.items)

class StrawberryDiscount:
	def apply(self, fruit):
		if fruit.name == "strawberry":
			fruit.price = fruit.price * 0.8
		return fruit

class Full100Minus10:
	def apply(self, price):
		if price >= 100:
			price -= 10
		return price

# 控制折扣開關
strawberrydiscount = 1 #若strawberrydiscount為1則草莓限时打 8 折
full100minus10 = 1 #若full100minus10為1則购物满 100 减 10 块

apple = Fruit("apple", 8)
strawberry = Fruit("strawberry", 13)
mango = Fruit("mango", 20)

if strawberrydiscount == 1:
	strawberry = StrawberryDiscount().apply(strawberry)

cart = Cart()
cart.add(apple, 6)
cart.add(strawberry, 3)
cart.add(mango, 2)
totalmoney = cart.total()

if full100minus10 == 1:
	totalmoney = Full100Minus10().apply(totalmoney)

print(totalmoney)
