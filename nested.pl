%---N stands for node numbering
prior(N1,N2) :- parent(N2,N1).
prior(N1,N3) :- prior(N1,N2), prior(N2,N3).
prior(N1,N2) :- node(P1,S1,N1), node(P2,S2,N2), node(P2,S3,N3), parent(N1,N3), init(P2,S3), S2!=S3.
