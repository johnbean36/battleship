#Battleship console game by John Bass
import os
import library

#global variables
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
attack_coordinate = ""
attack_board = []
board = []
game = True
hit = False
ship_reference = []

print("by John Bass\n\n")
board = library.board()
attack_board = library.board()
for num in range(12):
    print(board[num])
while(main_loop):
    #variables for counting number of times a ship has been hit
    
    carrier_count = 0
    battleship_count = 0
    cruiser_count = 0
    submarine_count = 0
    destroyer_count = 0
    ai_carrier_count = 0
    ai_battleship_count = 0
    ai_cruiser_count = 0
    ai_submarine_count = 0
    ai_destroyer_count = 0    
    check = True
    ai_ship_count = 0
    
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
        print(attack_board[num])
    print("\n")
    for num in range(12):
        print(board[num])
    ai_carrier_list = library.ai_get_coordinates(5)
    check = True
    while check:
        ai_battleship_list = library.ai_get_coordinates(4)
        for i in ai_battleship_list:
            if i in ai_carrier_list:
                ai_battleship_list.clear()
                break
        if ai_battleship_list != []:
            check = False
    check = True
    while check:
        ai_cruiser_list = library.ai_get_coordinates(3)
        for i in ai_cruiser_list:
            if i in ai_carrier_list:
                ai_carrier_list.clear()
                break
            elif i in ai_battleship_list:
                ai_cruiser_list.clear()
                break
        if ai_cruiser_list != []:
            check = False
    check = True
    while check:
        ai_submarine_list = library.ai_get_coordinates(3)
        for i in ai_submarine_list:
            if i in ai_carrier_list:
                ai_submarine_list.clear()
                break
            elif i in ai_battleship_list:
                ai_submarine_list.clear()
                break
            elif i in ai_cruiser_list:
                ai_submarine_list.clear()
                break
        if ai_submarine_list != []:
            check = False
    check = True
    while check:
        ai_destroyer_list = library.ai_get_coordinates(2)
        for i in ai_destroyer_list:
            if i in ai_carrier_list:
                ai_destroyer_list.clear()
                break
            elif i in ai_battleship_list:
                ai_destroyer_list.clear()
                break
            elif i in ai_cruiser_list:
                ai_destroyer_list.clear()
                break
            elif i in ai_submarine_list:
                ai_destroyer_list.clear()
                break
        if ai_destroyer_list != []:
            check = False
    while game:
        print("Enter a coordinate to attack: ")
        while True:
            try:
                attack_coordinate = input().upper()
                top, left, error = library.convert_coordinates(attack_coordinate)
                if error == True:
                    raise ValueError('Coorindate invalid')
                break
            except Exception as e:
                print(e)
        temp_list.append(top)
        temp_list.append(left)
        hit, ship_reference = library.update_attack_board(attack_board, temp_list.copy(), ai_carrier_list, ai_battleship_list, ai_cruiser_list, ai_submarine_list, ai_destroyer_list)
        temp_list.clear()
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        for i in range(12):
            print(attack_board[i])
        for i in range(12):
            print(board[i])
        if hit == True:
            print("It was a hit!")
            if ship_reference is ai_carrier_list:
                ai_carrier_count += 1
                if ai_carrier_count == 5:
                    print("You sank their Carrier!")
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        print("You have won the game!")
                        game = False
            elif ship_reference is ai_battleship_list:
                ai_battleship_count += 1
                if ai_battleship_count == 4:
                    print("You sank their Battleship!")
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        print("You have won the game!")
                        game = False
            elif ship_reference is ai_cruiser_list:
                ai_cruiser_count += 1
                if ai_cruiser_count == 3:
                    print("You sank their Cruiser!")
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        print("You have won the game!")
                        game = False
            elif ship_reference is ai_submarine_list:
                ai_submarine_count += 1
                if ai_submarine_count == 3:
                    print("You sank their Submarine!")
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        print("You have won the game!")
                        game = False
            elif ship_reference is ai_destroyer_list:
                ai_destroyer_count += 1
                if ai_destroyer_count == 2:
                    print("You sank their Destroyer!")
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        print("You have won the game!")
                        game = False
        elif hit == False:
            print("It was a miss")
    print("Do you want to play another game(y/n)")
    if input().upper() == 'N' or input().upper() == "NO":
        main_loop = False
    
