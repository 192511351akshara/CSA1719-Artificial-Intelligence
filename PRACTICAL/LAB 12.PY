# Tic-Tac-Toe using CSP

board = [' '] * 9

# Winning combinations
winning_positions = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])


def check_winner(player):
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_safe(position):
    return board[position] == ' '


# Main game
print("TIC-TAC-TOE")
print("Positions are 1 to 9")

for turn in range(9):

    print_board()

    player = 'X' if turn % 2 == 0 else 'O'

    position = int(input("Player " + player + ", enter position: ")) - 1

    if is_safe(position):
        board[position] = player

        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            break
    else:
        print("Position already occupied!")
        continue

else:
    print_board()
    print("It's a Draw!")
