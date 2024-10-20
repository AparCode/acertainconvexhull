# Input Files Generator
# @author: Aparnaa Senthilnathan
# FOR TESTING
# Takes two arguments, the output file name and size of the points
# ------------------------------------------------------------------------------------------

import sys
import random

#graph_range -> (-1 <= x <= 16, -2 <= y <= 5)
file_name = sys.argv[1]
input_size = int(sys.argv[2])
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