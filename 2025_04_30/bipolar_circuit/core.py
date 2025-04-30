import dataclasses

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

