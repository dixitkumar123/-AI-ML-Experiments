import copy

# Target Goal State configuration ('_' represents the empty space)
GOAL_STATE = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '_']
]

def print_board(state):
    """Displays the 3x3 board cleanly."""
    for row in state:
        print("  ".join(row))
    print()

def find_blank(state):
    """Locates the coordinates (row, col) of the blank tile '_'."""
    for r in range(3):
        for c in range(3):
            if state[r][c] == '_':
                return r, c
    return None

def calculate_heuristic(state):
    """
    Heuristic Function h(n): Misplaced Tiles Heuristic.
    Counts the number of numbered tiles not in their goal position.
    The blank tile '_' is excluded from the count.
    """
    misplaced = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != '_' and state[r][c] != GOAL_STATE[r][c]:
                misplaced += 1
    return misplaced

def get_successors(state):
    """Generates all valid neighboring board configurations."""
    successors = []
    blank_r, blank_c = find_blank(state)

    # Valid blank tile moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_r, new_c = blank_r + dr, blank_c + dc
        # Ensure target tile coordinates remain within the 3x3 grid
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = copy.deepcopy(state)
            # Swap blank space with adjacent tile
            new_state[blank_r][blank_c], new_state[new_r][new_c] = (
                new_state[new_r][new_c],
                new_state[blank_r][blank_c],
            )
            successors.append(new_state)
    return successors

def hill_climbing(initial_state):
    """
    Implements Steepest-Ascent Hill Climbing search based on h(n).
    Transitions to the neighbor with the lowest heuristic value.
    """
    current_state = initial_state
    current_h = calculate_heuristic(current_state)
    step = 0

    print("--- Initial State ---")
    print_board(current_state)
    print(f"Initial Heuristic Value h(n) = {current_h}\n")

    while True:
        if current_h == 0:
            print(f"Goal state reached successfully in {step} steps!")
            return

        neighbors = get_successors(current_state)
        best_neighbor = None
        best_h = current_h

        # Evaluate all generated neighbors to find the steepest improvement
        for neighbor in neighbors:
            h_val = calculate_heuristic(neighbor)
            if h_val < best_h:
                best_h = h_val
                best_neighbor = neighbor

        # If no strictly better neighbor is found, we hit a local maximum or plateau
        if best_neighbor is None or best_h >= current_h:
            print("Search stopped: Stuck at a Local Optimum or Plateau.")
            print(f"Final state reached with h(n) = {current_h}:")
            print_board(current_state)
            return

        # Move to the best neighbor
        current_state = best_neighbor
        current_h = best_h
        step += 1

        print(f"--- Step {step} ---")
        print_board(current_state)
        print(f"Heuristic Value h(n) = {current_h}\n")

if __name__ == "__main__":
    # Example solvable board configuration
    initial_board = [
        ['1', '2', '3'],
        ['4', '_', '6'],
        ['7', '5', '8']
    ]
    hill_climbing(initial_board)