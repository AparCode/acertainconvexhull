# Input Files Generator
# @author: Aparnaa Senthilnathan, Evan Prizel
# FOR TESTING
# Takes two arguments, the output file name and size of the points
# ------------------------------------------------------------------------------------------

import sys
import random

# Generates a list of points and writes them to a file
# Graph Range -> (-1 <= x <= 16, -2 <= y <= 5)
# Format:
# n
# x1 y1
# x2 y2
# ...
# xn yn
def generatePoints(file_name, input_size):
    P = []
    with open(file_name, "w") as f:
        f.write(str(input_size) + '\n')
        for i in range(input_size):
            x = random.uniform(-1, 16)
            y = random.uniform(-2, 5)
            p = (x,y)
            if p not in P:
                P.append(p)
            else:
                i -= 1
        for p in P:
            f.write(str(p[0]) + " " + str(p[1]) + "\n")
        f.close()

# Ask the user for input on what the matrix should be
# and append the matrix to the file
# Format:
# Input Matrix:
# m[0,0]: (user input)
# m[0,1]: (user input)
# m[0,2]: (user input)
# m[1,0]: (user input)
# m[1,1]: (user input)
# m[1,2]: (user input)
# The third row is always 0 0 1
def generateMatrix(file_name):
    m = [] * 3
    with open(file_name, "a") as f:
        print("Input Matrix:")
        print("[   ] [   ] [   ]\n")
        print("[   ] [   ] [   ]\n")
        print("[ 0 ] [ 0 ] [ 1 ]\n")
        for i in range(2):
            m1 = input(f"({i},0): ")
            m2 = input(f"({i},1): ")
            m3 = input(f"({i},2): ")
            f.write(m1 + " " + m2 + " " + m3 + "\n")
            m.append([int(m1), int(m2), int(m3)])
        f.write("0 0 1\n")
        m.append([0, 0, 1])
        f.close()
    return m

#graph_range -> (-1 <= x <= 16, -2 <= y <= 5)
filename = sys.argv[1]
input_size = int(sys.argv[2])
P = generatePoints(filename, input_size)
M = generateMatrix(filename)
