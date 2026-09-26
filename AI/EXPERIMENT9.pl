% ===================================================================
% Experiment 9: N-Queens Problem using Prolog and Backtracking
% ===================================================================

% -------------------------------------------------------------------
% Predicate: n_queens(N, Solution)
% Solves the N-Queens problem on an N x N chessboard.
% Solution is represented as a list of column positions [Q1, Q2, ..., QN]
% where Qi represents the column index of the queen in row i.
% -------------------------------------------------------------------
n_queens(N, Solution) :-
    numlist(1, N, Domain),       % Domain = [1, 2, ..., N]
    permutation(Domain, Solution),% Enforces: No two queens share the same row/column
    safe(Solution).              % Enforces: No two queens attack along diagonals

% -------------------------------------------------------------------
% Predicate: safe(List)
% Base Case: An empty board or single queen is trivially safe.
% -------------------------------------------------------------------
safe([]).
% Recursive Step: Head queen must not attack any remaining queens in Tail.
safe([Queen | Others]) :-
    safe(Others),
    no_attack(Queen, Others, 1).

% -------------------------------------------------------------------
% Predicate: no_attack(Queen, Others, Distance)
% Verifies that Queen does not diagonally attack any queen in Others.
% Distance represents vertical row separation between queens.
% -------------------------------------------------------------------
no_attack(_, [], _).
no_attack(Queen, [OtherQueen | Rest], Distance) :-
    % Check positive and negative diagonal constraints:
    % |Queen - OtherQueen| \= Distance
    OtherQueen - Queen =\= Distance,
    Queen - OtherQueen =\= Distance,
    NewDistance is Distance + 1,
    no_attack(Queen, Rest, NewDistance).

% -------------------------------------------------------------------
% Helper Predicate: print_board(Solution)
% Displays the board cleanly in text format
% -------------------------------------------------------------------
print_board([]).
print_board([Col | Rest]) :-
    print_row(Col, 1),
    nl,
    print_board(Rest).

print_row(Col, Col) :-
    write(' Q '), !.
print_row(Col, Current) :-
    Current =\= Col,
    write(' . '),
    Next is Current + 1,
    print_row(Col, Next).

% Wrapper to run and print solution
solve(N) :-
    n_queens(N, Solution),
    write('Solution representation (Column per Row): '),
    write(Solution), nl, nl,
    print_board(Solution),
    nl.