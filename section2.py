import datetime


def area():
    x = float(input("请输入球的半径"))
    s = 4 * 3.14 * x * x
    v = 4 / 3 * 3.14 * x * x * x
    print("球的表面积为：", s)
    print("球的体积为：", v)


def birthday():
    name = input("请输入您的姓名：")
    y = int(input("请输入你的出生年份"))
    age = datetime.date.today().year - y
    print("您好{0}，您的年龄是：{1}".format( name,  age))

birthday()