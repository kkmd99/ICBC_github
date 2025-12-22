from main import Fruit, Cart, StrawberryDiscount, Full100Minus10

# 測試案例 1：蘋果1斤、草莓1斤(打8折)、芒果10斤
apple = Fruit("apple", 8)
strawberry = Fruit("strawberry", 13)
mango = Fruit("mango", 20)
strawberry = StrawberryDiscount().apply(strawberry) #打8折

cart = Cart()
cart.add(apple, 1)
cart.add(strawberry, 1)
cart.add(mango, 10)

total = cart.total()
#total = Full100Minus10().apply(total) #滿100減10

assert total == 8 + 10.4 + 200, f"期望 218.4，實際 {total}"
print(f"測試1: 期望218.4，實際 {total}")

# 測試案例 2：蘋果6斤、草莓3斤(打8折)、芒果2斤 + 滿100減10
apple = Fruit("apple", 8)
strawberry = Fruit("strawberry", 13)
mango = Fruit("mango", 20)
strawberry = StrawberryDiscount().apply(strawberry) #打8折

cart = Cart()
cart.add(apple, 6)
cart.add(strawberry, 3)
cart.add(mango, 2)

total = cart.total()
total = Full100Minus10().apply(total) #滿100減10

assert total == (6*8 + 3*10.4 + 2*20) - 10, f"期望 109.2，實際 {total}"
print(f"測試2: 期望109.2，實際 {total}")
print("所有測試通過 ✔")
