# Matrix Operations Blueprint
# @Author: Aparnaa Senthilnathan, Evan Prizel
# Computes the Matrix Operations inputted by the user
# ------------------------------------------------------------------------------------------

import sys

# Takes a file with a list of point and reads it into a list P
# input format:
# n
# x1 y1
# x2 y2
# ...
# xn yn
# m[1,1] m[1,2] m[1,3]
# m[2,1] m[2,2] m[2,3]
# m[3,1] m[3,2] m[3,3]
def read_points_from_file(filename):
    points = []
    with open (filename, "r") as f:
        # Get the number of points in the dataset
        num_points = int(f.readline())
        i = 0
        matrix = []
        for line in f:
            if i >= num_points:
                # Store the matrix as a 2d list of integers
                if len(line.split()) != 3:
                    break
                m1, m2, m3 = line.split()
                matrix.append([float(m1), float(m2), float(m3)])
            else:
                # Store the points as a tuple
                x, y = line.split()
                points.append((float(x), float(y)))
            i += 1
    return points, num_points, matrix

# Takes a list of points and writes them to a file
# Cut off after 6 decimal places
# Format:
# x1 y1
# x2 y2
# ...
# xn yn
def write_points_to_file(filename, points):
    with open (filename, "w") as f:
        for point in points:
            f.write(f"{point[0]:.6f} {point[1]:.6f}\n")
    return True

# Takes a list of points and a matrix and returns a new list of points
# that is the result of the matrix operation on the input points
def matrix_operation(points, matrix):
    new_points = []
    for (x,y) in points:
        new_x = matrix[0][0]*x + matrix[0][1]*y + matrix[0][2]
        new_y = matrix[1][0]*x + matrix[1][1]*y + matrix[1][2]
        new_points.append((new_x, new_y))
    return new_points
        
# Main function
# Must be ran with the filename of the input file as its 
# first and only argument
if len(sys.argv) == 2:
    # Get the points from the file
    points, num_of_points, matrix = read_points_from_file(sys.argv[1])

    # Perform the matrix operation on the points
    new_points = matrix_operation(points, matrix)

    # Print the modified points to an output file
    write_points_to_file("output.txt", new_points)