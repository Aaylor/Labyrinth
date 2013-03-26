#!/usr/bin/env python3

class Labyrinthe :
    """Contient "labyrinthe" : le tableau à deux dimensions représentant le labyrinthe"""
    def __init__(self, chaine) :
        """Lis la chaine de caractère chaine et construit un labyrinthe sous forme d'un tableau à deux dimensions"""
        self.labyrinthe = list()
        chaine = chaine.split("\n")
        for ligne in chaine :
            #On enleve les eventuels espaces incongrus de la chaine
            ligneLabyrinthe = list()
            for lettre in ligne :
                if lettre == "0" :
                    ligneLabyrinthe.append(0)
                elif lettre == "1" :
                    ligneLabyrinthe.append(1)
                elif lettre == "E" :
                    ligneLabyrinthe.append(2)
            self.labyrinthe.append(ligneLabyrinthe)
            
    def __str__(self) :
        chaine = ""
        for i in self.labyrinthe :
            chaine += str(i)
            chaine += "\n"
        return chaine

    def maxX(self) :
        """Retourne la largeur maximum du Labyrinthe"""
        pass

    def maxY(self) :
        """Retourne hauteur maximum du Labyrinthe"""
        pass
