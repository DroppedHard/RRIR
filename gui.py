import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

def main_screen(data):
    window = tk.Tk()
    window.tk.call("source", "azure.tcl")
    window.tk.call("set_theme", "dark")
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=3)
    window.rowconfigure(2, weight=3)

    slider_label = tk.Label(window, text='Slider')
    slider_label.grid(column=0, row=0)
    slider = tk.Scale(window, from_=0, to=50, tickinterval=10, length=200, orient='horizontal')
    slider.grid(column=0, row=1)

    options = [
        "Równanie 1",
        "Równanie 2",
        "Równanie 3",
        "Równanie 4"
    ]

    clicked = tk.StringVar()
    clicked.set("Równanie 1")
    equations_label = tk.Label(window, text='Equations')
    equations_label.grid(column=1, row=0)
    equations = tk.OptionMenu(window, clicked, *options)
    equations.grid(column=1, row=1)

    button = tk.Button(window, text="Plot", command=lambda: button_click(clicked, slider))
    button.grid(column=2, row=1)

    plot = plot_shots(data, window)
    plot.grid(column=0, row=2, columnspan=3)


    tk.mainloop()

def plot_shots (data, window):
    x_vals, solutions = data
    plt.rcParams['toolbar'] = 'None'
    figure = plt.figure(facecolor='#333333')
    
    figure_canvas = FigureCanvasTkAgg(figure, window)
    figure_canvas.draw()

    plots = figure.add_subplot()
    for i, solution in enumerate(solutions):
        labelstr = 'numerical solution' if i == len(solutions)-1 else 'shot #' + str(i)
        plots.plot(
            x_vals, solution, 
            marker='.', markersize=5, 
            linestyle='--', label='solution #' + str(i))
    plots.grid(True)
    plots.tick_params(colors='white', which='both') 
    
    return figure_canvas.get_tk_widget()
    

def button_click(clicked, slider):
    equation = clicked.get()
    match equation:
        case "Równanie 1":
            print("R1")
        case "Równanie 2":
            print("R2")
        case "Równanie 3":
            print("R3")
        case "Równanie 4":
            print("R4")
    slider_value = slider.get()