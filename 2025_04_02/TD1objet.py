# # Ex1

import math
import numbers

class Vecteur3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f'Vecteur3D({self.x}, {self.y}, {self.z})'
        
    def norme(self):
    	return math.sqrt(self.x**2+self.y**2+self.z**2)
    	
    def __add__(self,other):
    	return Vecteur3D(self.x+other.x, self.y+other.y, self.z+other.z)
    	
    def __mul__(self,other):
    	if isinstance(other, Vecteur3D):
    		return self.x*other.x + self.y*other.y + self.z*other.z
    	elif isinstance(other, numbers.Number):
    		return Vecteur3D(self.x*other, self.y*other, self.z*other)
    	return NotImplemented
    
    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self*other
        return NotImplemented

v1 = Vecteur3D(.2, 3, 5)
v1.norme()

# +
v1 = Vecteur3D(.2, 3, 5)
v2 = Vecteur3D(.3, 1, 8)

v1+v2
# -

2*v1





# #Ex2

# +
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
    
    def __repr__(self):
        return f'Livre({self.titre!r}, {self.auteur!r}, {self.annee!r})'
    
    def __str__(self):
        return f'{self.auteur} ({self.annee}) - {self.titre}'

    def auteur_nom(self):
        return self.auteur.split()[-1]
    
    def cle(self):
        auteur_nom = self.auteur_nom()
        return f'{auteur_nom}{self.annee}'
    
    def to_latex(self):
        return f"\\bibitem{{{self.cle()}}}\n{self.auteur} ({self.annee}) \\emph{{{self.titre}}}\n"
    
def make_livre_from_dct(dct):
    return Livre(titre=dct['titre'], auteur=dct['auteur'], annee=dct['annee'])


# +
livre1 = Livre("A very nice book", "F. Dupont", 2014)
livre2 = Livre("A very smart book", "A. Einstein", 1923)
livre3 = Livre("A very stupid comic", "D. Duck", 1937)

print(livre1)
livre1
# -

make_livre_from_dct(livre1.__dict__)

print(livre1.to_latex())

# +
import json

class Bibliographie :
    def __init__(self, livres=None):
        if isinstance(livres, list):
            livres = set(livres)
        if livres :
            self.livres = livres
        else :
            self.livres = set()
            
    def append(self, other):
        self.livres |= {other}
        
    def __add__(self, other):
        if isinstance(other, Bibliographie):
            return Bibliographie(self.livres | other.livres)
        return NotImplemented
        
    def __repr__(self):
        return f"Bibliographie({self.livres!r})"
    
    def save_to_json(self, filename):
        data = [livre.__dict__ for livre in self.livres]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

#    def load_from_jason :

    
    def filter_by_year (self,annee):
        return Bibliographie([livre for livre in self.livres if livre.annee==annee])
        
    def to_latex(self):
        out = []
        out.append(r"\begin{thebibliography}{9}")
        for livre in self.livres:
            out.append(livre.to_latex())
        out.append("\end{thebibliography}")
        return '\n'.join(out)
#        return "\\begin{thebibliography}{9} \n" + "\n".join(livre.to_latex() for livre in self.livres) + "\n \\end{thebibliography}"

    def to_latex(self):
        liste_livres = "\n".join(livre.to_latex() for livre in self.livres) 
        return rf"""\begin{{thebibliography}}{{9}}
{liste_livres}
\end{{thebibliography}}"""

    
def make_bibliographie_from_list(list_of_dict):
    return Bibliographie([make_livre_from_dct(item) for item in list_of_dict])


def make_bibliographie_from_jsonfile(filename):
    with open(filename) as f:
        data = json.load(f)
    return make_bibliographie_from_list(data)
        

# -

bib = Bibliographie()
bib.append(livre1)
bib.append(livre2)

bib.save_to_json('bibliographie.json')
make_bibliographie_from_jsonfile('bibliographie.json')

print(bib.to_latex())

bib+bib


# Ex4

class BipolarCircuit(object):	
	pass

class Combination(BipolarCircuit):
	pass

class Serial(Combination) :
	pass

class Device(BipolarCircuit):
	pass

class Resistor(Device):
	pass

class Capacitor :
class Inductor :
class Parallel :


1+1

	

