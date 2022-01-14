# Tic-Tac-Toe Assignment
# CSE 210
# Professor Kay
# Created by Daniel Wilkes

#Variables for game
game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ",]
player_Turn = "X"
game_Winner = None
runningGame = True

# Prints out Game Board
def main(game_board):
    print(game_board[0] + "|" + game_board[1] + "|" + game_board[2])
    print("-+-+-")
    print(game_board[3] + "|" + game_board[4] + "|" + game_board[5])
    print("-+-+-")
    print(game_board[6] + "|" + game_board[7] + "|" + game_board[8])

# Takes the player's Inputs and checks if chosen square has already been taken
def playersInputs(game_board):
    inp = int(input("Choose a square (1-9)"))
    if inp >= 1 and inp <= 9 and game_board[inp-1] == " ":
        game_board[inp-1] = player_Turn
    else:
        print("Sorry that square is taken")

#Checks to see if there is a winner for horizontal squares
def horizontalWin(game_board):
    global game_Winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != " ":
        game_Winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != " ":
        game_Winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != " ":
        game_Winner = game_board[6]
        return True

#Checks to see if there is a winner for vertical squares
def verticalWin(game_board):
    global game_Winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != " ":
        game_Winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != " ":
        game_Winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != " ":
        game_Winner = game_board[2]
        return True

#Checks to see if there is a winner for diagonal squares
def diagonalWin(game_board):
    global game_Winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != " ":
        game_Winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != " ":
        game_Winner = game_board[2]
        return True

#Checks previous functions to see if there is a winner
def winGame(game_board):
    global runningGame
    if diagonalWin(game_board) or verticalWin(game_board) or horizontalWin(game_board):
        print(f"Player {game_Winner} is the winner!!!")
        runningGame = False

#Checks to see if there is a tie
def tieGame(game_board):
    global runningGame
    if " " not in game_board:
        main(game_board)
        print("You both tied!!!")
        runningGame = False

#Switches between players
def switchPlayers():
    global player_Turn
    if player_Turn == "X":
        player_Turn = "O"
    else:
         player_Turn = "X"

#While game is running
while runningGame: 
    main(game_board)
    playersInputs(game_board)
    winGame(game_board)
    tieGame(game_board)
    switchPlayers()
    