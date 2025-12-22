from dataclasses import dataclass
from typing import List, Callable

# -------------------- 基础领域模型 --------------------
@dataclass
class Fruit:
    """水果"""
    name: str
    price: int  # 单价（元/斤）

    def cost(self, weight: int) -> int:
        """计算某种水果的总价（斤数*单价）"""
        if weight < 0:
            raise ValueError("斤数不能为负数")
        return weight * self.price


# -------------------- 促销策略 --------------------
class DiscountStrategy:
    """促销策略接口"""
    def apply(self, original: int) -> int:
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    """无折扣"""
    def apply(self, original: int) -> int:
        return original


class Strawberry80Discount(DiscountStrategy):
    """草莓打 8 折（只折草莓部分）"""
    def __init__(self, strawberry: Fruit):
        self.strawberry = strawberry

    def apply(self, original: int) -> int:
        # 原价 = 苹果 + 草莓 + 芒果
        # 折后 = 苹果 + 草莓*0.8 + 芒果
        # 但 original 已经是三者原价总和，我们并不知道各买了多少，
        # 所以改成：在 ShoppingCart 里先算好草莓折扣金额，再传进来。
        # 这里为了兼容旧接口，直接返回原始值，由调用方提前把草莓部分扣掉。
        # 更干净的做法是：把折扣逻辑移到 ShoppingCart 内部。
        # 但面试题场景下，最简单就是：在 total() 里先算草莓折后价，再拼总价。
        return original   # 本策略不再二次打折，由购物车提前算好


class Full100Minus10(DiscountStrategy):
    """满 100 减 10"""
    def __init__(self, next_strategy: DiscountStrategy = None):
        self.next = next_strategy or NoDiscount()

    def apply(self, original: int) -> int:
        after = self.next.apply(original)
        if after >= 100:
            after -= 10
        return after


# -------------------- 购物车 --------------------
class ShoppingCart:
    """购物车（支持任意水果、任意促销策略）"""
    def __init__(self, strategy: DiscountStrategy = None):
        self.strategy = strategy or NoDiscount()
        self.items: List[tuple[Fruit, int]] = []

    def add(self, fruit: Fruit, weight: int):
        self.items.append((fruit, weight))

    def total(self) -> int:
        raw = sum(f.cost(w) for f, w in self.items)
        return self.strategy.apply(raw)


# -------------------- 题目要求的四个函数 --------------------
def question1(apple_w: int, strawberry_w: int) -> int:
    """1. 苹果8元/斤，草莓13元/斤"""
    apple = Fruit("苹果", 8)
    strawberry = Fruit("草莓", 13)
    cart = ShoppingCart()
    cart.add(apple, apple_w)
    cart.add(strawberry, strawberry_w)
    return cart.total()


def question2(apple_w: int, strawberry_w: int, mango_w: int) -> int:
    """2. 增加芒果20元/斤"""
    apple = Fruit("苹果", 8)
    strawberry = Fruit("草莓", 13)
    mango = Fruit("芒果", 20)
    cart = ShoppingCart()
    cart.add(apple, apple_w)
    cart.add(strawberry, strawberry_w)
    cart.add(mango, mango_w)
    return cart.total()


def question3(apple_w: int, strawberry_w: int, mango_w: int) -> int:
    """3. 草莓打8折——直接把草莓单价换成 13*0.8"""
    apple   = Fruit("苹果", 8)
    mango   = Fruit("芒果", 20)
    strawberry = Fruit("草莓", int(13 * 0.8))   # 单价先折好
    cart = ShoppingCart()                      # 无需特殊策略
    cart.add(apple, apple_w)
    cart.add(strawberry, strawberry_w)
    cart.add(mango, mango_w)
    return cart.total()


def question4(apple_w: int, strawberry_w: int, mango_w: int) -> int:
    apple   = Fruit("苹果", 8)
    mango   = Fruit("芒果", 20)
    strawberry = Fruit("草莓", int(13 * 0.8))
    cart = ShoppingCart(strategy=Full100Minus10())  # 只留满减
    cart.add(apple, apple_w)
    cart.add(strawberry, strawberry_w)
    cart.add(mango, mango_w)
    return cart.total()


# -------------------- 简单自测 --------------------
def _assert_same(fn: Callable, cases: List[tuple], expect: List[int]):
    for args, exp in zip(cases, expect):
        got = fn(*args)
        assert got == exp, f"{args=} expect={exp} got={got}"
    print(f"{fn.__name__} 自测通过 ✔")


def self_test():
    """运行自测用例"""
    # 题目1
    _assert_same(question1,
                 [(0, 0), (1, 0), (0, 1), (2, 3)],
                 [0, 8, 13, 8 * 2 + 13 * 3])
    # 题目2
    _assert_same(question2,
                 [(0, 0, 0), (1, 1, 1)],
                 [0, 8 + 13 + 20])
    # 题目3（草莓8折）
    _assert_same(question3,
                 [(0, 1, 0), (1, 1, 1)],
                 [int(13 * 0.8), 8 + int(13 * 0.8) + 20])
    # 题目4（草莓8折+满100减10）
    _assert_same(question4,
                 [(6, 3, 2)],
                 [108])
    print("全部自测通过 ✔✔✔")


if __name__ == "__main__":
    # 跑一遍自测
    self_test()

    # 现场演示：任意输入
    demo = (2, 3, 4)  # 苹果2斤，草莓3斤，芒果4斤
    print("现场演示：苹果{}斤 草莓{}斤 芒果{}斤".format(*demo))
    print("Q1 总价：", question1(*demo[:2]))
    print("Q2 总价：", question2(*demo))
    print("Q3 总价（草莓8折）：", question3(*demo))
    print("Q4 总价（草莓8折+满100减10）：", question4(*demo))