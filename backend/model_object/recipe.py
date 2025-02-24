from cooking_time import CookingTime

# 食谱对象，每个菜谱的单个对象
class Recipe():
    # 从数据库里面读取数据对象，所以输入值是菜谱名称
    # name要进行模糊搜索，返回的是一个列表
    # only情况下只返回关联度最大的一个
    def __init__(self, name, only=True):
        # 菜谱数据库分为接受版本和爬虫爬下来的暂时版本
        self.cooking_time_list = None

        self.cooking_time_list = CookingTime(name, only)
        pass

    
    def calculate_food_preparation(self):
        pass