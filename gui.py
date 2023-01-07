import tkinter as tk
import method
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
import equations as eq


def main_screen():
    window = tk.Tk()
    window.title('Shooting method')
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=3)
    window.rowconfigure(2, weight=3)

    slider_label = tk.Label(window, text='Step size')
    slider = tk.Scale(window, from_=0.1, to=1, tickinterval=0.2, length=160, orient='horizontal', resolution=0.1)
    slider.set(0.1)

    options = map(lambda equation: equation[1], eq.get_equations())

    clicked = tk.StringVar()
    clicked.set(eq.get_equations()[0][1])
    equations_label = tk.Label(window, text='Equations')
    equations = tk.OptionMenu(window, clicked, *options)
    equations.configure(width=45)

    figure_canvas, plots = plot_create(window)

    button = tk.Button(window, text="Plot", command=lambda: button_click(clicked, slider, plots))

    window.protocol("WM_DELETE_WINDOW", lambda: exit())

    window.configure(bg='#333333')
    slider_label.configure(bg='#333333', fg='white')
    slider.configure(bg='#333333', fg='white')
    equations_label.configure(bg='#333333', fg='white')
    equations.configure(bg='#333333', fg='white')
    button.configure(bg='#333333', fg='white')

    slider_label.grid(column=0, row=0)
    slider.grid(column=0, row=1)
    equations_label.grid(column=1, row=0)
    equations.grid(column=1, row=1)
    button.grid(column=2, row=1)
    figure_canvas.grid(column=0, row=2, columnspan=3)

    tk.mainloop()


def plot_create(window):
    plt.rcParams['toolbar'] = 'None'
    figure = plt.figure(facecolor='#333333')
    
    figure_canvas = FigureCanvasTkAgg(figure, window)
    figure_canvas.draw()
    plots = figure.add_subplot()

    plots.grid(True)
    plots.tick_params(colors='white', which='both') 
    
    return figure_canvas.get_tk_widget(), plots


def plot_redraw(data, plot, exact_solution):
    x_vals, solutions = data
    plot.clear()
    for i, solution in enumerate(solutions):
        label = "shot #" + str(i + 1)
        plot.plot(
            x_vals, solution, 
            marker='.', markersize=5, 
            linestyle='--', label=label)
    plot.plot(
            x_vals, exact_solution,
            marker='None',
            linewidth=3,
            linestyle='-', label="exact plot")
    plot.grid(True)
    plot.tick_params(colors='white', which='both')
    plot.legend(loc='best')
    plt.draw() 


def button_click(clicked, slider, plot):
    equation = clicked.get()
    step = slider.get()
    data, exact_solution = method.give_equation(equation, step)
    plot_redraw(data, plot, exact_solution)
    