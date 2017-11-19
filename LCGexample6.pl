proc(a).
proc(b).
proc(c).
proc(d).
proc(e).
proc(f).

init(a,0).
init(b,0).
init(c,0).
init(d,0).
init(e,0).
init(f,0).

node(a,1,1).
node(b,1,2).
node(c,1,3).
node(e,1,4).
node(d,0,5).
node(e,0,6).
node(f,0,7).
node(a,0,8).

parent(1,2).
parent(1,3).
parent(2,4).
parent(2,5).
parent(3,6).
parent(3,7).
parent(4,8).
parent(5,8).
parent(6,8).

