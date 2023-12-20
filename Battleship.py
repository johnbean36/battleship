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
for num in range(12):
    print(board[num])
while(main_loop):
    check = True
    print("Enter first coordinate for Carrier ex. B4")
    print("Carriers are 5 slots:")
    carrier_list, main_loop = library.get_coordinates("Carrier", 5)
    while check:
        print("Enter first coordinate for Battleship")
        print("Battleships are 4 slots:")
        battleship_list, main_loop = library.get_coordinates("Battleship", 4)
        for i in battleship_list:
            if i in carrier_list:
                print("Coordinates overlap with Carrier coordinates, please try again")
                battleship_list.clear()
                break
        if battleship_list != []:
            check = False
    check = True
    while check:
        print("Enter first coordinate for Cruiser")
        print("Cruisers are 3 slots:")
        cruiser_list, main_loop = library.get_coordinates("Cruiser", 3)
        for i in cruiser_list:
            if i in battleship_list:
                print("Coordinates overlap with Battleship coordinates, please try again")
                cruiser_list.clear()
                break
            elif i in carrier_list:
                print("Coordinates overlap with Carrier coordinates, please try again")
                cruiser_list.clear()
                break
        if cruiser_list != []:
            check = False
    check = True
    while check:
        print("Enter first coordinate for Submarine")
        print("Submarines are 3 slots:")
        submarine_list, main_loop = library.get_coordinates("Submarine", 3)
        for i in submarine_list:
            if i in carrier_list:
                print("Coordinates overlap with Carrier coordinates, please try again")
                submarine_list.clear()
                break
            elif i in battleship_list:
                print("Coordinates overlap with Battleship coordinates, please try again")
                submarine_list.clear()
                break
            elif i in cruiser_list:
                print("Coordinates overlap with Cruiser coordinates, please try again")
                submarine_list.clear()
                break
        if submarine_list != []:
            check = False
    check = True
    while check:
        print("Enter first coordinate for Destroyer")
        print("Destroyers are 2 slots")
        destroyer_list, main_loop = library.get_coordinates("Destroyer", 2)
        for i in destroyer_list:
            if i in carrier_list:
                print("Coordinates_overlap with Carrier coordinates, please try again")
                destroyer_list.clear()
                break
            elif i in battleship_list:
                print("Coordinates overlap with Battleship coordinates, please try again")
                destroyer_list.clear()
                break
            elif i in cruiser_list:
                print("Coordinates overlap with Cruiser coordinates, please try again")
                destroyer_list.clear()
                break
            elif i in submarine_list:
                print("Coordinates overlap with Submrine coordinates, please try again")
                destroyer_list.clear()
                break
        if destroyer_list != []:
            check = False
    
    print("Do you want to play another game(y/n)")
    while True:
        if input().upper == 'N' or "NO":
            main_loop = False
            break
        elif input.upper == 'Y' or "YES":
            break
