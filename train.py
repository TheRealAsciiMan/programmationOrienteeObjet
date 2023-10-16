class Wagon:
    def __init__(self, contenu):
        "Constructeur"
        self.contenu = contenu
        self.suivant = None
    def __repr__(self):
        "Affichage dans la console"
        return f'Wagon de {self.contenu}'
    def __str__(self):
        "Conversion en string"
        return self.__repr__()

foodWagon = Wagon("Food")


class Train:
    def __init__(self):
        self.premier = None
        self.nb_wagons = 0

    def est_vide(self):
        return self.premier is None

    def donne_nb_wagons(self):
        return self.nb_wagons

    def transporte_du(self, contenu):
        wagon = self.premier
        while wagon is not None:
            if wagon.contenu == contenu:
                return True
            wagon = wagon.suivant
        return False

    def ajoute_wagon(self, nouveau):
        if self.est_vide():
            self.premier = nouveau
        else:
            wagon = self.premier
            while wagon.suivant is not None:
                wagon = wagon.suivant
            wagon.suivant = nouveau
        self.nb_wagons += 1

    def supprime_wagon_de(self, contenu):
        if self.est_vide():
            return False
        if self.premier.contenu == contenu:
            self.premier = self.premier.suivant
            self.nb_wagons -= 1
            return True
        precedent = self.premier
        wagon = precedent.suivant
        while wagon.contenu != contenu:
            precedent = wagon
            wagon = wagon.suivant
            if wagon is None:
                return False
        precedent.suivant = wagon.suivant
        self.nb_wagons -= 1
        return True

    def __repr__(self):
        contenus_wagons = ['']
        wagon = self.premier
        while wagon is not None:
            contenus_wagons.append(str(wagon))
            wagon = wagon.suivant
        return "Locomotive" + " - ".join(contenus_wagons)

    def __str__(self):
        return self.__repr__()
