%---N stands for node numbering
prior(N1,N2) :- parent(N2,N1).
prior(N1,N3) :- prior(N1,N2), prior(N2,N3).
prior(N1,N2) :- node(P1,S1,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3, P1!=P2.
%localState(P,S) :- node(P,S,N).
%1{seq(1..O,P,S)}1 :- localState(P,S), O={node(P1,S1,N1):node(P1,S1,N1)}.
1{seq(1..O,P,S)}1 :- node(P,S,N), O={node(P1,S1,N1):node(P1,S1,N1)}.
:- prior(N1,N2), node(P1,S1,N1), node(P2,S2,N2), seq(O1,P1,S1), seq(O2,P2,S2), O1>O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), P1!=P2, O1=O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), S1!=S2, O1=O2.
%--------
%simplification of output
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), not init(P2,S2),O1>O2.
:- seq(O1,P1,S1), seq(O2,P2,S2), init(P1,S1), init(P2,S2), P1<P2,O1>O2.

#show seq/3.
