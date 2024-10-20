# Jarvis's Algorithm Blueprint
# @author: Aparnaa Senthilnathan
# computes the convex hull using Jarvis's March implementation
# ------------------------------------------------------------------------------------------

import sys
import time

P = []
CH = []
num_of_points = 0


# Takes a file with a list of point and reads it into a list P
def read_points_from_file(input_file):
    P = []
    with open(sys.argv[1], "r") as f:
        num_of_points = int(f.readline())
        for c in f.readlines():
            idx = c.index(" ")
            x = c[:idx]
            y = c[(idx + 1):]
            y = y.strip("\n")
            P.append((float(x),float(y)))
    f.close()
    return P, num_of_points


# Uses the Jarvis's March algorithm to compute the convex hull
def jarvis_march(P, num_of_points):
    left_x = P[0][0]
    left_y = P[0][1]
    v1 = P[0] # v1 is the initial point
    for p in P:
        if p[0] < left_x:
            left_x = p[0]
            left_y = p[1]
            v1 = p
        elif p[0] == left_x:
            if p[1] > left_y:
                left_x = p[0]
                left_y = p[1]
                v1 = p

    hull_pt = 0 # checkpoint for if the path circulates back to the starting point
    p = v1
    q = v1
    while(hull_pt != 1):
        CH.append(p)
        p_idx = P.index(p)
        q_idx = (p_idx + 1) % num_of_points
        q = P[q_idx]

    # compute the orientation of the three points for each given point (r). if the result is less than 0 then this means
    # r is more counterclockwise than q and therefore it should replace q
        for r in P:
            ori = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            
            if ori < 0:
                q = r
        p = q
        if p == v1:
            if hull_pt == 0:
                hull_pt += 1
                break
    return CH

# writes the resulting convex hull into an output file (jm_out)
def write_hull_to_file(CH, out_file):
    with open(out_file, "w") as f:
        f.write(str(len(CH)) + '\n')
        for c in CH:
            x = c[0]
            y = c[1]
            if x % 1 == 0:
                x = int(x)
            if y % 1 == 0:
                y = int(y)
            f.write(str(x) + ' ' + str(y) + '\n')
    f.close()
    
# prints the convex hull to standard output
def print_convex_hull(CH, time_elapsed):
    print("Convex Hull:")
    print("Algorithm Used: Jarvis's March")
    print("Length: " + str(len(CH)))
    print("Points:")
    
    for c in CH:
        x = c[0]
        y = c[1]
        if x % 1 == 0:
            x = int(x)
        if y % 1 == 0:
            y = int(y)
        print(str(x) + ' ' + str(y))
        
    print("Time Elapsed: " + str(time_elapsed) + " seconds")

# main function; MUST take either of the two python files and one input file
if len(sys.argv) == 2:
    P, num_of_points = read_points_from_file(sys.argv[1])     
    timer = time.time() # starts the stopwatch
    CH = jarvis_march(P, num_of_points)
    timer_end = time.time() # ends the stopwatch
    time_elapsed = timer_end - timer
                    
    write_hull_to_file(CH, "jm_out.txt")
    print_convex_hull(CH, time_elapsed)
    
else:
    print("usage: python [brute_force.py/jarvis.py] [name of input file]")