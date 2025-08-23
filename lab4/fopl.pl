%all engineers are problem solvers

problemsolver(X):-
    engineer(X).
engineer(X):-
    softwaredev(X).
analyticthinker(X):-
    problemsolver(X).
good_at(X) :-
     drinks_coffee(X).
softwaredev(alice).
drinks_coffee(alice).


