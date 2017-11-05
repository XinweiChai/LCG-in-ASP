proc(a).  proc(b).  proc(c).
branch(1..2).
init(a,0).
init(b,0).
init(c,0).

nodeState(1,1,a,1).
nodeState(1,2,b,0).
nodeState(2,1,b,1).
nodeState(2,4,c,0).
