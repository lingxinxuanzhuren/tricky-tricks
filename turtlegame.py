"""
Description:一个使用Python自带模块画图的模块
这个模块虚拟一只乌龟在窗口上爬行，以此来进行绘图

Version: 0.1
Author: 王平
Date: 2019-5-5
"""

import turtle #我开始将.py命名成turtle，结果报错--没有pensize属性，看来文件命名得注意

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
