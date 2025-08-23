% ----- Jug capacities -----
capacity(a, 4).
capacity(b, 3).

% ----- Initial and goal state -----
initial(state(0,0)).
goal(state(2,_)).  % Goal: 2 liters in Jug A

% ----- Solve predicate -----
solve :-
    initial(State),
    write('Starting state: '), write(State), nl,
    water_jug(State, []).

% ----- Base case: goal reached -----
water_jug(State, _) :-
    goal(State),
    write('Goal reached! '), write(State), nl.

% ----- Recursive case: explore next moves -----
water_jug(State, Visited) :-
    \+ member(State, Visited),
    move(State, NewState),
    write('Move to: '), write(NewState), nl,
    water_jug(NewState, [State|Visited]).

% ----- Move rules -----

% Fill Jug A
move(state(A,B), state(MaxA,B)) :-
    capacity(a, MaxA),
    A < MaxA.

% Fill Jug B
move(state(A,B), state(A,MaxB)) :-
    capacity(b, MaxB),
    B < MaxB.

% Empty Jug A
move(state(A,B), state(0,B)) :- A > 0.

% Empty Jug B
move(state(A,B), state(A,0)) :- B > 0.

% Pour A -> B
move(state(A,B), state(NewA,NewB)) :-
    A > 0,
    capacity(b, MaxB),
    SpaceB is MaxB - B,
    SpaceB > 0,
    Pour is min(A, SpaceB),
    NewA is A - Pour,
    NewB is B + Pour.

% Pour B -> A
move(state(A,B), state(NewA,NewB)) :-
    B > 0,
    capacity(a, MaxA),
    SpaceA is MaxA - A,
    SpaceA > 0,
    Pour is min(B, SpaceA),
    NewA is A + Pour,
    NewB is B - Pour.
