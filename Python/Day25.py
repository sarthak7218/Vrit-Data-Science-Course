## Higher-Order-Derivative

import sympy as sp

x = sp.symbols('x')
f = sp.sin(x)
dfdx = sp.diff(f, x)
print(dfdx)

d2fdx2 = sp.diff(f,x,2)
print(d2fdx2)

x = sp.symbols('x')
f = sp.sin(x)
dfdx = sp.diff(f,x)
dfdx2 = sp.diff(dfdx,x)
print(dfdx2)


##Implicit Differentiation

x, y = sp.symbols('x y')
f = x**2 + y**2 - 4
dfdx = sp.diff(f, x)
dfdy = sp.diff(f, y)
dydx = -dfdx/dfdy
print(dydx)


##Partial Differentiation

#Define the function
x, y = sp.symbols('x y')
f = x**2 + 3*x*y + y**2

#Find the partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

#Evaluate the partial derivatives
point = {x: 1, y: 2}
df_dx_at_point = df_dx.subs(point)
df_dy_at_point = df_dy.subs(point)

print("Partial differentiation wrt x:", df_dx_at_point)
print("Partial differentiation wrt y:", df_dx_at_point)


##Gradient-and-Gradient-Descent

import numpy as np

#Define the function
def f(x, y):
    return x**2 + 2*y

#Compute the gradients
def gradient(x, y):
    df_dx = 2*x
    df_dy = 2
    return np.array([df_dx, df_dy])

#Test the gradients
x = 2
y = 3
grads = gradient(x, y)
print(grads)

def gradient_descent(starting_point, learning_rate, num_iterations):
    #Initialize the parameters
    point = starting_point

    #Iterate
    for i in range(num_iterations):
        #Compute the gradient
        grad = gradient(point[0], point[1])

        #Update the parameters
        point = point - learning_rate * grad

    return point

#Test the gradient descent function
starting_point = np.array([2, 3])
learning_rate = 0.1
num_iterations = 100
optimum = gradient_descent(starting_point, learning_rate, num_iterations)
print("Optimal point: ", optimum)
print("Optimal Value: ", f(optimum[0], optimum[1]))





