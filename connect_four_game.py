# import module
from collections import deque

players = deque([1, 2])
ROWS, COLS = 6, 7

board = [['0'] * COLS for row in range(ROWS)]


# check win for win state
def check_win(player_symbol, col):
    for line in board:
        if line.count(player_symbol) == 4:
            player_symbol_idx = line.index(player_symbol)
            if line[player_symbol_idx] == line[player_symbol_idx + 1] == line[player_symbol_idx + 2] == line[
                player_symbol_idx + 3]:  # check horizontal
                return True

    for row in range(ROWS // 2):
        if board[row][col - 1] == player_symbol and board[row + 1][col - 1] == player_symbol and board[row + 2][
            col - 1] == player_symbol and \
                board[row + 3][col - 1] == player_symbol:  # check vertical
            return True


# additional data
while True:
    current_player = players[0]
    try:
        player_move = int(input(f"Player {current_player}, please choose a column: "))
        if board[0][player_move - 1] != '0':
            print("\nNo free spots on that row!")
            print()
            continue

        if board[5][player_move - 1] == "0":
            board[5][player_move - 1] = str(current_player)
        else:
            for row in range(ROWS):
                if board[row][player_move - 1] != "0":
                    board[row - 1][player_move - 1] = str(current_player)
                    break

        for line in board:
            print([int(x) for x in line])
        print()

        players.append(players.popleft())

        if check_win(str(current_player), player_move):
            print(f"Player {current_player} connected four {current_player}-s and won the game!")
            break
    except ValueError:
        print("\nInvalid input!")
        print()
    except IndexError:
        print("\nIndex out of range!")
        print()
