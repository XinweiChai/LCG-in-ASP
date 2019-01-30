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
reachable(state(A,B,C),state(A,B,C)) :- loc(A), loc(B), loc(C).
reachable(X,Z) :- trans(Y, Z), reachable(X,Y).
loc_reach(a,A1,state(A2,B2,C2)) :- reachable(state(A1,_,_), state(A2,B2,C2)), A1!=A2.
loc_reach(b,B1,state(A2,B2,C2)) :- reachable(state(_,B1,_), state(A2,B2,C2)), B1!=B2.
loc_reach(c,C1,state(A2,B2,C2)) :- reachable(state(_,_,C1), state(A2,B2,C2)), C1!=C2.

loc_unreach(a,A2,state(A1,B1,C1)) :- not loc_reach(a,A2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2), A1!=A2.
loc_unreach(b,B2,state(A1,B1,C1)) :- not loc_reach(b,B2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2), B1!=B2.
loc_unreach(c,C2,state(A1,B1,C1)) :- not loc_reach(c,C2,state(A1,B1,C1)), state(A1,B1,C1), state(A2,B2,C2), C1!=C2.
%#show reachable/2.
#show loc_reach/3.
#show loc_unreach/3.
%#show unreachable/3.
