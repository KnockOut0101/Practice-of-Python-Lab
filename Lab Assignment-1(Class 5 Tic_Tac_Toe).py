Tic_Tac_Toe=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def Add_O(index,gamelist):
    gamelist[index] = 'O'

def Add_X(index,gamelist):
    gamelist[index] = 'X'

def Print_Game(gamelist):
    print("%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n"%(gamelist[0],gamelist[1],gamelist[2],gamelist[3],gamelist[4],gamelist[5],gamelist[6],gamelist[7],gamelist[8]))

def Check_Status(gamelist):
    if(gamelist[0]==gamelist[1]==gamelist[2]=='O' or gamelist[0]==gamelist[1]==gamelist[2]=='X'):
        print("Game Won")
        return True
    elif(gamelist[0]==gamelist[3]==gamelist[6]=='O' or gamelist[0]==gamelist[3]==gamelist[6]=='X'):
        print("Game Won")
        return True
    elif(gamelist[0]==gamelist[4]==gamelist[8]=='O' or gamelist[0]==gamelist[4]==gamelist[8]=='X'):
        print("Game Won")
        return True
    elif(gamelist[1]==gamelist[4]==gamelist[7]=='O' or gamelist[1]==gamelist[4]==gamelist[7]=='X'):
        print("Game Won")
        return True
    elif(gamelist[2]==gamelist[5]==gamelist[8]=='O' or gamelist[2]==gamelist[5]==gamelist[8]=='X'):
        print("Game Won")
        return True
    elif(gamelist[2]==gamelist[4]==gamelist[6]=='O' or gamelist[2]==gamelist[4]==gamelist[6]=='X'):
        print("Game Won")
        return True
    elif(gamelist[3]==gamelist[4]==gamelist[5]=='O' or gamelist[3]==gamelist[4]==gamelist[5]=='X'):
        print("Game Won")
        return True
    elif(gamelist[6]==gamelist[7]==gamelist[8]=='O' or gamelist[6]==gamelist[7]==gamelist[8]=='X'):
        print("Game Won")
        return True
        


def Start_Game(gamelist):
    while(True):
        P1 = int(input("Enter a Postion (Player 1):-"))
        Add_O(P1,Tic_Tac_Toe)
        Print_Game(Tic_Tac_Toe)
        status=Check_Status(Tic_Tac_Toe)
        if (status==True):
            break
        P2 = int(input("Enter a Postion (Player 2):-"))
        Add_X(P2,Tic_Tac_Toe)
        Print_Game(Tic_Tac_Toe)
        status=Check_Status(Tic_Tac_Toe)
        if (status==True):
            break



Start_Game(Tic_Tac_Toe)