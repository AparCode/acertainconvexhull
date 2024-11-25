# The Main File
# @Author: Aparnaa Senthilnathan, Evan Prizel
# ------------------------------------------------------------------------------------------

import sys
import matrix as m 
from pyweb import pydom

class Board:
    def __init__(self):
        self.board = pydom["table#board"]
        self.status = pydom["h2#status"]
        self.console = pydom["script#console"][0]
        
    def set_status(self, text):
        self.status.html = text
    
    def add_point(self, event):
        x = int(event.target.getAttribute('data-x'))
        y = int(event.target.getAttribute('data-y'))
        
        print(x)
        print(y)
        
    def reset(self, event):
        self.console._js.terminal.clear()
        

start = Board()
        
# import keyboard

# if len(sys.argv) == 1:
#     points = []
#     while True:
#         if keyboard.read_key() == "x":
#             break
#         else:
#             x = input("Please enter a x-coord:")
#             y = input("Please enter a y-coord:")
#             coord = (x,y)
#             points.append(coord)
            
#             points = matrix_operation(coord, )
