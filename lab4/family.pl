% family relationships using facts and rules for parenthood, gender, and sibling relations.
% Facts: parent(X, Y) means X is parent of Y
parent(mary, george).
parent(mary, lisa).
parent(george, charlie).
parent(lisa, anna).

% Facts: gender
male(george).
male(charlie).
female(mary).
female(lisa).
female(anna).

%rule:father(x,y): x is father of y if x is male and x is parent of y
father(X,Y):-
    male(X),
    parent(X,Y).
mother(X,Y):-
    female(X),
    parent(X,Y).
sibling(X,Y):-
    parent(Z,X),
    parent(Z,Y).
%x is sister of y is x is female and they have same parent
sister(X,Y):-
    female(X),
    parent(Z,X),
    parent(Z,Y).