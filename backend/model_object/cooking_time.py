

# 烹饪时间
class CookingTime():
    """
    初始化时间对象

    参数:
    time_name (str): 时间名称
    time (str): 时间值
    """
    def __init__(self, time_name, time):
        self.time_name = time_name
        self.time = time

    def calculate_cooking_time(self):
        ...