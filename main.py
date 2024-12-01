# The Main File
# @Author: Aparnaa Senthilnathan, Evan Prizel
# ------------------------------------------------------------------------------------------

import turtle
import matrix as m 

points = []
new_points = []

# function that runs when the user inputs a point
def click(x,y):
    turtle.speed(100000000000000000000000000)
    points.append((float(x), float(y)))
    turtle.goto(points[0][0], points[0][1])
    turtle.clear()
    m.write_points_to_file("input.txt", points)
    # matrix = [float(1), float(0), float(0), float(0), float(1), float(0), float(0), float(0), float(0), float(1)]
    # m.matrix_operation(points, matrix)
    turtle.pendown()
    if len(points) > 1:
        for p in range(1,len(points)):
            turtle.dot(5)
            turtle.goto(int(points[p][0]), int(points[p][1]))
    turtle.dot(5)
    turtle.goto(int(points[0][0]), int(points[0][1]))

    # turtle.clear()
    # m.write_points_to_file("input.txt", points)
    # turtle.penup()
    # if len(points) != 1:
    #     turtle.pendown()
    # turtle.pendown()
    # turtle.dot(5)
    # turtle.penup()

turtle.ht()
turtle.onscreenclick(click,1)
turtle.listen()
turtle.speed(50)
turtle.done()