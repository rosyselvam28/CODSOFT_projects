import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        if i < 6:
            print('-' * 5)

def check_winner(b, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(b[pos] == player for pos in combo) for combo in win_positions)

def is_draw(b):
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'

def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move!")
        except:
            print("Enter a valid number!")

def play_game():
    print("You are X, AI is O")
    print_board()

    while True:
        human_move()
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("Draw!")
            break

        print("AI's Turn...")
        ai_move()
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("Draw!")
            break

play_game()