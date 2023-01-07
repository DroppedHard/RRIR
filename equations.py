import math

# (shooting_method parameters tuple, gui string, exact solution)
equations = [
    ((lambda x,y,yprime : 5*yprime - 6*y, 0, 1, 1, math.e**2), "y\'\'=5y\'-6y", lambda x : math.e**(2*x)),
    ((lambda x,y,yprime : 2, 0, 10, 0, 0), "y\'\'=2", x**2 - 10*x),
    ((lambda x,y,yprime : -8*math.sin(x)*math.cos(x), 0, math.pi, 0, 0), "y\'\'=-8sin(x)cos(x)", lambda x: math.sin(2*x)),
    ((lambda x,y,yprime : math.e**x - 6*x**2*math.sin(x) + x**3*math.cos(x) - 6*x*math.cos(x), 0, math.pi, 0, 0), "y\'\'=e^x-6x^2sin(x)+x^3cos(x)-6xcos(x)", lambda x: math.e**x - math.cos(x)*x**3)
]