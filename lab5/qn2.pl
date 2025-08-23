% Define inheritance relationships between entities
is_a(dog, animal).
is_a(cat, animal).
is_a(parrot, bird).
is_a(bird, animal).

% Define properties that entities possess
has(animal, eyes).
has(animal, mouth).
has(dog, tail).
has(parrot, wings).

% Define other relationships between entities
related_to(dog, likes, bone).
related_to(cat, chases, mouse).
related_to(parrot, likes, fruit).

% Determine if an entity has a property, either directly or via inheritance
has_property(Entity, Property) :-
    has(Entity, Property).

has_property(Entity, Property) :-
    is_a(Entity, Parent),
    has_property(Parent, Property).

% Find all ancestors of an entity through inheritance
ancestor(Entity, Ancestor) :-
    is_a(Entity, Ancestor).

ancestor(Entity, Ancestor) :-
    is_a(Entity, Parent),
    ancestor(Parent, Ancestor).

% Find entities related to another entity via a specific relationship
related(Entity1, Relation, Entity2) :-
    related_to(Entity1, Relation, Entity2).
%dont write this comment just use these queries 
%has_property(dog, tail).
% has_property(dog, eyes).
%ancestor(parrot, X).


%dont write this comment just use these queries 
%has_property(dog, tail).
% has_property(dog, eyes).

%ancestor(parrot, X).
