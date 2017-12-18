%---N stands for node numbering
prior(N1,N2) :- parent(N2,N1).
prior(N1,N3) :- prior(N1,N2), prior(N2,N3).
prior(N1,N2) :- node(P1,S1,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3, P1!=P2. 
1{seq(1..O,P,S)}1 :- node(P,S,N), O={node(P1,S1,N1):node(P1,S1,N1)}, not unreachable.
:- rule(N1,N2), node(P1,S1,N1), node(P2,S2,N2), seq(O1,P1,S1), seq(O2,P2,S2), O1>O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), P1!=P2, O1=O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), S1!=S2, O1=O2.

%--------output formatting
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), not init(P2,S2),O1>O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), init(P2,S2), P1<P2,O1>O2.

unreachable :- prior(N1,N2), prior(N2,N1), N1<N2.
reachable :- not unreachable.
conflict(P2) :- prior(N1,N2), prior(N2,N1), node(P1,_,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3, P1!=P2.

rule(N1,N2) :- parent(N2,N1).
rule(N1,N3) :- rule(N1,N2), rule(N2,N3).
rule(N1,N2) :- node(P1,S1,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3, P1!=P2, not conflict(P2).
addTransition(N,P,S) :- transition(N,P,S), conflict(P).
%#minimize{{addTransition(N,P,S):addTransition(N,P,S)}}.
%node(
%parent()



#include "LCGexample5.pl".
#show seq/3.
#show unreachable/0.
#show reachable/0.
#show conflict/1.
#show addTransition/3.
