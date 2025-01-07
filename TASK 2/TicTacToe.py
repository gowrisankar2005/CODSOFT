# Tic-Tac-Toe with unbeatable AI
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for draw
    for row in board:
        if ' ' in row:
            return None
    return 'Draw'

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 10 - depth
    if winner == 'X':
        return depth - 10
    if winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and AI is O.")
    
    while True:
        print_board(board)
        if check_winner(board):
            result = check_winner(board)
            if result == 'Draw':
                print("It's a draw!")
            else:
                print(f"The winner is: {result}")
            break

        # Human move
        try:
            x, y = map(int, input("Enter your move (row and column, 0-2): ").split())
            if board[x][y] == ' ':
                board[x][y] = 'X'
            else:
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 0 and 2.")
            continue

        # AI move
        if not check_winner(board):
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'

play_game()
