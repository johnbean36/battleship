#Battleship console game by John Bass

import os
import library

top = 0
left = 0
library.welcome()
temp_list = []
main_loop = True
error = False
carrier_list = []
print("by John Bass\n\n")
print("At any time type quit to exit the game")
board = library.board()
for num in range(13):
    print(board[num])
while(main_loop):
    carrier_list, main_loop = library.carrier_coordinates()

