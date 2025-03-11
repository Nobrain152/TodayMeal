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

    def calculate_cooking_time(self):
        """
        计算烹饪时间

        该方法用于计算烹饪所需的时间。具体实现需要根据烹饪的食材和烹饪方式来确定。

        返回:
            int: 烹饪所需的时间（单位：分钟）
        """
        pass
    
    # 计算食材
    def calcuate_ingredients(self):
        pass
    

