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
temp_str = ""
strtolst = []
ai_battleship_list = []
ai_carrier_list = []
ai_cruiser_list = []
ai_submarine_list = []
ai_destroyer_list = []

print("by John Bass\n\n")
print("At any time type quit to exit the game")
board = library.board()
attack_board = library.board()

for num in range(12):
    print(board[num])
while(main_loop):

    check = True
    print("Enter first coordinate for Carrier ex. B4")
    print("Carriers are 5 slots:")
    carrier_list, main_loop = library.get_coordinates("Carrier", 5)
    library.player_board(carrier_list, board, 5)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for num in range(12):
        print(board[num])
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
    library.player_board(battleship_list, board, 4)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for num in range(12):
        print(board[num])
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
    library.player_board(cruiser_list, board, 3)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for num in range(12):
        print(board[num])
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
    library.player_board(submarine_list, board, 3)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for num in range(12):
        print(board[num])
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
    library.player_board(destroyer_list, board, 2)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for num in range(12):
        print(board[num])

    ai_carrier_list = library.ai_get_coordinates(5)
    check = True
    while check:
        ai_battleship_list = library.ai_get_coordinates(4)
        for i in ai_battleship_list:
            if i in ai_carrier_list:
                ai_battleship_list.clear()
                continue
        check = False
    check = True
    while check:
        ai_cruiser_list = library.ai_get_coordinates(3)
        for i in ai_cruiser_list:
            if i in ai_carrier_list:
                ai_carrier_list.clear()
                continue
            elif i in ai_battleship_list:
                ai_battleship_list.clear()
                continue
        check = False
    check = True
    while check:
        ai_submarine_list = library.ai_get_coordinates(3)
        for i in ai_submarine_list:
            if i in ai_carrier_list:
                ai_submarine_list.clear()
                continue
            elif i in ai_battleship_list:
                ai_submarine_list.clear()
                continue
            elif i in ai_cruiser_list:
                ai_submarine_list.clear()
                continue
        check = False
    check = True
    while check:
        ai_destroyer_list = library.ai_get_coordinates(2)
        for i in ai_destroyer_list:
            if i in ai_carrier_list:
                ai_destroyer_list.clear()
                continue
            elif i in ai_battleship_list:
                ai_destroyer_list.clear()
                continue
            elif i in ai_cruiser_list:
                ai_destroyer_list.clear()
                continue
            elif i in ai_submarine_list:
                ai_destroyer_list.clear()
                continue
        check = False
    print(ai_carrier_list)
    print(ai_battleship_list)
    print(ai_cruiser_list)
    print(ai_submarine_list)
    print(ai_destroyer_list)
    
    print("Do you want to play another game(y/n)")
    while True:
        if input().upper() == 'N' or input().upper() == "NO":
            main_loop = False
            break
        elif input().upper() == 'Y' or input().upper() == "YES":
            break
