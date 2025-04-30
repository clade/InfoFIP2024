""" Module permettant de représenter un circuit bipolaire

Example :

    R1 = Resistor(10)
    R2 = Resistor(5)
    L1 = Inductor(15E-6)
    C1 = Capacitor(10E-6)
    circuit = (C1|L1|R1) + R2

"""

import dataclasses
from math import pi

class BipolarCircuit(object):
    def __add__(self, other):
        if not isinstance(other, BipolarCircuit):
            return NotImplemented
        return Serial(self, other)
    
    def __or__(self, other):
        if not isinstance(other, BipolarCircuit):
            return NotImplemented
        return Parallel(self, other)
        
class Combination(BipolarCircuit):
    pass
    
@dataclasses.dataclass
class Serial(Combination) :
    arg1 : BipolarCircuit
    arg2 : BipolarCircuit
    
    def __str__(self):
        return f"({self.arg1!s} + {self.arg2!s})"
    
    def impedance(self, frequence):
        return (self.arg1.impedance(frequence) 
                + self.arg2.impedance(frequence))
    
@dataclasses.dataclass
class Parallel(Combination) :
    arg1 : BipolarCircuit
    arg2 : BipolarCircuit
    
    def __str__(self):
        return f"({self.arg1!s} | {self.arg2!s})"

    def impedance(self, frequence):
        return 1/(1/self.arg1.impedance(frequence) 
                + 1/self.arg2.impedance(frequence))
    


@dataclasses.dataclass
class Device(BipolarCircuit):
    value : float
    

class Resistor(Device):
    """ Représente une résistance 
    
    Example : 
        r = Resistor(50)
    """
    def __str__(self):
        return f'{self.value}Ω'

    def impedance(self, frequence):
        return self.value
    
@dataclasses.dataclass
class Capacitor(Device):
    value : float

    def __str__(self):
        val = self.value
        if val>1:
            return f'{self.value}F'
        if val>1E-3:
            return f'{self.value*1000}mF'
        if val>1E-6:
            return f'{self.value*1E6}μF'

    def impedance(self, frequence):
        return 1/(1J*self.value*2*pi*frequence)

        
@dataclasses.dataclass
class Inductor(Device):
    value : float
        
    def __str__(self):
        return f'{self.value}H'
        
    def impedance(self, frequence):
        return 1J*self.value*2*pi*frequence
        

