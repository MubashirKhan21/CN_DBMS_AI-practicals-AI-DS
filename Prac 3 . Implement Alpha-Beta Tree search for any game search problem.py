# Tic-Tac-Toe board represented as a 3x3 list
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals for a win or draw
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True
    return False

# Function to evaluate the board
def evaluate_board(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            return 1
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            return -1
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return 1
        if board[0][i] == board[1][i] == board[2][i] == 'O':
            return -1
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        return -1
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return -1
    return 0

# Alpha-Beta Pruning function for Tic-Tac-Toe
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if is_game_over(board) or depth == 0:
        return evaluate_board(board)

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = alpha_beta(board, depth - 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = alpha_beta(board, depth - 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move using Alpha-Beta Pruning
def find_best_move(board):
    best_eval = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = alpha_beta(board, 9, -float('inf'), float('inf'), False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main game loop
while not is_game_over(board):
    print_board(board)
    player_row, player_col = map(int, input("Enter your move (row and column): ").split())
    if board[player_row][player_col] != ' ':
        print("Invalid move. Try again.")
        continue
    board[player_row][player_col] = 'O'
    if is_game_over(board):
        break
    print("Computer is thinking...")
    computer_row, computer_col = find_best_move(board)
    board[computer_row][computer_col] = 'X'

print_board(board)
result = evaluate_board(board)
if result == 0:
    print("It's a draw!")
elif result == 1:
    print("You win!")
else:
    print("Computer wins!")
