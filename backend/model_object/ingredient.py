
# 食材对象，包括食材和调味品
class Ingredient():
    """
    食材对象，包括食材和调味品
    包含食材名称，需求数值，数值单位
    """
    def __init__(self, name, num, unit):
        self.name = name
        self.num = num
        self.unit = unit
