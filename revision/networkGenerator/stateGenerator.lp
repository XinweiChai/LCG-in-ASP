{trans(state(V0, V1, V2, V3), state(V0X,V1,V2,V3))} :- state(V0, V1, V2, V3), state(V0X, V1, V2, V3), V0!=V0X.
{trans(state(V0, V1, V2, V3), state(V0,V1X,V2,V3))} :- state(V0, V1, V2, V3), state(V0, V1X, V2, V3), V1!=V1X.
{trans(state(V0, V1, V2, V3), state(V0,V1,V2X,V3))} :- state(V0, V1, V2, V3), state(V0, V1, V2X, V3), V2!=V2X.
{trans(state(V0, V1, V2, V3), state(V0,V1,V2,V3X))} :- state(V0, V1, V2, V3), state(V0, V1, V2, V3X), V3!=V3X.
:- {trans(state(V0, V1, V2, V3), _)}0, state(V0, V1, V2, V3).
:- {trans(state(V0, V1, V2, V3), state(V0X, V1X, V2X, V3X)) : trans(state(V0, V1, V2, V3), state(V0X, V1X, V2X, V3X))}17.
#show trans/2.