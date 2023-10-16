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
        "Constructeur"
        self.premier = None
        self.nb_wagons = 0

    def est_vide(self):
        """renvoie True si ce train est vide (ne comporte aucun wagon),
        False sinon
        """
        return self.premier is None

    def donne_nb_wagons(self):
        "Renvoie le nombre de wagons de ce train"
        return self.nb_wagons

    def transporte_du(self, contenu):
        """Détermine si ce train transporte du {contenu} (une chaine de caractères).
        Renvoie True si c'est le cas, False sinon
        """
        wagon = self.premier
        while wagon is not None:
            if wagon.contenu == contenu:
                return True
            wagon = wagon.suivant
        return False

    def ajoute_wagon(self, nouveau):
        """Ajoute un wagon à la fin de ce train.
        L'argument est le wagon à ajouter
        """
        if self.est_vide():
            self.premier = nouveau
        else:
            wagon = self.premier
            while wagon.suivant is not None:
                wagon = wagon.suivant
            wagon.suivant = nouveau
        self.nb_wagons += 1

    def supprime_wagon_de(self, contenu):
        """Supprime le premier wagon de {contenu}
        Renvoie False si ce train ne contient pas de {contenu},
        True si la suppression est effectuée
        """
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
            if wagon is None:   # pas de "contenu" dans le train
                return False
        precedent.suivant = wagon.suivant
        # MAJ du nombre de wagons et résultat de la fonction
        self.nb_wagons -= 1
        return True

    def __repr__(self):
        "Affichage dans la console"
        contenus_wagons = ['']
        wagon = self.premier
        while wagon is not None:
            contenus_wagons.append(str(wagon))
            wagon = wagon.suivant
        return "Locomotive" + " - ".join(contenus_wagons)

    def __str__(self):
        "Conversion en string"
        return self.__repr__()
