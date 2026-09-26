% ===================================================================
% Experiment 11: Travelling Salesperson Problem (TSP) using Prolog
% Environment: SWI-Prolog
% ===================================================================

% -------------------------------------------------------------------
% 1. Facts: Symmetric road distances between cities
% distance(City1, City2, Distance).
% -------------------------------------------------------------------
edge(a, b, 10).
edge(a, c, 15).
edge(a, d, 20).
edge(b, c, 35).
edge(b, d, 25).
edge(c, d, 30).

% Bidirectional road lookup: cost between X and Y is identical in both directions
cost(X, Y, Dist) :- edge(X, Y, Dist).
cost(X, Y, Dist) :- edge(Y, X, Dist).

% -------------------------------------------------------------------
% 2. Tour Generation and Cost Calculation
% tour_cost(Tour, Cost)
% -------------------------------------------------------------------

% Base case: Only starting node left to return to
calc_path([X, Y], Total) :-
    cost(X, Y, Total).

% Recursive step: Accumulate cost along consecutive cities in path
calc_path([X, Y | Rest], Total) :-
    cost(X, Y, D1),
    calc_path([Y | Rest], D2),
    Total is D1 + D2.

% Complete tour: Starts at StartCity, visits all cities once, returns to StartCity
tour(StartCity, [StartCity | Tour]) :-
    % List of remaining cities to visit
    findall(C, (edge(C, _, _) ; edge(_, C, _)), AllCitiesWithDups),
    sort(AllCitiesWithDups, AllCities),
    delete(AllCities, StartCity, OtherCities),
    permutation(OtherCities, Permutation),
    append(Permutation, [StartCity], FullPath),
    Tour = FullPath.

% -------------------------------------------------------------------
% 3. Find All Tours and Identify the Optimal (Minimum-Cost) Route
% -------------------------------------------------------------------
all_tours(StartCity, AllTours) :-
    findall(Cost-Path,
            (tour(StartCity, Path), calc_path(Path, Cost)),
            AllTours).

% -------------------------------------------------------------------
% 4. Solver Wrapper Predicate
% -------------------------------------------------------------------
solve_tsp :-
    Start = a,
    write('----------------------------------------------------'), nl,
    write(' Solving TSP starting and ending at City: '), write(Start), nl,
    write('----------------------------------------------------'), nl,
    all_tours(Start, AllTours),
    keysort(AllTours, SortedTours), % Sorts tours in ascending order by Cost
    SortedTours = [MinCost-BestPath | _],
    nl,
    write('All Evaluated Valid Tours:'), nl,
    print_all_tours(SortedTours),
    nl,
    write('===================================================='), nl,
    write('OPTIMAL TOUR FOUND:'), nl,
    format('Path : ~w~n', [BestPath]),
    format('Cost : ~w~n', [MinCost]),
    write('===================================================='), nl.

print_all_tours([]).
print_all_tours([Cost-Path | Rest]) :-
    format('  Route: ~w  ==> Cost: ~w~n', [Path, Cost]),
    print_all_tours(Rest).