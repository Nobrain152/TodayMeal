# 单位的枚举类
# 实际使用需要用另一个主类进行数值转化，这边仅列下单位和数值的对应关系
from enum import Enum

class Unit(Enum):
    G = 1
    KG = 1000
    ML = 1
    L = 1000

    勺 = 10
    # 匙
    匙 = 3


    # 不可按重量计算单位
    个 = '个'
    瓣 = '瓣'


    # num是原单位的数字标记
    # 将一个单位转换为另一个单位
    def transform(self, num, unit_from, unit_to):
        new_unit = unit_from
        if type(unit_from.value) == type(0) and type(unit_to.value) == type(0):
            num = num * unit_from.value / unit_to.value
            new_unit = unit_to

        return num, new_unit