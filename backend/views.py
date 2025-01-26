from django.shortcuts import render, HttpResponse

# 所有服务的初始化界面
def index(reques):
    return HttpResponse("欢迎使用")

# 不同服务需要分开，但是暂时先先放在一起
# 每周食谱生成界面
# 获得每周食谱配置界面信息
# 暂时先不需要开发，这个配合之后的用户相关信息配置，读取默认配置，但是现在先在界面上直接显示
# 输入：用户id
# 输出：用户相关信息
def initialization_recipe(reques):
    return HttpResponse("食谱初始化界面")

# post方法
# 生成每周食谱
# 核心方法
# 根据输入生成每周食谱
def generate_weekly_menu(reques):
    return HttpResponse("返回生成好的食谱对象")