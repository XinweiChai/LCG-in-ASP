bird(tweety). chicken(tweety).
bird(tux). penguin(tux).
fly(X) :- bird(X), not -fly(X).
-fly(X) :- bird(X), not fly(X).
-fly(X) :- penguin(X).
:-fly(X), -fly(X).
%:-fly(tux), -fly(tux).

