# # 3. Types of Functions
# import turtle
# import colorsys
#
# t = turtle.Turtle()
# s = turtle.Screen().bgcolor("black")
# n = 70
# h = 0
#
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h , 1 , 0.8)
#     h += 1 / n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range(2):
#         t.left(2)
#         t.circle(100)
def greet(name):
    print(f"Hi,", name)

greet("Hammad")