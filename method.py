import math
import random
import numpy as np

# picks the next guess based on two previous guesses (and resulting solutions)
def linear_interpolation (guess1, guess2, solution1, solution2, y_end):
    m = (guess1 - guess2) / (solution1 - solution2)
    return guess2 + m*(y_end - solution2)

# solves 2nd order ode using forward Euler method
# y'' = f
def solve_ivp_second (f, step_size, x_vals, y_start, yprimestart):
    y_vals = np.zeros_like(x_vals)
    y_vals[0] = y_start
    yprime_vals = np.zeros_like(x_vals)
    yprime_vals[0] = yprimestart

    # solve system of recursive equations
    for i, x_val in enumerate(x_vals[:-1]):
        y_vals[i+1] = y_vals[i] + yprime_vals[i]*step_size
        yprime_vals[i+1] = yprime_vals[i] + f(x_val, y_vals[i], yprime_vals[i])*step_size
    
    return y_vals

def shooting_method (f, x_start, x_end, y_start, y_end, step_size):
    guesses = []
    # solutions is a of list solution sequences for each guess
    solutions = []

    x_vals = np.arange(x_start, x_end, step_size)

    while (len(solutions) == 0 or np.abs(y_end - solutions[-1][-1]) > 1e-9):
    
        if(len(guesses) <= 2):
            guesses.append(random.randrange(0, 10))
        else:
            guesses.append(linear_interpolation(guesses[-2], guesses[-1], solutions[-2][-1], solutions[-1][-1], y_end))

        solutions.append(solve_ivp_second(f, step_size, x_vals, y_start, guesses[-1]))

        if len(solutions) >= 1e4:
            break
        if len(solutions) >= 2 and solutions[-2][-1] == solutions[-1][-1]:
            break

    return (x_vals, solutions)

def give_equation(equation, step):
    # r = (lambda x,y,yprime : f(x,y,y'), x_start, x_end, y_start, y_end)
    match equation:
        case "y\'\'=5y\'-6y":
            r = (lambda x,y,yprime : 5*yprime - 6*y, 0, 1, 1, math.e**2)
        case "y\'\'=2":
            r = (lambda x,y,yprime : 2, 0, 10, 0, 0)
        case "y\'\'=-8sin(x)cos(x)":
            r = (lambda x,y,yprime : -8*math.sin(x)*math.cos(x), 0, math.pi, 0, 0)
        case "y\'\'=e^x-6x^2sin(x)+x^3cos(x)-6xcos(x)":
            r = (lambda x,y,yprime : math.e**x - 6*x**2*math.sin(x) + x**3*math.cos(x) - 6*x*math.cos(x), 0, math.pi, 0, 0)
    data = shooting_method(*r, step)
    return data

""" # y'' = f(x,y,y')
f1 = lambda x,y,yprime : x*yprime + 2*y + 2*x
f2 = lambda x,y,yprime : -x*yprime + x*y + 2*x
f3 = lambda x,y,yprime : 5*yprime - 6*y
f4 = lambda x,y,yprime : 5*yprime - 6*y

# boundary conditions y(x_start) = y_start, y(x_end) = y_end
x_start = 0
x_end = 1
y_start = 1
y_end = 2
 """