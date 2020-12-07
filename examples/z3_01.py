from z3 import *
########################
# Propositional Logic
########################
# create a fresh propositional variable uniquely identified by its name 'p'
# excluded middle

slvr = Solver()
slvr.push()
p = Bool('p')
slvr.add(Not(Or(p, Not(p))))
print(slvr.check())
# print (slvr.model())


# Pierce's law
slvr.pop()
slvr.push()
q = Bool('q')
slvr.add(Not(Implies(Implies(Implies(p, q), p), p)))
print(slvr.check())
# print (slvr.model())

# De Mogan's law
slvr.pop()
slvr.push()
a = Bool('a')
b = Bool('b')
and_a_b = And(a, b)
not_or = Not(Or(Not(a), Not(b)))
slvr.add(and_a_b == not_or)
print(slvr.check())
# print (slvr.model)

# Other useful connectives:
#Implies, And

########################################
# Uninterpreted functions and constants
########################################

slvr.pop()
slvr.push()
A = DeclareSort('A')
x = Const('x', A)
y = Const('y', A)
f = Function('f', A, A)  # f : a -> a
slvr.add(f(f(x)) == x)
slvr.add(f(x) == y)
slvr.add(Not(x == y))
print(slvr)
print(slvr.check())
print(slvr.model())

########################################
# Arithmetic
########################################

slvr.pop()
slvr.push()
a = Const('a', IntSort())
b = Const('b', IntSort())
c = Const('c', IntSort())
d = Const('d', RealSort())
e = Const('e', RealSort())
slvr.push()
slvr.add(a > b+2, a == 2*c + 10, c+b <= 1000, d >= e)
print(slvr)
print(slvr.check())
print(slvr.model())
slvr.pop()
slvr.add(e > ToReal(a+b)+2.0, d == ToReal(c)+0.5, a > b)
print(slvr.check())
print(slvr.model())

# Nonlinear arithmetic


# Division
slvr.pop()
slvr.push()
a = Int('a')
# r1  = Int('r1')
# r2 = Int('r2')
# r3 = Int('r3')
# r4 = Int('r4')
r = [Int('r' + str(i)) for i in range(0, 10)]
slvr.add(a == 10, r[1] == a/4, r[2] == a % 4)
slvr.add(r[3] == a % 4, r[4] == a / -4)
slvr.add(r[5] == a % -4, r[6] == a % -4)
print(slvr.check())
print(slvr.model())


########################################
# Bitvectors
########################################

# Prove a bitwise version of deMorgan's law:
slvr.pop()
slvr.push()
x = BitVec('x', 64)
y = BitVec('y', 64)
slvr.add(Not(((~x) & (~y)) == ~(x | y)))
print(slvr)
print(slvr.check())
# we get an unsat
# print(slvr.model())
a = BitVecVal(-1, 16)
b = BitVecVal(65535, 16)
print(simplify(a == b))


bv_const_zero = BitVecVal(0, 32)
bv_const_one = BitVecVal(1, 32)


def power_of_two(x):
    bv_and = x & (x - bv_const_one)
    return bv_and == bv_const_zero


# Bit tricks
x = BitVec('x', 32)
powers = [2**i for i in range(32)]
# fast = And(x != 0, x & (x - 1) == 0)
fast = And(x != bv_const_zero, power_of_two(x))
# fast = power_of_two(x)
slow = Or([x == p for p in powers])
print(fast)
prove(fast == slow)

print("trying to prove buggy version...")
fast = x & (x - 1) == 0
print(fast)
prove(fast == slow)
