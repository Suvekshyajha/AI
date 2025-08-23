% Define classes with parent class and default slots
class(vehicle, none, [wheels=4, fuel=none]).
class(car, vehicle, [fuel=petrol, airbags=2]).
class(cycle, vehicle, [fuel=none, num_gears=6]).
class(boat, vehicle, [engine_count=2, fuel=diesel]).

% Define instances/objects with possible slot overrides
instance(car1, car, [color=black]).  
instance(cycle1, cycle, [num_gears=18, color=red]).  
instance(boat1, boat, [engine_count=4, color=blue]).

% Retrieve the value of a slot for a given instance (checks instance first, then class hierarchy)
get_slot(Instance, Slot, Value) :-
    instance(Instance, Class, InstanceSlots),
    ( member(Slot=Value, InstanceSlots)           % Check if instance overrides slot
    ; get_class_slot(Class, Slot, Value) ).      % Otherwise, check class and parent recursively

% Retrieve slot value from a class (current class only)
get_class_slot(Class, Slot, Value) :-
    class(Class, _, Slots),
    member(Slot=Value, Slots).

% Retrieve slot value from parent class recursively if not found in current class
get_class_slot(Class, Slot, Value) :-
    class(Class, Parent, _),
    Parent \= none,
    get_class_slot(Parent, Slot, Value).

%dont write this comment just use these queries
%get_slot(car1, color, X).
% get_slot(car1, wheels, X).
% get_slot(car1, airbags, X).
