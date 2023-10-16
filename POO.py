class voiture:
    """
    Permet de créer une voiture avec différements attributs : matiere, km, couleur.
    """
    matiere="acier"
    km=0
    def __init__(self, color="red"):
        """
        Choisit la couleur
        :param color: par défaut red
        """
        self.couleur = color
    def parcours(self, dist):
        """
        rajoute la distance à km
        :param dist: les distance int
        """
        self.km+=dist
    def estNeuve(self):
        """
        vérifie si la voiture est neuve
        :return: True ou False
        """
        if self.km==0:
            return True
        else:
            return False

    def changerCouleur(self, color):
        """
        Permet de changer la couleur
        :param color:
        self.couler = color
        """


c0 = voiture("red")
print(c0.estNeuve())
c0.parcours(55)
print(c0.couleur, c0.km)
print(c0.estNeuve())