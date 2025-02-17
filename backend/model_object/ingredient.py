
# 食材对象，包括食材和调味品
class Ingredient():
    """
    调味品类，用于表示一种调味品的属性，包括名称、味道和价格。

    核心功能：
    - 初始化调味品对象，设置其名称、味道和价格。
    - 返回调味品的字符串表示形式。

    参数：
    - name (str): 调味品的名称。
    - flavor (str): 调味品的味道。
    - price (float): 调味品的价格。

    使用示例：
    >>> ingredient = Ingredient("盐", "咸", 1.5)
    >>> print(ingredient)
    调味品名称: 盐, 味道: 咸, 价格: 1.5元
    """

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price

    def __str__(self):
        return f"调味品名称: {self.name}, 味道: {self.flavor}, 价格: {self.price}元"
