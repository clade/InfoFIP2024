import dataclasses
from math import pi

from .core import Device


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

