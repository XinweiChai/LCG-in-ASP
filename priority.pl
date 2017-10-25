prior(B1,B2) :- nodeState(B1,_,X,A), nodeState(B2,_,X,_), proc(X), init(X,A), B1!=B2.
prior(B1,B2) :- prior(B1,B3), prior(B3,B2).
unreachable(B1,B2):- prior(B1,B2), prior(B2,B1),B1<B2.
%reachable(B1) :- not unreachable(B1,_), not unreachable(_,B1), prior(B1,_). 
%reachable(B1) :- not unreachable(B1,_), not unreachable(_,B1), prior(_,B1). 
reachable :- not unreachable(_,_).
%reachable :- {unreachable(_,_)}0.
%#show prior/2.
#show unreachable/2.
%#show reachable/1.
#show reachable/0.
