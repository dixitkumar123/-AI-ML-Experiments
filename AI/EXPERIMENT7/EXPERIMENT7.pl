% ===================================================================
% Experiment 7: Family Tree Knowledge Base in Prolog
% ===================================================================

% -------------------------
% 1. Facts: Given genealogical tree
% father(Father, Child).
% -------------------------
father(a, b).
father(a, c).
father(b, d).
father(b, e).
father(c, f).

% -------------------------
% 2. Rules / Predicates
% -------------------------

% brother(X, Y): X and Y are brothers if they share the same father and are not identical.
brother(X, Y) :-
    father(F, X),
    father(F, Y),
    X \= Y.

% cousin(X, Y): X and Y are cousins if their fathers (F1 and F2) are brothers.
cousin(X, Y) :-
    father(F1, X),
    father(F2, Y),
    brother(F1, F2).

% grandson(X, Y): X is a grandson of Y if Y is the father of X's father.
grandson(X, Y) :-
    father(Y, Z),
    father(Z, X).

% descendent(X, Y): Base case - X is a direct child of Y.
descendent(X, Y) :-
    father(Y, X).

% descendent(X, Y): Recursive case - X is a descendant of Z, where Z is a child of Y.
descendent(X, Y) :-
    father(Y, Z),
    descendent(X, Z).