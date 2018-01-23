%---N stands for numbering
prior(N1,N2) :- parent(N2,N1).
prior(N1,N3) :- prior(N1,N2), prior(N2,N3).
prior(N1,N2) :- node(P1,S1,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3, P1!=P2. 
validNode(P,S,N) :- node(P,S,N), newParent(N,_).
validNode(P,S,N) :- node(P,S,N), newParent(_,N).
1{seq(1..O,P,S)} :- validNode(P,S,N), O={validNode(P1,S1,N1):validNode(P1,S1,N1)}.
:- rule(N1,N2), node(P1,S1,N1), node(P2,S2,N2), seq(O1,P1,S1), seq(O2,P2,S2), O1>=O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), P1!=P2, O1==O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), S1!=S2, O1==O2.

%--------output formatting
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), not init(P2,S2), O1>O2, not addTransition(_,P1,S1).
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), init(P2,S2), P1<P2, O1>O2, not addTransition(_,P2,S2), not addTransition(_,P1,S1).

unreachable :- prior(N1,N2), prior(N2,N1), N1<N2.
reachable :- not unreachable.
conflict(P2) :- prior(N1,N2), prior(N2,N1), node(P1,_,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3, P1!=P2.

newParent(N1,N2) :- addParent(N1,N2).
newParent(N1,N2) :- parent(N1,N2).
rule(N1,N2) :- newParent(N2,N1).
rule(N1,N3) :- rule(N1,N2), rule(N2,N3).
rule(N1,N2) :- node(P1,S1,N1), node(P2,S2,N2), node(P2,S3,N3), newParent(N1,N3), init(P2,S3), S2!=S3, P1!=P2, not addParent(N3,_), N1!=N3, N2!=N3.
rule(N3,N2) :- init(P,S), addTransition(N,P,S), node(P,S,N2), node(P,S1,N1), newParent(N3,N1), S1!=S.
{addTransition(N,P,S)}1 :- transition(N,P,S), conflict(P), init(P,S).
:- 2{addTransition(N,P,S):init(P,S)}.
{addTransition(N2,P2,S2)}1 :- addTransition(N1,P1,S1), comp(N1,P2,S2), not init(P2,S2), transition(N2,P2,S2).
:- addTransition(N,P1,S1), comp(N,P2,S2), not init(P2,S2), not addTransition(_,P2,S2), node(P2,S2,N2), not newParent(N2,_).
addParent(N1,N2) :- addTransition(N,P1,S1), comp(N,P2,S2), node(P1,S1,N1), node(P2,S2,N2).
reachableAfterAddition :- unreachable, 0{seq(O,P,S):seq(O,P,S)}.
%noSolution :- not reachableAfterAddition.


%#include "LCGexample6.pl".
#show seq/3.
#show unreachable/0.
#show reachable/0.
#show conflict/1.
#show addTransition/3.
#show addParent/2.
#show reachableAfterAddition/0.
