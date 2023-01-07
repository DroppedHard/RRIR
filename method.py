import random
import numpy as np
import equations as eq


# picks the next guess based on two previous guesses (and resulting solutions)
def linear_interpolation(guess1, guess2, solution1, solution2, y_end):
    m = (guess1 - guess2) / (solution1 - solution2)
    return guess2 + m*(y_end - solution2)


# solves 2nd order ode using forward Euler method
# y'' = f
def solve_ivp_second(f, step_size, x_vals, y_start, yprimestart):
    y_vals = np.zeros_like(x_vals)
    y_vals[0] = y_start
    yprime_vals = np.zeros_like(x_vals)
    yprime_vals[0] = yprimestart

    # solve system of recursive equations
    for i, x_val in enumerate(x_vals[:-1]):
        y_vals[i+1] = y_vals[i] + yprime_vals[i]*step_size
        yprime_vals[i+1] = yprime_vals[i] + f(x_val, y_vals[i], yprime_vals[i])*step_size
    
    return y_vals


def shooting_method(f, x_start, x_end, y_start, y_end, step_size):
    guesses = []
    # solutions is a of list solution sequences for each guess
    solutions = []

    x_vals = np.arange(x_start, x_end, step_size)

    while len(solutions) == 0 or np.abs(y_end - solutions[-1][-1]) > 1e-3:
    
        if len(guesses) <= 2:
            guesses.append(random.randrange(0 + 5*len(guesses), 5 + 5*len(guesses)))
        else:
            guesses.append(linear_interpolation(guesses[-2], guesses[-1], solutions[-2][-1], solutions[-1][-1], y_end))

        solutions.append(solve_ivp_second(f, step_size, x_vals, y_start, guesses[-1]))

        if len(solutions) >= 100:
            break
        if len(solutions) > 2 and solutions[-2][-1] == solutions[-1][-1]:
            break

    return x_vals, solutions


def give_equation(current_equation, step):
    for equation in eq.get_equations():
        if equation[1] == current_equation:
            solution_eq = equation[2]
            data = shooting_method(*equation[0], step)
            exact_solution = []
            for i in data[0]:
                exact_solution.append(solution_eq(i))
            return data, exact_solution
