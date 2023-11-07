from math import sqrt

class Vecteur2D:
    def __init__(self, x:float ,y:float):
        self.x = x
        self.y = y
    def Norme(self):
        return sqrt(self.x**2 + self.y**2)
    def Multiplie(self, fact:float):
        assert isinstance(fact, (int, float)), "Le facteur doit être un nombre"
        self.x *= fact
        self.y *= fact
        return Vecteur2D(self.x,self.y)

    def Ajoute(self, vect):
        assert isinstance(vect, Vecteur2D), "L'argument doit être un Vecteur2D"
        self.x += vect.x
        self.y += vect.y
        return Vecteur2D(self.x,self.y)


    def ProduitScalaire(self, vect):
        assert isinstance(vect, Vecteur2D), "L'argument doit être un Vecteur2D"
        proscal = self.x * vect.x + self.y * vect.y
        return proscal

    def EstPerpendiculaire(self, vect):
        assert isinstance(vect, Vecteur2D), "L'argument doit être un Vecteur2D"
        if self.ProduitScalaire(vect) == 0:
            return True
        else:
            return False

    def EstColinéaire(self, vect):
        assert isinstance(vect, Vecteur2D), "L'argument doit être un Vecteur2D"
        if self.x * vect.y - vect.x * self.y == 0:
            return True
        else:
            return False

    def __str__(self):
        return f"vecteur de coordonnées : x={self.x} et y={self.y}"

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return self.Multiplie(other)
        if isinstance(other,Vecteur2D):
            return self.ProduitScalaire(other)
        else:
            return self

    def __add__(self, other):
        if isinstance(other,Vecteur2D):
            return self.Ajoute(other)
        else:
            return self



# Test de création d'un vecteur
v1 = Vecteur2D(3, 4)
assert v1.x == 3
assert v1.y == 4

# Test de calcul de la norme
assert v1.Norme() == 5

# Test de multiplication par un facteur
v1.Multiplie(2)
assert v1.x == 6
assert v1.y == 8

# Test d'addition de vecteurs
v2 = Vecteur2D(1, 2)
v1.Ajoute(v2)
assert v1.x == 7
assert v1.y == 10

# Test de produit scalaire
v3 = Vecteur2D(2, 3)
assert v1.ProduitScalaire(v3) == 44

# Test d'orthogonalité
v4 = Vecteur2D(4, -3)
assert v1.EstPerpendiculaire(v4) == False

# Test de colinéarité
v5 = Vecteur2D(14, 20)
assert v1.EstColinéaire(v5) == True

# Test de multiplication de vecteur par un facteur avec opérateur *
v6 = v1 * 3
assert v6.x == 21
assert v6.y == 30

# Test d'addition de vecteurs avec opérateur +
v7 = (v1 + v2)
assert v7.x == 22
assert v7.y == 32



