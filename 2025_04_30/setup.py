from setuptools import setup

__version__ = "0.1"

long_description=""" Module permettant de représenter un circuit bipolaire

Example :

    R1 = Resistor(10)
    R2 = Resistor(5)
    L1 = Inductor(15E-6)
    C1 = Capacitor(10E-6)
    circuit = (C1|L1|R1) + R2

"""

setup(name='bipolar_circuit',
      version=__version__,
      description='Constantes fondamentales',
      long_description=long_description,
      author='François Pignon',
      author_email='francois.pignon@trucmuch.fr',
      url='',
      packages=['bipolar_circuit'],
     )
