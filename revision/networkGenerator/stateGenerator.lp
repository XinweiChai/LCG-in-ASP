state(0,0,0).
state(0,0,1).
state(0,1,0).
state(0,1,1).
state(1,0,0).
state(1,0,1).
state(1,1,0).
state(1,1,1).

{trans(state(A1,B1,C1), state(A2,B1,C1))} :- state(A1,B1,C1), state(A2,B1,C1), A1!=A2.
{trans(state(A1,B1,C1), state(A1,B2,C1))} :- state(A1,B1,C1), state(A1,B2,C1), B1!=B2.
{trans(state(A1,B1,C1), state(A1,B1,C2))} :- state(A1,B1,C1), state(A1,B1,C2), C1!=C2.
:- {trans(state(A,B,C),_)}0, state(A,B,C).
:- {trans(state(A1,B1,C1),state(A2,B2,C2)):trans(state(A1,B1,C1),state(A2,B2,C2))}16, state(A,B,C).
%:- trans(state(A1,B1,C1), state(A1,B1,C1)).


reachable(0,A2,state(A1,B1,C1)) :- trans(state(A1,B1,C1), state(A2,B2,C2)).
reachable(0,A2,state(A1,B1,C1)) :- trans(state(A1,B1,C1), X), reachable(0,A2,X).

:- reachable(0,1,state(0,0,_)).

#show trans/2.
%#show reachable/3.
