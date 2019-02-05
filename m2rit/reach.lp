state(0,0,0).
state(0,0,1).
state(0,1,0).
state(0,1,1).
state(1,0,0).
state(1,0,1).
state(1,1,0).
state(1,1,1).
loc(0).
loc(1).
%Global reachability
reachable(a,A,state(A,B,C)) :- loc(A), loc(B), loc(C).
reachable(b,B,state(A,B,C)) :- loc(A), loc(B), loc(C).
reachable(c,C,state(A,B,C)) :- loc(A), loc(B), loc(C).
reachable(a,A,X) :- trans(X, state(A,B,C)).
reachable(b,B,X) :- trans(X, state(A,B,C)).
reachable(c,C,X) :- trans(X, state(A,B,C)).
reachable(X,Y,W) :- trans(W, Z), reachable(X,Y,Z).

%unreachable(a,A2,state(A1,B1,C1)) :- not reachable(a,A2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2).
%unreachable(b,B2,state(A1,B1,C1)) :- not reachable(b,B2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2).
%unreachable(c,C2,state(A1,B1,C1)) :- not reachable(c,C2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2).
#show reachable/3.
%#show unreachable/3.
