## Limit of a function

import sympy as sp

x = sp.symbols('x')
f = (x**2 - 1)/(x-1)
limit = sp.limit(f,x,1)

print(limit)


##Derivative

x=sp.symbols('x')
f=sp.sin(x)
dfdx = sp.diff(f,x)

print(dfdx)
