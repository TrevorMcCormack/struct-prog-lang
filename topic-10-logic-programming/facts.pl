% Define people
person(greg).
person(susan).

% Define family relationships
son(greg, david).
son(david, jack).

daughter(kim, david).
daughter(steph, david).

% Define general child relationships
child(X, Y) :- son(X, Y).
child(X, Y) :- daughter(X, Y).

% Define grandchild relationships
grandchild(X, Y) :- child(X, Z), child(Z, Y).

% Define grandson relationships
grandson(X, Y) :- son(X, Z), child(Z, Y).

% Define gender based on child relationships
male(X) :- son(X, _).
female(X) :- daughter(X, _).

% Define granddaughter relationships
granddaughter(X, Y) :- grandchild(X, Y), female(X).

% Define grandmother relationships
grandmother(X, Y) :- grandchild(Y, X), female(X).

upper([],_,[]).
upper([H|T], V, [H|Rest]) :- H > V, upper(T, V, Rest).
upper([H|T], V, Rest) :- H =< V, upper(T, V, Rest).

lower([],_,[]).
lower([H|T], V, [H|Rest]) :- H < V, lower(T, V, Rest).
lower([H|T], V, Rest) :- H >= V, lower(T, V, Rest).

equal([],_,[]).
equal([H|T], V, [H|Rest]) :- H =:= V, equal(T, V, Rest).
equal([H|T], V, Rest) :- H =\= V, equal(T, V, Rest).

qsort([], []).
qsort([V|Rest], Sorted) :-
    lower(Rest, V, Lower),
    equal([V|Rest], V, Equal),
    upper(Rest, V, Upper),
    qsort(Lower, SortedLower),
    qsort(Upper, SortedUpper),
    append(SortedLower, Equal, Temp),
    append(Temp, SortedUpper, Sorted).
