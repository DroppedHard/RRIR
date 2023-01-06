import numpy as np
import matplotlib.pyplot as plt

# boundary condition values
start = 0
target = 8
f1 = lambda x,y : 4*x - (2*y)/x
f2 = lambda x,y : x**5 + 1
f3 = lambda x,y : 8*np.exp(-x)*(1 + x) - 2*y

def linear_interpolation (guess1, guess2, solution1, solution2):
    m = (guess1 - guess2) / (solution1 - solution2)
    return guess2 + m*(target - solution2)

# solves ode using forward Euler method
def solve_ivp (f, step_size, xstart, xend, ystart):
    dydx = f
    step_size = 0.5
    x_vals = np.arange(xstart, xend, step_size)
    y_vals = np.zeros_like(x_vals)
    y_vals[0] = ystart

    for i, x_val in enumerate(x_vals[:-1]):
        y_vals[i+1] = y_vals[i] + dydx(x_val, y_vals[i])*step_size
    
    return (x_vals, y_vals)

def show_chart (x_vals, y_vals):
    plt.plot(
    x_vals, y_vals, 
    marker='.', markersize=15, 
    linestyle='--', label='Numerical solution'
    )

    plt.grid(True)
    plt.legend()
    plt.show()

guess = 20
(xs, ys) = solve_ivp(f3, start, target, guess)
show_chart(xs, ys)