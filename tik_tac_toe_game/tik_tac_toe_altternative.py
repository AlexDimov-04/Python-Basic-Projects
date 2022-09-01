# import module
import random

# global variables for the game base
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None


# drawing the game board func
def draw_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# place input sign func
def player_input(board):
    input_data = int(input("Enter a number 1/9: "))
    if board[input_data - 1] == '-':
        board[input_data - 1] = currentPlayer
    else:
        print("Sorry! You can't place there!")


# check inputs horizontally func
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


# check inputs by rows func
def check_rows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[3]
        return True


# check inputs diagonally func
def check_diagonals(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[2]
        return True


# check if the game is a tie func
def check_tie(board):
    if '-' not in board:
        draw_board(board)
        print()
        print("The game is a TIE!")
        exit()


# check win func
def check_win(board):
    if check_horizontal(board):
        draw_board(board)
        print()
        print(f"The winner is {winner}!")
        exit()

    elif check_rows(board):
        draw_board(board)
        print()
        print(f"The winner is {winner}!")
        exit()

    elif check_diagonals(board):
        draw_board(board)
        print()
        print(f"The winner is {winner}!")
        exit()


# switch the player role
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# the computer chooses empty spot
def computer_turn(board):
    while currentPlayer == "O":
        position = random.randrange(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()


# gameplay
while True:
    draw_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    switch_player()
    computer_turn(board)
    check_win(board)
    check_tie(board)
