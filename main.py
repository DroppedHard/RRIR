import numpy as np
import matplotlib.pyplot as plt
import random
import math

# picks the next guess based on two previous guesses (and resulting solutions)
def linear_interpolation (guess1, guess2, solution1, solution2, y_end):
    print("interp", guess1, guess2, solution1, solution2)
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
            print(y_end, solutions[-1][-1])
            guesses.append(linear_interpolation(guesses[-2], guesses[-1], solutions[-2][-1], solutions[-1][-1], y_end))

        solutions.append(solve_ivp_second(f, step_size, x_vals, y_start, guesses[-1]))

        if len(solutions) >= 1e4:
            break
        if len(solutions) >= 2 and solutions[-2][-1] == solutions[-1][-1]:
            break

    return (x_vals, solutions)

def plot_shots (x_vals, solutions):
    for i, solution in enumerate(solutions):
        print(solution)
        plt.plot(
            x_vals, solution, 
            marker='.', markersize=15, 
            linestyle='--', label='solution #' + str(i))

        """ plt.plot(x_vals,solutions[-1]) """

    plt.grid(True)
    plt.legend()
    plt.show()

# y'' = f(x,y,y')
f1 = lambda x,y,yprime : x*yprime + 2*y + 2*x
f2 = lambda x,y,yprime : -x*yprime + x*y + 2*x
f3 = lambda x,y,yprime : 5*yprime - 6*y
f4 = lambda x,y,yprime : -9.8

# boundary conditions y(x_start) = y_start, y(x_end) = y_end
x_start = 0
x_end = 1
y_start = 1
y_end = math.e**2

(x_vals, solutions) = shooting_method(f3, x_start, x_end, y_start, y_end, 0.1)
plot_shots(x_vals, solutions)
