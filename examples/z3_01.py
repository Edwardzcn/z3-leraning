from z3 import *
########################
## Propositional Logic
########################
# create a fresh propositional variable uniquely identified by its name 'p'
# excluded middle

slvr = Solver()
slvr.push()
p = Bool('p')
slvr.add(Not(Or(p, Not(p))))
print (slvr.check())
# print (slvr.model())


# Pierce's law
slvr.pop()
slvr.push()
q = Bool('q')
slvr.add(Not(Implies(Implies(Implies(p, q), p), p)))
print (slvr.check())
# print (slvr.model())

# De Mogan's law
slvr.pop()
slvr.push()
a = Bool('a')
b = Bool('b')
and_a_b = And(a,b)
not_or = Not( Or (Not(a),Not(b)))
slvr.add(and_a_b == not_or)
print (slvr.check())
# print (slvr.model)

#Other useful connectives:
#Implies, And

########################################
## Uninterpreted functions and constants
########################################

slvr.pop()
slvr.push()
A = DeclareSort('A')
x = Const('x', A)
y = Const('y', A)
f = Function('f', A, A)  # f : a -> a
slvr.add(f(f(x)) == x)
slvr.add(f(x) == y )
slvr.add(Not( x == y))
print (slvr)
print (slvr.check())
print (slvr.model())

########################################
## Arithmetic
########################################

slvr.pop()
slvr.push()
a = Const('a', IntSort())
b = Const('b', IntSort())
c = Const('c', IntSort())
d = Const('d', RealSort())
e = Const('e', RealSort())
slvr.push()
slvr.add(a > b+2 , a == 2*c + 10, c+b <= 1000, d >= e)
print(slvr)
print(slvr.check())
print(slvr.model())
slvr.pop()
slvr.add(e>ToReal(a+b)+2.0 , d==ToReal(c)+0.5 , a > b)
print(slvr.check())
print(slvr.model())

### Nonlinear arithmetic

slvr.pop()
slvr.push()
