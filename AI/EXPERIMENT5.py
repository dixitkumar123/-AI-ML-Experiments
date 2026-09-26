import heapq

# Target Goal State configuration (0 represents the blank space)
GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Precomputed goal coordinates for each number (1-8) for fast Manhattan lookup
GOAL_POSITIONS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1)
}

def print_board(state):
    """Displays the 3x3 board cleanly."""
    for row in state:
        formatted_row = [str(num) if num != 0 else "_" for num in row]
        print("  ".join(formatted_row))
    print()

def find_blank(state):
    """Locates the coordinates (row, col) of the blank tile 0."""
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c
    return None

def calculate_manhattan_distance(state):
    """
    Heuristic Function h(n): Manhattan Distance.
    Calculates the sum of vertical and horizontal distances of tiles from their goal positions.
    Admissible and consistent heuristic for A*.
    """
    total_distance = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                goal_r, goal_c = GOAL_POSITIONS[val]
                total_distance += abs(r - goal_r) + abs(c - goal_c)
    return total_distance

def get_successors(state):
    """Generates all valid neighbor states by sliding tiles into the blank space."""
    successors = []
    blank_r, blank_c = find_blank(state)

    # Valid blank tile moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Convert tuple state to mutable nested list
    board_list = [list(row) for row in state]

    for dr, dc in moves:
        new_r, new_c = blank_r + dr, blank_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            # Swap
            board_list[blank_r][blank_c], board_list[new_r][new_c] = (
                board_list[new_r][new_c],
                board_list[blank_r][blank_c],
            )
            # Convert back to immutable tuple of tuples for set/hash checks
            successors.append(tuple(tuple(row) for row in board_list))
            # Backtrack swap
            board_list[blank_r][blank_c], board_list[new_r][new_c] = (
                board_list[new_r][new_c],
                board_list[blank_r][blank_c],
            )

    return successors

class Node:
    """Represents a node in the A* search tree."""
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g          # Cost to reach this node
        self.h = h          # Estimated cost to goal
        self.f = g + h      # Total estimated evaluation function

    def __lt__(self, other):
        # Tie-breaking for priority queue (min-heap) based on f(n)
        return self.f < other.f

def a_star(initial_state):
    """Solves the 8-puzzle problem using the A* Search Algorithm."""
    initial_h = calculate_manhattan_distance(initial_state)
    start_node = Node(state=initial_state, parent=None, g=0, h=initial_h)

    # Open List: Min-priority queue (stores Nodes ordered by f(n))
    open_heap = []
    heapq.heappush(open_heap, start_node)

    # Closed Set / Cost tracker: stores best g(n) achieved for a visited state
    visited_costs = {initial_state: 0}

    while open_heap:
        current_node = heapq.heappop(open_heap)

        # Goal Test
        if current_node.state == GOAL_STATE:
            # Backtrack to reconstruct the optimal path
            path = []
            curr = current_node
            while curr:
                path.append(curr)
                curr = curr.parent
            path.reverse()

            print("Goal state reached successfully via A* Search!\n")
            print(f"Optimal Path Length: {len(path) - 1} steps\n")
            for step, node in enumerate(path):
                print(f"--- Step {step} (g = {node.g}, h = {node.h}, f = {node.f}) ---")
                print_board(node.state)
            return

        # Expand neighboring nodes
        for neighbor_state in get_successors(current_node.state):
            tentative_g = current_node.g + 1
            if neighbor_state not in visited_costs or tentative_g < visited_costs[neighbor_state]:
                visited_costs[neighbor_state] = tentative_g
                h_val = calculate_manhattan_distance(neighbor_state)
                neighbor_node = Node(
                    state=neighbor_state,
                    parent=current_node,
                    g=tentative_g,
                    h=h_val
                )
                heapq.heappush(open_heap, neighbor_node)

    print("No solution exists for the given board configuration.")

if __name__ == "__main__":
    # Solvable initial board state (0 represents empty position)
    initial_board = (
        (1, 2, 3),
        (0, 4, 6),
        (7, 5, 8)
    )
    a_star(initial_board)