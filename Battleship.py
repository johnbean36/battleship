#Battleship console game by John Bass
import os
import library

#global variables
top = 0
left = 0
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
ai_ship_reference = []
attack_history = []
ai_attack_history = []
error1 = False
ai_attack = []

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
library.welcome()
print("by John Bass\n\n")
print("Instructions: Select coordinates in the format such as B4 for your ships to be placed on the player board, then select coordinate to guess where the computer's ships are.")
print("The coordinates you select will show up on the attack board as either a x or an o for a hit or a miss.  As the computer chooses coordinates that ")
print("hit your ships, your ships blocks will be replaced by an x.  When all your ships or the computers ships have been sunk the game will be over.\n")
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
    ship_count = 0
    display_text = ""
    display_game = ""
    display_hit = ""
    ai_hit = ""
    ai_display_text = ""
    ai_display_game = ""
    ai_hit_history = []
    board = library.board()
    attack_board = library.board()
    print("Player board\n")
    for num in range(12):
        print(board[num])
    carrier_list = library.get_coordinates("Carrier", 5)
    library.player_board(carrier_list, board, 5)
    print("Player board\n")
    for num in range(12):
        print(board[num])
    while check:
        battleship_list = library.get_coordinates("Battleship", 4)
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
    print("Player board\n")
    for num in range(12):
        print(board[num])
    check = True
    while check:
        cruiser_list = library.get_coordinates("Cruiser", 3)
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
    print("Player board\n")
    for num in range(12):
        print(board[num])
    check = True
    while check:
        submarine_list = library.get_coordinates("Submarine", 3)
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
    print("Player board\n")
    for num in range(12):
        print(board[num])
    check = True
    while check:
        destroyer_list = library.get_coordinates("Destroyer", 2)
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
    print("Attack Board")
    for num in range(12):
        print(attack_board[num])
    print("\n")
    print("Player Board")
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
    check = True
    while game:
        print("Enter a coordinate to attack: ")
        while check:
            error1 = False
            try:
                temp_list.clear()
                attack_coordinate = input().upper()
                top, left, error = library.convert_coordinates(attack_coordinate)
                temp_list.append(top)
                temp_list.append(left)
                if temp_list in attack_history:
                    print("You have already selected this coordinate, please try again")
                    error1 = True
                if error1 != True:
                    attack_history.append(temp_list.copy())
                if error == True:
                    raise ValueError('Coorindate invalid')
                if error1 != True:
                    break
            except Exception as e:
                print(e)
        hit, ship_reference = library.update_attack_board(attack_board, temp_list.copy(), ai_carrier_list, ai_battleship_list, ai_cruiser_list, ai_submarine_list, ai_destroyer_list)
        temp_list.clear()
        if hit == True:
            display_hit = "It was a hit!"
            if ship_reference is ai_carrier_list:
                ai_carrier_count += 1
                if ai_carrier_count == 5:
                    display_text = "You sank their Carrier!"
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        display_game = "You have won the game!"
                        game = False
            elif ship_reference is ai_battleship_list:
                ai_battleship_count += 1
                if ai_battleship_count == 4:
                    display_text = "You sank their Battleship!"
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        display_game = "You have won the game!"
                        game = False
            elif ship_reference is ai_cruiser_list:
                ai_cruiser_count += 1
                if ai_cruiser_count == 3:
                    display_text = "You sank their Cruiser!"
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        display_game = "You have won the game!"
                        game = False
            elif ship_reference is ai_submarine_list:
                ai_submarine_count += 1
                if ai_submarine_count == 3:
                    display_text = "You sank their Submarine!"
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        display_game = "You have won the game!"
                        game = False
            elif ship_reference is ai_destroyer_list:
                ai_destroyer_count += 1
                if ai_destroyer_count == 2:
                    display_text = "You sank their Destroyer!"
                    ai_ship_count += 1
                    if ai_ship_count == 5:
                        display_game = "You have won the game!"
                        game = False
        elif hit == False:
            display_hit = "It was a miss"
        #Computer guesses coordinates to attack
        check = True
        while check:
            ai_attack, ai_ship_reference = library.ai_guess_coordinate(carrier_list, battleship_list, cruiser_list, submarine_list, destroyer_list)
            if ai_attack not in ai_attack_history:
                ai_attack_history.append(ai_attack)
                check = False
        if ai_ship_reference is carrier_list:
            ai_hit = "Your Carrier has been hit!"
            carrier_count += 1
            library.update_player_board(ai_attack, board, True)
            if carrier_count == 5:
                ai_display_text = "Your Carrier has been sunk"
                ship_count += 1
                if ship_count == 5:
                    ai_display_game = "You have lost the game"
                    game = False
        elif ai_ship_reference is battleship_list:
            ai_hit = "Your Battleship has been hit!"
            battleship_count += 1
            library.update_player_board(ai_attack, board, True)
            if battleship_count == 4:
                ai_display_text = "Your Battleship has been sunk"
                ship_count += 1
                if ship_count == 5:
                    ai_display_game = "You have lost the game"
                    game = False
        elif ai_ship_reference is cruiser_list:
            ai_hit = "Your Cruiser has been hit!"
            cruiser_count += 1
            library.update_player_board(ai_attack, board, True)
            if cruiser_count == 3:
                ai_display_text = "Your Cruiser has been sunk"
                ship_count += 1
                if ship_count == 5:
                    ai_display_game = "You have lost the game"
                    game = False
        elif ai_ship_reference is submarine_list:
            ai_hit = "Your Submarine has been hit!"
            submarine_count += 1
            library.update_player_board(ai_attack, board, True)
            if submarine_count == 3:
                ai_display_text = "Your Submarine has been sunk"
                ship_count += 1
                if ship_count == 5:
                    ai_display_game = "You have lost the game"
                    game = False
        elif ai_ship_reference is destroyer_list:
            ai_hit = "Your Destroyer has been hit!"
            destroyer_count += 1
            library.update_player_board(ai_attack, board, True)
            if destroyer_count == 2:
                ai_display_text = "Your Destroyer has been sunk"
                ship_count += 1
                if ship_count == 5:
                    ai_display_game = "You have lost the game"
                    game = False
        else:
            library.update_player_board(ai_attack, board, False)
            
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            for i in range(12):
                print(attack_board[i])
            for i in range(12):
                print(board[i])
            if destroyer_count == 2:
                print("Your Destroyer has been sunk")
                ship_count += 1
                if ship_count == 5:
                    print("You have lost the game")
                    game = False
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("Attack Board")
        for i in range(12):
                print(attack_board[i])
        print("Player Board")
        for i in range(12):
            print(board[i])
        print(display_hit)
        if display_text != "":
            print(display_text)
        if display_game != "":
            print(display_game)
        if ai_hit != "":
            print(ai_hit)
        if ai_display_text != "":
            print(ai_display_text)
        if ai_display_game != "":
            print(ai_display_game)
        display_text = ""
        display_game = ""
        ai_hit = ""
        ai_display_text = ""
        ai_display_game = ""        
        check = True
        main_loop = False

