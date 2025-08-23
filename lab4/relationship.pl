%Write a Prolog Program to Represent Simple Relationships.
%facts: parent(x,y) means x is parent of y
parent(mary,george).
parent(george,charlie).
parent(george,jane).
parent(jane,judy).

%rule:grandparent(x,y)
grandparent(X,Z):-
parent(X,Y),
parent(Y,Z).