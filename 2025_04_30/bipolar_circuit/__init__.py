""" Module permettant de représenter un circuit bipolaire

Example :

    R1 = Resistor(10)
    R2 = Resistor(5)
    L1 = Inductor(15E-6)
    C1 = Capacitor(10E-6)
    circuit = (C1|L1|R1) + R2

"""

from .device import Resistor, Capacitor, Inductor

