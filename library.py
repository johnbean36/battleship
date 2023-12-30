import random

#Displays the welcome splash at the beginning of the game when called
def welcome():
    welcome_splash ="""\
     __          __  _                                         
     \ \        / / | |                                       
      \ \  /\  / /__| | ___ ___  _ __ ___   ___                
       \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \               
        \  /\  /  __/ | (_| (_) | | | | | |  __/               
      _  \/  \/ \___|_|\___\___/|_| |_| |_|\___| _     _       
     | |        |  _ \      | | | | | |         | |   (_)      
     | |_ ___   | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
     | __/ _ \  |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
     | || (_) | | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
      \__\___/  |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                                        | |    
                                                        |_| """
    print(welcome_splash)
#Assigns the ascii board to a list variable when called
def board():
    board_list = []
    board_list.append("    A   B   C   D   E   F   G   H   I   J\n")
    board_list.append("   _______________________________________\n")
    board_list.append("1 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("2 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("3 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("4 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("5 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("6 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("7 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("8 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("9 |   |   |   |   |   |   |   |   |   |   |\n")
    board_list.append("10|___|___|___|___|___|___|___|___|___|___|\n")
    
    return board_list

#converts coordinates such as A4 into coordinates that can coorispond to the
#indices for location in the ship lists
def convert_coordinates(coordinate):
    left = 0
    top = 0
    top_index = 0
    val = 0
    error = False
    try:
        val = int(coordinate[1])
    except Exception as e:
        #print(e)
        return 0, 0, True
    if len(coordinate) > 3 or (len(coordinate) == 3 and int(coordinate[1]) > 1) or (len(coordinate) == 3 and int(coordinate[2]) > 0):
        error = True
    if len(coordinate) > 2:
        try:
            val = int(coordinate[2])
        except:
            return 0, 0, True
        left = 10
    elif len(coordinate) == 2:
        left = int(coordinate[1])
    
    left = left - 1
    top = coordinate [0]
    top.upper()
    if top == 'A':
        top_index = 0
    elif top == 'B':
        top_index = 1
    elif top == 'C':
        top_index = 2
    elif top == 'D':
        top_index = 3
    elif top == 'E':
        top_index = 4
    elif top == 'F':
        top_index = 5
    elif top == 'G':
        top_index = 6
    elif top == 'H':
        top_index = 7
    elif top == 'I':
        top_index = 8
    elif top == 'J':
        top_index = 9
    else:
        error = True
    return top_index, left, error

#fill the coordinates in the carrier list between the starting and ending coordinates
#the user provided
def find_middle(ship_list, size):
    temp_list = []
    temp_swap = []
    if (ship_list[0][0] == ship_list[-1][0] or ship_list[0][1] == ship_list[-1][1]) and len(ship_list) == size:
        if ship_list[0][0] == ship_list[-1][0]:
            if size == 2:
                return False
            if ship_list[-1][1] > ship_list[0][1]:
                for i in range(1, size):
                    temp_list.append(ship_list[0][0])
                    temp_list.append(ship_list[0][1]+i)
                    ship_list[i] = temp_list.copy()
                    temp_list.clear()
            elif ship_list[size][1] < ship_list[0][1]:
                temp_list.append(ship_list[0][0])
                temp_list.append(ship_list[0][1])
                temp_swap.append(ship_list[-1][0])
                temp_swap.append(ship_list[-1][1])
                ship_list[0] = temp_swap.copy()
                temp_swap.clear()
                ship_list[-1] = temp_list.copy()
                temp_list.clear()
                for i in range(1, size):
                    temp_list.append(ship_list[0][0])
                    temp_list.append(ship_list[0][1]+i)
                    ship_list[i] = temp_list.copy()
                    temp_list.clear()
        elif ship_list[0][1] == ship_list[-1][1]:
            if size == 2:
                return False
            if ship_list[-1][0] > ship_list[0][0]:
                for i in range(1, size):
                    temp_list.append(ship_list[0][0]+i)
                    temp_list.append(ship_list[0][1])
                    ship_list[i] = temp_list.copy()
                    temp_list.clear()
            elif ship_list[-1][0] < ship_list[0][0]:
                temp_list.append(ship_list[0][0])
                temp_list.append(ship_list[0][1])
                temp_swap.append(ship_list[-1][0])
                temp_swap.append(ship_list[-1][1])
                ship_list[-1] = temp_list.copy()
                ship_list[0] = temp_swap.copy()
                for i in range(1, size):
                    temp_list.append(ship_list[0][0]+i)
                    temp_list.append(ship_list[0][1])
                    ship_list[i] = temp_list.copy()
                    temp_list.clear()
                    temp_swap.clear()   
    else:
        return True

#Asks the user for two coordinates that are the starting and ending coordinates
#of the ship, checks to make sure the coordinates are valid and returns the list
#mainloop
def get_coordinates(ship_name, ship_size):
    ship_list = []
    ship = ""
    temp_list = []
    top = 0
    left = 0
    error = False
    error2 = False
    while True:
        try:
            while(True):
                print("Enter first coordinate for " + ship_name)
                print(ship_name + "'s are " + str(ship_size) + " slots: ")
                try:
                    ship = input()
                    ship = ship.upper()
                    top, left, error = convert_coordinates(ship)
                    if error == True:
                        raise ValueError('Coordinate invalid')
                    break
                except Exception as e:
                    print(e)
            temp_list.append(top)
            temp_list.append(left)
            ship_list.append(temp_list.copy())
            temp_list.clear()
            if ship_size > 2:
                for i in range(0,ship_size-2):
                    temp_list.append('')
                    temp_list.append('')
                    ship_list.append(temp_list.copy())
                    temp_list.clear()
            print("Enter last coordinate for " + ship_name + ": ")
            while True:
                error = False
                ship = input()
                ship = ship.upper()
                top, left, error = convert_coordinates(ship)
                temp_list.append(top)
                temp_list.append(left)
                ship_list.append(temp_list.copy())
                if temp_list[0] == ship_list[0][0]:
                    if (temp_list[1] > (ship_list[0][1] + ship_size-1)) or (temp_list[1] < ship_list[0][1] + ship_size-1):
                        error = True
                        ship_list.pop(ship_size-1)        
                elif temp_list[1] == ship_list[0][1]:
                    if (temp_list[0] > ship_list[0][0] + ship_size-1) or (temp_list[0] < ship_list[0][0] + ship_size-1):
                        error = True
                        ship_list.pop(ship_size-1)
                temp_list.clear()
                if error:
                    print('Coordinate Invalid')
                if error == False:
                    break
            if error != True:
                if find_middle(ship_list, ship_size) == True:
                    raise ValueError("Coordinates invalid please try again")
        except Exception as e:
            print(e)
        if error != True:
            break
    return ship_list

def player_board(ship_list, board, size):
    ship_temp = []
    temp_str = ""
    strtolst = ""
    for i in range(0, size):
        ship_temp = ship_list[i]
        #print(ship_temp)
        temp_str = board[2+ship_temp[1]]
        strtolst = list(temp_str)
        strtolst[4+(ship_temp[0]*4)] = u"\u2588"
        temp_str = ''.join(strtolst)
        board[2+ship_temp[1]] = temp_str

#updates the players board when their ships get hit
def update_player_board(coordinate, board, hit):
    temp_str = ""
    strtolst = []
    if hit == True:
        temp_str = board[2+coordinate[1]]
        strtolst = list(temp_str)
        strtolst[4+(coordinate[0]*4)] = u"\u00D7"
        temp_str = ''.join(strtolst)
        board[2+coordinate[1]] = temp_str
    elif hit == False:
        temp_str = board[2+coordinate[1]]
        strtolst = list(temp_str)
        strtolst[4+(coordinate[0]*4)] = 'o'
        temp_str = ''.join(strtolst)
        board[2+coordinate[1]] = temp_str

#The computer selects the coordinates for it's ships
def ai_get_coordinates(size):
    ship_list = []
    ship = ""
    temp_list = []
    h_or_v = 0
    check = True
    
    while check:
        temp_list.append(random.randint(0,9))
        temp_list.append(random.randint(0,9))
        ship_list.append(temp_list.copy())
        temp_list.clear()
        h_or_v = random.randint(0,1)
        if h_or_v == 0:
            if ship_list[0][0] + size-1 > 9:
                ship_list.clear()
                continue
            else:
                if size > 2:
                    for i in range(0, size-2):
                        temp_list.append('')
                        temp_list.append('')
                        ship_list.append(temp_list.copy())
                        temp_list.clear()
                temp_list.append(ship_list[0][0] + size-1)
                temp_list.append(ship_list[0][1])
                ship_list.append(temp_list.copy())
                temp_list.clear()
            check = False
        elif h_or_v == 1:
            if ship_list[0][1] + size-1 > 9:
                ship_list.clear()
                continue
            else:
                if size > 2:
                    for i in range(0, size-2):
                        temp_list.append('')
                        temp_list.append('')
                        ship_list.append(temp_list.copy())
                        temp_list.clear()
                temp_list.append(ship_list[0][0])
                temp_list.append(ship_list[0][1] + size-1)
                ship_list.append(temp_list.copy())
                temp_list.clear()
            check = False
    find_middle(ship_list, size)
    return ship_list

#updates the attack board with the coordinates the user selected
def update_attack_board(attack_board, attack_coordinate, ship1, ship2, ship3, ship4, ship5):
    board_text = ""
    temp_list = []
    attack = False
    temp_str = ""
    ship_number = 0
    if attack_coordinate in ship1:
        attack = True
        ship_number = 1
    elif attack_coordinate in ship2:
        attack = True
        ship_number = 2
    elif attack_coordinate in ship3:
        attack = True
        ship_number = 3
    elif attack_coordinate in ship4:
        attack = True
        ship_number = 4
    elif attack_coordinate in ship5:
        attack = True
        ship_number = 5
    else:
        attack = False

    board_text = attack_board[attack_coordinate[1]+2]
    if attack == True:
        temp_list = list(board_text)
        temp_list[4+attack_coordinate[0]*4] = u"\u00D7"
        temp_str = ''.join(temp_list)
        attack_board[attack_coordinate[1]+2] = temp_str
        if ship_number == 1:
            return True, ship1
        elif ship_number == 2:
            return True, ship2
        elif ship_number == 3:
            return True, ship3
        elif ship_number == 4:
            return True, ship4
        elif ship_number == 5:
            return True, ship5
    elif attack == False:
        temp_list = list(board_text)
        temp_list[4+attack_coordinate[0]*4] = 'o'
        temp_str = ''.join(temp_list)
        attack_board[attack_coordinate[1]+2] = temp_str
        return False, temp_list
#The computer guesses coordinates to attack
def ai_guess_coordinate(ship1, ship2, ship3, ship4, ship5):
    top = 0
    left = 0
    temp_list = []
    
    top = random.randint(0, 9)
    left = random.randint(0, 9)
    temp_list.append(top)
    temp_list.append(left)

    if temp_list in ship1:
        return temp_list.copy(), ship1
    elif temp_list in ship2:
        return temp_list.copy(), ship2
    elif temp_list in ship3:
        return temp_list.copy(), ship3
    elif temp_list in ship4:
        return temp_list.copy(), ship4
    elif temp_list in ship5:
        return temp_list.copy(), ship5
    else:
        return temp_list.copy(), temp_list.copy()
