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
        if coordinate == 'quit':
            error = False
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
        if coordinate == 'quit':
            error = False
            print('b')
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
    try:
        while(True):
            try:
                ship = input()
                ship = ship.upper()
                if ship == "QUIT":
                    return temp_list, False
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
        while(True):
            try:
                ship = input()
                ship = ship.upper()
                if ship == "QUIT":
                    return temp_list, False
                top, left, error = convert_coordinates(ship)
                if error == True:
                    raise ValueError('Coordinate Invalid')
                break
            except Exception as e:
                print(e)
        temp_list.append(top)
        temp_list.append(left)
        ship_list.append(temp_list.copy())
        temp_list.clear()
        if find_middle(ship_list, ship_size) == True:
            raise ValueError("Coordinates invalid please try again")
    except Exception as e:
        print(e)
    return ship_list, True

