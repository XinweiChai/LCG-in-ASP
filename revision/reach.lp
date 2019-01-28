state(0,0,0).
state(0,0,1).
state(0,1,0).
state(0,1,1).
state(1,0,0).
state(1,0,1).
state(1,1,0).
state(1,1,1).

reachable(a,A2,X) :- trans(X, state(A2,B2,C2)).
reachable(b,B2,X) :- trans(X, state(A2,B2,C2)).
reachable(c,C2,X) :- trans(X, state(A2,B2,C2)).
reachable(X,Y,W) :- trans(W, Z), reachable(X,Y,Z).

%unreachable(a,A2,state(A1,B1,C1)) :- not reachable(a,A2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2).
%unreachable(b,B2,state(A1,B1,C1)) :- not reachable(b,A2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2).
%unreachable(c,C2,state(A1,B1,C1)) :- not reachable(c,A2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2).
#show reachable/3.
%#show unreachable/3.
