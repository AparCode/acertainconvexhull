# The Main File
# @Author: Aparnaa Senthilnathan, Evan Prizel
# ------------------------------------------------------------------------------------------

import turtle


def click(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(5)
    turtle.penup()

turtle.ht()
turtle.onscreenclick(click,1)
turtle.listen()
turtle.speed(50)
turtle.done()