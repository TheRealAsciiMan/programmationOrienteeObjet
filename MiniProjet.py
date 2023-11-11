from math import sqrt


class Vecteur2D:
    """Classe pour représenter un vecteur 2D."""

    def __init__(self, x: float, y: float):
        """Initialise un vecteur 2D avec des coordonnées x et y.

        Args:
            x (float): Coordonnée x du vecteur.
            y (float): Coordonnée y du vecteur.
        """
        self.x = x
        self.y = y

    def Norme(self):
        """Calcule la norme du vecteur.

        Returns:
            float: La norme du vecteur.
        """
        return sqrt(self.x**2 + self.y**2)

    def Multiplie(self, fact: float):
        """Multiplie le vecteur par un facteur.

        Args:
            fact (float): Le facteur de multiplication.

        Returns:
            Vecteur2D: Un nouveau vecteur résultant de la multiplication.
        """
        assert isinstance(fact, (int, float)), "Le facteur doit être un nombre"
        self.x *= fact
        self.y *= fact
        return Vecteur2D(self.x, self.y)

    def Ajoute(self, vect):
        """Additionne ce vecteur avec un autre vecteur.

        Args:
            vect (Vecteur2D): Le vecteur à ajouter.

        Returns:
            Vecteur2D: Un nouveau vecteur résultant de l'addition.
        """
        assert isinstance(vect, Vecteur2D), "L'argument vect doit être un Vecteur2D"
        self.x += vect.x
        self.y += vect.y
        return Vecteur2D(self.x, self.y)

    def ProduitScalaire(self, vect):
        """Calcule le produit scalaire entre ce vecteur et un autre vecteur.

        Args:
            vect (Vecteur2D): Le vecteur pour le produit scalaire.

        Returns:
            float: Le produit scalaire des deux vecteurs.
        """
        assert isinstance(vect, Vecteur2D), "L'argument vect doit être un Vecteur2D"
        return self.x * vect.x + self.y * vect.y

    def EstPerpendiculaire(self, vect):
        """Vérifie si ce vecteur est perpendiculaire à un autre vecteur.

        Args:
            vect (Vecteur2D): Le vecteur à comparer.

        Returns:
            bool: True si les vecteurs sont perpendiculaires, sinon False.
        """
        assert isinstance(vect, Vecteur2D), "L'argument vect doit être un Vecteur2D"
        if self.ProduitScalaire(vect) == 0:
            return True
        else:
            return False

    def EstColinéaire(self, vect):
        """Vérifie si ce vecteur est colinéaire à un autre vecteur.

        Args:
            vect (Vecteur2D): Le vecteur à comparer.

        Returns:
            bool: True si les vecteurs sont colinéaires, sinon False.
        """
        assert isinstance(vect, Vecteur2D), "L'argument vect doit être un Vecteur2D"
        if self.x * vect.y - vect.x * self.y == 0:
            return True
        else:
            return False

    def __str__(self):
        """Renvoie une représentation sous forme de chaîne du vecteur.

        Returns:
            str: Une chaîne de caractères représentant le vecteur.
        """
        return f"vecteur de coordonnées : x={self.x} et y={self.y}"

    def __mul__(self, other):
        """Redéfinition de l'opérateur de multiplication.

        Args:
            other (int, float, Vecteur2D): L'opérande à multiplier.

        Returns:
            Vecteur2D or float: Le résultat de la multiplication.
        """
        if isinstance(other, (int, float)):
            return self.Multiplie(other)
        if isinstance(other, Vecteur2D):
            return self.ProduitScalaire(other)
        else:
            return self

    def __add__(self, other):
        """Redéfinition de l'opérateur d'addition.

        Args:
            other (Vecteur2D): Le vecteur à ajouter.

        Returns:
            Vecteur2D: Le résultat de l'addition.
        """
        if isinstance(other, Vecteur2D):
            return self.Ajoute(other)
        else:
            return self


def test_vecteur2d():
    # Test du constructeur
    v = Vecteur2D(3.0, 4.0)
    assert v.x == 3.0
    assert v.y == 4.0

    # Test de la méthode Norme
    v = Vecteur2D(3.0, 4.0)
    assert v.Norme() == 5.0

    # Test de la méthode Multiplie
    v = Vecteur2D(3.0, 4.0)
    v2 = v.Multiplie(2.0)
    assert v2.x == 6.0
    assert v2.y == 8.0

    # Test de la méthode Ajoute
    v = Vecteur2D(3.0, 4.0)
    v2 = Vecteur2D(1.0, 2.0)
    v3 = v.Ajoute(v2)
    assert v3.x == 4.0
    assert v3.y == 6.0

    # Test de la méthode ProduitScalaire
    v = Vecteur2D(3.0, 4.0)
    v2 = Vecteur2D(1.0, 2.0)
    produit = v.ProduitScalaire(v2)
    assert produit == 11.0

    # Test de la méthode EstPerpendiculaire
    v = Vecteur2D(3.0, 4.0)
    v2 = Vecteur2D(-4.0, 3.0)
    assert v.EstPerpendiculaire(v2)

    # Test de la méthode EstColinéaire
    v = Vecteur2D(3.0, 4.0)
    v2 = Vecteur2D(6.0, 8.0)
    assert v.EstColinéaire(v2)

    # Test de la multiplication d'un vecteur par un nombre avec *
    v = Vecteur2D(3.0, 4.0)
    v2 = v*5
    assert v2.x == 15
    assert v2.y == 20

    # Test de la multiplication d'un vecteur par un autre vecteur avec *
    v = Vecteur2D(3.0, 4.0)
    v2 = Vecteur2D(5.0, 3.0)
    produit = v*v2
    assert produit == 27

    # Test de l'addition d'un vecteur avec un autre vecteur avec +
    v = Vecteur2D(3.0, 4.0)
    v2 = Vecteur2D(5.0, 3.0)
    somme = v + v2
    assert somme.x == 8
    assert somme.y == 7


# Exécution des tests
test_vecteur2d()
