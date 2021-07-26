""" Global Variables"""

#Game board
board=["_","_","_",
        "_","_","_",
        "_","_","_"]
#if game is still going
game_still_going=True

#who won or tie??
winner=None

#whos turn is it
current_player="X"
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
#play an game of tic tac toe
def play_game():
    
    #Display intial board
 display_board()

 #while the game is still going
 while game_still_going:

    #handle a single turn of an arbitrary player
     handle_turn(current_player)

    #check if game is has ended
     check_if_game_over()

    #flip to the other player
     flip_player()

     #The game has ended
 if winner=="X"or winner=="O":
        print(winner+" won.")
 elif winner==None:
        print("Tie.")

#handle a single turn of an arbitrary player
def handle_turn(player):

 print(player+" 's turn.")
 position=input("choose a position from 1-9: ")
 valid=False
 while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
         position=input("Invalid input. choose a position again from 1-9: ")

    position=int(position)-1

    if board[position] =="_":
      valid=True
    else:
      print("You cant't go there.Go again.")
 board[position]=player



 display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    #set up gloabal variables
    global winner
    # check rows
    row_winner=check_rows()
    # check columns
    column_winner=check_columns()
    # check diagnols
    diagnol_winner=check_diagnols()
    if row_winner:
        #there was a win
        winner=row_winner
    elif column_winner:
        # there was a win
        winner=column_winner
    elif diagnol_winner:
        #there was a win
        winner=diagnol_winner
    else:
        #there was no win
        winner = None
    return

def check_rows():
    # set the global variables
    global game_still_going
    row_1=board[0]==board[1]==board[2] !="_"
    row_2=board[3]==board[4]==board[5] !="_"
    row_3=board[6]==board[7]==board[8] !="_"
#if any row does have a match,flag that there is a  win
    if row_1 or row_2 or row_3:
        game_still_going=False
   #return the winner (X or O)
    if row_1:
      return  board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():

    # set the global variables
    global game_still_going
    column_1=board[0]==board[3]==board[6] !="_"
    column_2=board[1]==board[4]==board[7] !="_"
    column_3=board[2]==board[5]==board[8] !="_"
#if any column does have a match,flag that there is a  win
    if column_1 or column_2 or column_3:
        game_still_going=False
    #return the winner (X or O)
    if column_1:
      return  board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagnols():
    
    # set the global variables
    global game_still_going
    diagnol_1=board[0]==board[4]==board[8] !="_"
    diagnol_2=board[6]==board[4]==board[2] !="_"
#if any diagnol does have a match,flag that there is a  win
    if diagnol_1 or diagnol_2 :
        game_still_going=False
    #return the winner (X or O)
    if diagnol_1:
      return  board[0]
    elif diagnol_2:
        return board[1]
    return
    

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going=False
    return

def flip_player():
    #global variables we need
    global current_player
    #if current player is X then change into O
    if current_player=="X":
        current_player="O"
    #if the current player is O then change into X
    elif current_player=="O":
        current_player="X"
    return


play_game()

