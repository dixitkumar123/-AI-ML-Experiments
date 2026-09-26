def dfs_water_jug(cap_a, cap_b, target):
    """
    Solves the Water Jug problem using Depth-First Search (DFS).
    cap_a: Capacity of Jug A
    cap_b: Capacity of Jug B
    target: Desired amount of water in either Jug A or Jug B
    """
    if target > max(cap_a, cap_b):
        print("Target cannot be larger than the capacities of the jugs.")
        return

    # Initial state: both jugs are empty (0, 0)
    initial_state = (0, 0)

    # Stack stores tuples: ((current_a, current_b), [path_of_steps])
    # Using a Python list as a LIFO (Last-In-First-Out) stack
    stack = [(initial_state, [initial_state])]

    # Set to record visited states to avoid infinite loops and cycles
    visited = set()

    print(f"Searching for a solution using DFS to get {target}L using jugs of {cap_a}L and {cap_b}L...\n")

    while stack:
        # LIFO operation: Pop the most recently added state
        (curr_a, curr_b), path = stack.pop()

        # Skip if already processed via an earlier deeper path
        if (curr_a, curr_b) in visited:
            continue
        visited.add((curr_a, curr_b))

        # Goal Test: check if either jug contains the target amount
        if curr_a == target or curr_b == target:
            print("Goal state reached successfully via DFS!")
            print(f"Total steps required: {len(path) - 1}\n")
            print("Step-by-step state transitions (Jug A, Jug B):")
            for step_no, state in enumerate(path):
                print(f"Step {step_no}: Jug A = {state[0]}L, Jug B = {state[1]}L")
            return

        # Generate all 6 legal successor states
        next_states = [
            (cap_a, curr_b),                             # 1. Fill Jug A
            (curr_a, cap_b),                             # 2. Fill Jug B
            (0, curr_b),                                 # 3. Empty Jug A
            (curr_a, 0),                                 # 4. Empty Jug B
            # 5. Pour Jug A -> Jug B until B is full or A is empty
            (curr_a - min(curr_a, cap_b - curr_b), curr_b + min(curr_a, cap_b - curr_b)),
            # 6. Pour Jug B -> Jug A until A is full or B is empty
            (curr_a + min(curr_b, cap_a - curr_a), curr_b - min(curr_b, cap_a - curr_a))
        ]

        # Push valid unvisited successors onto the stack
        for state in next_states:
            if state not in visited:
                stack.append((state, path + [state]))

    print("No solution exists for the given inputs.")

if __name__ == "__main__":
    # Standard problem parameters: Jug A = 4L, Jug B = 3L, Target = 2L
    jug_a_capacity = 4
    jug_b_capacity = 3
    target_amount = 2
    dfs_water_jug(jug_a_capacity, jug_b_capacity, target_amount)