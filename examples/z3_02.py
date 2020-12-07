from z3 import *

slvr = Solver()

########################
# Arrays
########################


def util_print(s: Solver):
    r = s.check()
    print(r)
    if r.__repr__() == "sat":
        print(s.model())


slvr.push()
x = Int('x')
y = Int('y')
a1 = Array('a1', IntSort(), IntSort())
slvr.push()
a2 = Array('a2', IntSort(), IntSort())
util_print(slvr)

slvr.pop()
slvr.add(Select(a1, x) == x)
slvr.add(Store(a1, x, y) == a1)
util_print(slvr)
slvr.add(x != y)
util_print(slvr)


########################
# Datatypes
######################

# Records

slvr.pop()
slvr.push()
Pair = Datatype('Pair')
Pair.declare('mk_pair', ('pair_first', IntSort()),
             ('pair_second', IntSort()))  # single constructor
Pair = Pair.create()
mp = Pair.mk_pair
fi = Pair.pair_first
se = Pair.pair_second
p1 = Const('p1', Pair)
p2 = Const('p2', Pair)
slvr.add(p1 == p2)
slvr.add(se(p2) > 20)
util_print(slvr)
slvr.add(fi(p1) != fi(p2))
util_print(slvr)

# Scalars

slvr.pop()
slvr.push()
S = Datatype('S')
S.declare('A')
S.declare('B')
S.declare('C')
S = S.create()
x = Const('x', S)
y = Const('y', S)
z = Const('z', S)
u = Const('u', S)
slvr.add(Distinct(x, y, z))
util_print(slvr)
slvr.add(Distinct(x, y, z, u))
util_print(slvr)

slvr.pop()
slvr.push()
Lst = Datatype('Lst')
Lst.declare('nil')
Lst.declare('cons', ('hd', IntSort()), ('tl', Lst))
Lst = Lst.create()
print(Lst.cons(10, Lst.nil).sort())
