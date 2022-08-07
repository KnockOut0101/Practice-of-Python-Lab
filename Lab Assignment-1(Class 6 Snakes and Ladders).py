import random

no_of_players = int(input("Enter no. of Players:-"))
number = []

def Generate():
    return random.randint(1,99) 

snakes={}
player_positions = []
turn = []

def snakes_generator(Snakes_dict):
    for i in range(10):
        number.append(Generate())
    



for i in range(1,no_of_players+1):
    player_positions.append(0)
    turn.append(i)

print(player_positions)

def print_board(list_input,start,end):
    for i in range(start,end+1):
        print(list_input[i], end='\t')


def dice():
    return random.randint(1,6)

def game_board(positions_list,turn_list,player_turn):
    units=list(range(1,101))

    '''print(turn_list[player_turn])
    dice_value = dice()
    

    postion = positions_list[turn_list[player_turn]] + dice()
    '''
    

    print_board(units,0,9)
    print("\n--------------------------------------------------------------------------------")
    print_board(units,10,19)



game_board(player_positions,turn,1)