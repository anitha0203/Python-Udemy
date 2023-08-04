def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_win(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn.")

        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = (current_player + 1) % 2


if __name__ == "__main__":
    play_game()
