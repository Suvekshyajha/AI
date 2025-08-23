% demonstrate that if all mammals are warm-blooded and all cats are mammals, then all cats are warm-blooded.

% Facts: cats are mammals
mammal(cat).

% Rule: all mammals are warm-blooded
warm_blooded(X) :-
    mammal(X).
