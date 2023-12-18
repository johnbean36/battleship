#Battleship console game by John Bass

import os
import library

top = 0
left = 0
library.welcome()
start = []
stop = []
main_loop = True
error = False

print("by John Bass\n\n")
print("At any time type quit to exit the game")
board = library.board()
for num in range(13):
    print(board[num])
while(main_loop):
    print("Enter coordines for Carrier ex B4 and F4")
    print("Carriers are 5 slots:")
    while(True):
        try:
            carrier = input()
            if carrier.lower() == "quit":
                main_loop = False
                break
            top, left, error = library.convert_coordinates(carrier)
            if error == True:
                raise ValueError('Coordinate invalid')
            break
        except Exception as e:
            print(e)

