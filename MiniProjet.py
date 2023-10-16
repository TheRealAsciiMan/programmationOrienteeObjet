from math import sqrt

class Vecteur2D:
    def __int__(self, x ,y):
        self.x = x
        self.y = y
    def Norme(self):
        return sqrt(x**2 + y**2)
    def Multiplie(self, fact):
        self.x = x*fact
        self.y = y*fact
