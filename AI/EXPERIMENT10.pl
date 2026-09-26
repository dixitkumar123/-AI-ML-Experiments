% ===================================================================
% Experiment 10: 8-Puzzle Problem using Prolog
% Environment: SWI-Prolog
% ===================================================================

% -------------------------------------------------------------------
% 1. Goal State Definition
% Board is represented as a 9-element flat list: [Row1, Row2, Row3]
% '0' denotes the blank/empty space (_).
% -------------------------------------------------------------------
goal_state([1, 2, 3,
            4, 5, 6,
            7, 8, 0]).

% -------------------------------------------------------------------
% 2. Legal Moves / State Transitions (move(CurrentState, NextState))
% Moves correspond to sliding the blank tile (0) Up, Down, Left, or Right.
% -------------------------------------------------------------------

% Move Blank UP (Swaps position with element 3 positions prior: distance = -3)
move([0, B, C, D, E, F, G, H, I], [D, B, C, 0, E, F, G, H, I]).
move([A, 0, C, D, E, F, G, H, I], [A, E, C, D, 0, F, G, H, I]).
move([A, B, 0, D, E, F, G, H, I], [A, B, F, D, E, 0, G, H, I]).
move([A, B, C, 0, E, F, G, H, I], [A, B, C, G, E, F, 0, H, I]).
move([A, B, C, D, 0, F, G, H, I], [A, B, C, D, H, F, G, 0, I]).
move([A, B, C, D, E, 0, G, H, I], [A, B, C, D, E, I, G, H, 0]).

% Move Blank DOWN (Swaps position with element 3 positions ahead: distance = +3)
move([D, B, C, 0, E, F, G, H, I], [0, B, C, D, E, F, G, H, I]).
move([A, E, C, D, 0, F, G, H, I], [A, 0, C, D, E, F, G, H, I]).
move([A, B, F, D, E, 0, G, H, I], [A, B, 0, D, E, F, G, H, I]).
move([A, B, C, G, E, F, 0, H, I], [A, B, C, 0, E, F, G, H, I]).
move([A, B, C, D, H, F, G, 0, I], [A, B, C, D, 0, F, G, H, I]).
move([A, B, C, D, E, I, G, H, 0], [A, B, C, D, E, 0, G, H, I]).

% Move Blank LEFT (Swaps position with left neighbor: row must not change)
move([B, 0, C, D, E, F, G, H, I], [0, B, C, D, E, F, G, H, I]).
move([A, C, 0, D, E, F, G, H, I], [A, 0, C, D, E, F, G, H, I]).
move([A, B, C, E, 0, F, G, H, I], [A, B, C, 0, E, F, G, H, I]).
move([A, B, C, D, F, 0, G, H, I], [A, B, C, D, 0, F, G, H, I]).
move([A, B, C, D, E, F, H, 0, I], [A, B, C, D, E, F, 0, H, I]).
move([A, B, C, D, E, F, G, I, 0], [A, B, C, D, E, F, G, 0, I]).

% Move Blank RIGHT (Swaps position with right neighbor: row must not change)
move([0, B, C, D, E, F, G, H, I], [B, 0, C, D, E, F, G, H, I]).
move([A, 0, C, D, E, F, G, H, I], [A, C, 0, D, E, F, G, H, I]).
move([A, B, C, 0, E, F, G, H, I], [A, B, C, E, 0, F, G, H, I]).
move([A, B, C, D, 0, F, G, H, I], [A, B, C, D, F, 0, G, H, I]).
move([A, B, C, D, E, F, 0, H, I], [A, B, C, D, E, F, H, 0, I]).
move([A, B, C, D, E, F, G, 0, I], [A, B, C, D, E, F, G, I, 0]).

% -------------------------------------------------------------------
% 3. Search Algorithm: Depth-Limited Search to prevent infinite loops
% solve_dfs(CurrentState, Path, Visited, DepthLimit)
% -------------------------------------------------------------------

% Base case: Current state matches the goal state
solve_dfs(State, [State], _, _) :-
    goal_state(State).

% Recursive step: Expand to valid unvisited neighbors within the depth limit
solve_dfs(State, [State | Path], Visited, Depth) :-
    Depth > 0,
    move(State, NextState),
    \+ member(NextState, Visited),
    NewDepth is Depth - 1,
    solve_dfs(NextState, Path, [NextState | Visited], NewDepth).

% -------------------------------------------------------------------
% 4. Board Display Helpers
% -------------------------------------------------------------------
print_board([A, B, C, D, E, F, G, H, I]) :-
    format(' ~w  ~w  ~w~n', [A, B, C]),
    format(' ~w  ~w  ~w~n', [D, E, F]),
    format(' ~w  ~w  ~w~n~n', [G, H, I]).

print_path([]).
print_path([State | Rest]) :-
    print_board(State),
    print_path(Rest).

% -------------------------------------------------------------------
% 5. Main Execution Predicate
% -------------------------------------------------------------------
solve_puzzle :-
    % Sample solvable initial state (2 moves away from goal)
    InitialState = [1, 2, 3,
                    4, 0, 6,
                    7, 5, 8],
    DepthLimit = 10,
    write('Searching for solution (Depth Limit = 10)...'), nl, nl,
    solve_dfs(InitialState, Path, [InitialState], DepthLimit),
    length(Path, Steps),
    NumMoves is Steps - 1,
    format('Solution found in ~w move(s)!~n~n', [NumMoves]),
    print_path(Path), !.