% ----- Facts: symptoms of diseases -----
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(sore_throat).

disease(cold) :-
    symptom(cough),
    symptom(sneezing),
    symptom(runny_nose).

disease(allergy) :-
    symptom(sneezing),
    symptom(runny_nose),
    symptom(itchy_eyes).

% ----- Ask user about symptoms -----
ask(symptom(fever)) :-
    write('Do you have a fever? (yes/no)'), nl,
    read(Answer),
    Answer = yes.

ask(symptom(cough)) :-
    write('Do you have a cough? (yes/no)'), nl,
    read(Answer),
    Answer = yes.

ask(symptom(sore_throat)) :-
    write('Do you have a sore throat? (yes/no)'), nl,
    read(Answer),
    Answer = yes.

ask(symptom(sneezing)) :-
    write('Are you sneezing? (yes/no)'), nl,
    read(Answer),
    Answer = yes.

ask(symptom(runny_nose)) :-
    write('Do you have a runny nose? (yes/no)'), nl,
    read(Answer),
    Answer = yes.

ask(symptom(itchy_eyes)) :-
    write('Do you have itchy eyes? (yes/no)'), nl,
    read(Answer),
    Answer = yes.

% ----- Check symptoms -----
symptom(X) :-
    ask(X).

% ----- Start the system -----
diagnose :-
    disease(D),
    write('You may have: '), write(D), nl.
