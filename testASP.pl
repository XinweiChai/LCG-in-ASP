unsatisfied(1,1).
unsatisfied(1,2).
unsatisfied(2,1).
proc(1). proc(2).
satisfied(X):- not unsatisfied(X,_), proc(X).
