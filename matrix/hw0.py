# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    return [x for x in L if x%num != 0]



## Problem 2
def myLists(L):
    return [list(range(1,x+1)) for x in L]



## Problem 3
def myFunctionComposition(f, g):
    return {key_f:g[f[key_f]] for key_f in f}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 0 +1j
complex_addition_c = -1 +.001j
complex_addition_d = .001 +9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    total = 0
    for e in L:
        total += e
    return total



## Problem 7
def myProduct(L):
    total = 1
    for e in L:
        total *= e
    return total



## Problem 8
def myMin(L):
    L.sort()
    return L[0]



## Problem 9
def myConcat(L):
    L1 = ""
    for s in L:
        L1 += s
    return L1



## Problem 10
def myUnion(L):
    s = set()
    for x in L:
        s.update(x)
    return s

