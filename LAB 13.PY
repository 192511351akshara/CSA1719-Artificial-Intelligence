# Minimax Algorithm for Tic-Tac-Toe

board = [" "] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def winner(player):
    combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == player for i in c) for c in combinations)

def minimax(is_maximizing):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def best_move():
    best_score = -100
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Game
print("TIC-TAC-TOE")
print("You are X")
print("Computer is O")

while True:
    display()

    # User move
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move!")
        continue

    board[pos] = "X"

    if winner("X"):
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    # Computer move using Minimax
    move = best_move()
    board[move] = "O"

    if winner("O"):
        display()
        print("Computer Wins!")
        break
