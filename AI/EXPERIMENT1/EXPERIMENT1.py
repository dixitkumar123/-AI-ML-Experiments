def print_board(board):
    """Displays the 3x3 game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """
    Checks if the given player ('X' or 'O') has won.
    All 8 possible winning combinations (rows, columns, diagonals).
    """
    win_conditions = [
        # Horizontal rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Vertical columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the board is completely filled without a winner."""
    return all(cell in ['X', 'O'] for cell in board)

def play_game():
    # Board representation: 1D list of length 9, initialized with cell positions 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'

    print("===================================")
    print("    WELCOME TO TIC-TAC-TOE GAME    ")
    print("===================================")
    print("Positions are numbered 1 through 9:")
    print_board(board)

    while True:
        # Move validation loop
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): "))

            # Boundary and vacancy validation
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[move - 1] in ['X', 'O']:
                print("Position already occupied! Choose an empty slot.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer from 1 to 9.")
            continue

        # Execute legal move
        board[move - 1] = current_player
        print_board(board)

        # Check goal states
        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        if check_draw(board):
            print("The game ends in a Draw!")
            break

        # Switch turns
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()