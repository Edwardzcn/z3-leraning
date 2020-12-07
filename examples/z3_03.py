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
