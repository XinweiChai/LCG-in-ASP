state(X,0..1) :- proc(X).

conflict(X,B1,B2) :- nodeState(B1,_,X,LS1), nodeState(B2,_,X,LS2), B1!=B2, LS1!=LS2.

indirConflict(B1,B2) :- conflict(X,B1,B3), conflict(Y,B2,B3), not conflict(X,B1,B2), not conflict(Y,B1,B2), B1!=B2.
indirConflict(B1,B2) :- indirConflict(B1,B3), conflict(X,B2,B3), B1!=B2.
unsatisfied(X,B1,B2) :- conflict(X,B1,B2), indirConflict(B1,B2).
unsatisfied(X,B1,B2) :- conflict(X,B1,B2), conflict(Y,B1,B2), X!=Y, B1<B2.

%satis(X) :- 0{unsatisfied(X,_,_)}0,proc(X).
satisfied(X) :- not unsatisfied(X,_,_), proc(X).
%#show conflict/3.
%#show indirConflict/2.
#show unsatisfied/3.
#show satisfied/1.
