import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, lambdify, diff
import types

def d(expr):
    return diff(expr,t)
def tofunc(expr):
    return lambdify((t), expr, 'numpy')
def draw(func,name,expr):
    t = np.linspace(0,3,100)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot()
    if expr.is_constant():
        func = np.ones_like(t) * expr
        ax.plot(t,func)
    else:
        ax.plot(t,func(t))
    ax.set_title(f"Đồ thị của {name} theo t")
    ax.set_xlabel('t')
    ax.set_ylabel(f'{name}')
    ax.axis('equal')
 
#input
t = symbols('t')
theta = input("Nhap ham theta(t): ")
I = float(input("Nhap moment quan tinh: "))
theta_expr = sympify(theta)
theta_func = tofunc(theta_expr)

#Find Omega
omega_expr = d(theta_expr)
omega_func = tofunc(omega_expr)

#Find Beta
beta_expr = d(omega_expr)
beta_func = tofunc(beta_expr)

#Find Moment
moment = I * beta_expr
moment_func = tofunc(moment)

print(f"Van toc goc: {omega_expr}")
print(f"Gia toc goc: {beta_expr}")
print(f"Moment luc: {moment}")

#Draw
draw(theta_func,"theta(t)",theta_expr)
draw(moment_func, "Moment(t)",moment)
plt.show()