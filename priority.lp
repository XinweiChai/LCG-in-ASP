%prior(B1,B2) :- nodeState(B1,_,X,A), nodeState(B2,_,X,_), proc(X), init(X,A), B1!=B2.%priority of branches
%---------------
%priority of states
%node(B,N) :- branch(B), nodeState(B,N,_,_).%Definition with only positions
prior(P1,S1,P2,S2) :- nodeState(B,N1,P1,S1), nodeState(B,N2,P2,S2), N1>N2.%If one node is after another, then it is fired at first 
prior(P,S1,P,S2) :- nodeState(B1,N1,P,S1), nodeState(B2,N2,P,S2), init(P,S1), S1!=S2.%If a node is in initial state, then it is prior to others
prior(P3,S3,P,S2) :- nodeState(B1,N1,P,S1), nodeState(B2,N2,P,S2), init(P,S1), S1!=S2, nodeState(B1,N1-1,P3,S3).%and the predecessor is also prior
prior(P1,S1,P3,S3) :- prior(P1,S1,P2,S2), prior(P2,S2,P3,S3).%Passivity of priority
localState(P,S) :- nodeState(_,_,P,S).
1{seq(1..O,P,S)}1 :- localState(P,S), O={nodeState(B,N,P1,S1):nodeState(B,N,P1,S1)}.
:- prior(P1,S1,P2,S2), seq(O1,P1,S1), seq(O2,P2,S2),O1>O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), P1!=P2, O1=O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), S1!=S2, O1=O2.
%--------
%simplification of output
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), not init(P2,S2),O1>O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), init(P2,S2), P1<P2,O1>O2.


%prior(B1,B2) :- prior(B1,B3), prior(B3,B2).
%unreachable(B1,B2):- prior(B1,B2), prior(B2,B1),B1<B2.
%reachable(B1) :- not unreachable(B1,_), not unreachable(_,B1), prior(B1,_). 
%reachable(B1) :- not unreachable(B1,_), not unreachable(_,B1), prior(_,B1). 
%reachable :- not unreachable(_,_).
%reachable :- {unreachable(_,_)}0.
#show prior/4.
%#show localState/2.
%#show unreachable/2.
%#show reachable/1.
%#show reachable/0.
#show seq/3.
