from tkinter import *

#A SUPPRIMER
#GENERATION D'UN FAKE LABYRINTHE
import random
lab = [[random.randint(0, 1) for i in range(0, 11)] for i in range(0, 11)]
maxX = 10
maxY = 10
#FAKE PERSONNAGE
persoPosX = 5
persoPosY = 5
#############"

class GameScreen(Canvas) :
    def __init__(self, mainFrame) :
        Canvas.__init__(self, mainFrame, bg="ivory", width=800, height=450)

    def noGame(self) :
        """Configure l'affichage lorsque aucun labyrinthe n'est lancé"""
        ###METTRE UNE IMAGE "DUNGEON AND PYTHON"
        coord = 1, 1, 800, 450, 1, 450, 800, 1, 1, 1
        self.create_line(coord, fill="red")

    def topView(self) :
        """Configure l'affichage en mode vue du dessus"""
        tileSol = PhotoImage(file="../img/tile_sol.gif")
        tileVide = PhotoImage(file="../img/tile_vide.gif")
        persoImg = PhotoImage(file="../img/personnage.gif")
        
        #Calcul des ecarts
        largeurFenetre = 800
        hauteurFenetre = 450
        ecartHorizontal = (largeurFenetre - (maxX*16))/2
        ecartVertical = (hauteurFenetre - (maxY*16))/2
        
        #Dessin du lab
        compteurX = 0
        compteurY = 0
        for liste in lab :
            compteurX = 0
            for element in liste :
                if element == 0 :
                    self.create_image(ecartHorizontal + compteurX*16, ecartVertical + compteurY*16, anchor=NE, image=tileSol)
                elif element == 1 :
                    self.create_image(ecartHorizontal + compteurX*16, ecartVertical + compteurY*16, anchor=NE, image=tileVide)
                compteurX += 1
            compteurY += 1

        #Dessin du personnage
        self.create_image(ecartHorizontal + persoPosX*16 + 4, ecartVertical + persoPosY*16 - 16, anchor=NE, image=persoImg)

        mainloop()

    def fpsView(self) :
        """Configure l'affichage en mode FPS"""
        pass
