from pyfiglet import Figlet
import speech_recognition as sr

players = []
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]


def check_win():
    player_name, player_symbol = players[0]
    size = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])

    row_win = any([all(True if pos == player_symbol else False for pos in row) for row in board])
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"\n{player_name} won!")

        exit()

    players.append(players.pop(0))


def place_symbol(pos):
    row, col = (pos - 1) // 3, (pos - 1) % 3

    board[row][col] = players[0][1]

    check_win()

    print_board()
    choose_position()


def choose_position():
    while True:
        try:
            pos = int(input(f"{players[0][0]} choose a free position 1/9: "))
        except ValueError:
            print("\nInvalid position")
            continue

        if pos in range(len(board) * len(board) + 1):
            place_symbol(pos)
        else:
            print("\nInvalid position")


def print_board(begin=False):
    if begin:
        print("\nThis is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def game_start():
    figlet = Figlet(font='big')
    print(figlet.renderText('Tic-Tac-Toe'))

    with sr.Microphone() as source:
        r = sr.Recognizer()

        print("\nPlayer one, say your name: ")

        audio_data = r.record(source, duration=2)
        print("\nRecognizing...")
        player_one_name = r.recognize_google(audio_data)

        print("\nPlayer two, say your name: ")

        audio_data = r.record(source, duration=2)
        print("Recognizing...")
        player_two_name = r.recognize_google(audio_data)
        while True:
            player_1_sym = input(f"\n{player_one_name} would you like to play with 'X' or 'O'?: ").upper()

            if player_1_sym not in 'XO':
                print("\nPlease enter a valid symbol!")
            else:
                break

        player_2_sym = 'O' if player_1_sym == "X" else "X"

        players.append([player_one_name, player_1_sym])
        players.append([player_two_name, player_2_sym])

        print_board(begin=True)
        choose_position()


game_start()
