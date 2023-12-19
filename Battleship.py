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
battleship_list = []
cruiser_list = []
submarine_list = []
destroyer_list = []

print("by John Bass\n\n")
print("At any time type quit to exit the game")
board = library.board()
for num in range(13):
    print(board[num])
while(main_loop):
    print("Enter first coordinate for Carrier ex. B4")
    print("Carriers are 5 slots:")
    carrier_list, main_loop = library.get_coordinates("Carrier", 5)
    print(carrier_list)
    print("Enter first coordinate for Battleship")
    print("Battleships are 4 slots:")
    battleship_list, main_loop = library.get_coordinates("Battleship", 4)
    print("Enter first coordinate for Cruiser")
    print("Cruisers are 3 slots:")
    destroyer_list, main_loop = library.get_coordinates("Cruiser", 3)
    print("Enter first coordinate for Submarine")
    print("Submarines are 3 slots:")
    submarine_list, main_loop = library.get_coordinates("Submarine", 3)
    print("Enter first coordinate for Destroyer")
    print("Destroyers are 2 slots")
    destroyer_list, main_loop = library.get_coordinates("Destroyer", 2)
