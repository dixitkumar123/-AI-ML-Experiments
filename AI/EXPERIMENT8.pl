% ===================================================================
% Experiment 8: Tower of Hanoi Problem using Prolog
% ===================================================================

% -------------------------------------------------------------------
% Predicate: move(N, Source, Target, Auxiliary)
% Moves N disks from Source peg to Target peg using Auxiliary peg.
% -------------------------------------------------------------------

% Base Case: Moving a single disk (N = 1) directly from Source to Target
move(1, Source, Target, _) :-
    write('Move top disk from '),
    write(Source),
    write(' to '),
    write(Target),
    nl.

% Recursive Step: Moving N disks (where N > 1)
% 1. Move top (N-1) disks from Source to Auxiliary peg using Target peg.
% 2. Move the N-th (bottom-most) disk directly from Source to Target peg.
% 3. Move the (N-1) disks from Auxiliary to Target peg using Source peg.
move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(M, Auxiliary, Target, Source).

% -------------------------------------------------------------------
% Helper Predicate: hanoi(N)
% Wrapper to initiate puzzle execution with standard peg names:
% 'A' (Source), 'C' (Destination), and 'B' (Auxiliary).
% -------------------------------------------------------------------
hanoi(N) :-
    write('--- Solution for '), write(N), write(' Disks ---'), nl,
    move(N, 'A', 'C', 'B'),
    write('-----------------------------'), nl.