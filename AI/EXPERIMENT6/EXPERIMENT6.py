import math

# Symbols definition
HUMAN = 'X'   # Minimizing player (utility: -1)
AI = 'O'      # Maximizing player (utility: +1)
EMPTY = ' '

def print_board(board):
    """Prints the 3x3 game board with cell numbers or markings."""
    print("\n")
    for r in range(3):
        row = [board[r * 3 + c] if board[r * 3 + c] != EMPTY else str(r * 3 + c + 1) for c in range(3)]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if r < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    """
    Evaluates terminal states.
    Returns: 'O' if AI wins, 'X' if Human wins, 'Draw' if tied, or None if game continues.
    """
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for line in win_combinations:
        if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != EMPTY:
            return board[line[0]]
    if EMPTY not in board:
        return 'Draw'
    return None

def minimax(board, depth, is_maximizing):
    """
    Minimax recursive search algorithm.
    Maximizes utility for AI ('O') and minimizes for Human ('X').
    """
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    """Finds the optimal move for the AI agent using minimax."""
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    # Initial state: 9 empty spaces
    board = [EMPTY] * 9

    print("=======================================")
    print("     TIC-TAC-TOE USING MINIMAX AI     ")
    print("=======================================")
    print("You are Player X (Minimizer). AI is Player O (Maximizer).")
    print("Positions are numbered 1 through 9.")
    print_board(board)

    while True:
        # Human Player Turn
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid choice! Enter an integer between 1 and 9.")
                    continue
                if board[move] != EMPTY:
                    print("Cell already occupied. Choose an empty cell.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        board[move] = HUMAN
        print("\n--- Board after your move ---")
        print_board(board)

        # Check terminal state after human move
        status = check_winner(board)
        if status == HUMAN:
            print("Congratulations! You won!")
            break
        elif status == 'Draw':
            print("The game ended in a Draw!")
            break

        # AI Player Turn
        print("AI is calculating optimal move...")
        ai_move = find_best_move(board)
        board[ai_move] = AI
        print(f"AI chooses cell {ai_move + 1}:")
        print_board(board)

        # Check terminal state after AI move
        status = check_winner(board)
        if status == AI:
            print("AI wins! The Minimax agent made the optimal moves.")
            break
        elif status == 'Draw':
            print("The game ended in a Draw!")
            break

if __name__ == "__main__":
    play_game()