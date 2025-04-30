import unittest

from bipolar_circuit import Resistor, Inductor, Capacitor

class TestBipolar(unittest.TestCase):
    def test_resisistor(self):
        R1 = Resistor(10)
        s = R1.__str__()    
        self.assertEqual(R1.impedance(10000), 10)
    
    def test_serie(self):
        R1 = Resistor(10)
        R2 = Resistor(20)
        self.assertEqual((R1+R2).impedance(10), 30)
