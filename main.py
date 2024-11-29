# The Main File
# @Author: Aparnaa Senthilnathan, Evan Prizel
# ------------------------------------------------------------------------------------------

import turtle
import matrix as m 

points = []

def click(x,y):
    points.append((x,y))
    turtle.penup()
    if len(points) != 1:
        turtle.pendown()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(5)
    turtle.penup()



turtle.ht()
turtle.onscreenclick(click,1)
turtle.listen()
turtle.speed(50)
turtle.done()