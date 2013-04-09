#!/usr/bin/env python3
from tkinter import *

class GameScreen(Canvas) :
    def __init__(self, mainFrame) :
        Canvas.__init__(self, mainFrame, bg="ivory", width=800, height=450)
        self.mainFrame = mainFrame
        self.mode = "no_game"

    def no_game(self) :
        """Configure l'affichage lorsque aucun labyrinthe n'est lancé"""
        ###METTRE UNE IMAGE "DUNGEON AND PYTHON"
        self.mode = "no_game"
        coord = 1, 1, 800, 450, 1, 450, 800, 1, 1, 1
        self.create_line(coord, fill="red")

    def init_top_view(self, *arg) :
        ##Recupération des composants du jeu
        self.mode = "top_view"
        self.lab = self.mainFrame.game.game_labyrinth.labyrinth
        self.labWidth = self.mainFrame.game.game_labyrinth.width_on_odd_line + 1
        self.labHeight = self.mainFrame.game.game_labyrinth.height
        ###Initialisation des images
        self.tileSolIMG = PhotoImage(file="../img/tile_sol.gif")
        self.tileVideIMG = PhotoImage(file="../img/tile_vide.gif")
        self.persoIMG = PhotoImage(file="../img/personnage.gif")

    def draw(self, *arg) :
        if self.mode == "top_view" :
            self.draw_top_view()
    
    def draw_top_view(self) :        
        lab = self.lab
        labWidth = self.labWidth
        labHeight = self.labHeight
        player_position = self.mainFrame.game.player_position
        tileSol = self.tileSolIMG
        tileVide= self.tileVideIMG
        perso = self.persoIMG
        
        ##Debut de la construction du canevas
        #On efface le contenu du canevas
        self.delete("all")
        #Dessin de fond
        self.create_rectangle(0,0, 801, 451, fill="ivory")

        #Dessin du labyrinthe
        """Configure l'affichage en mode vue du dessus"""

        #Calcul des ecarts
        #Ecart = (Taille de l'écran - (taille d'un tiles * 2)*nb de case du labyrinte /2
        ecartHorizontal = (800 - 16*2*(labWidth) + 16)/2
        ecartVertical = (450 - 16*(labHeight+1))/2

        #Dessin du labyrinthe
        #Pour le dessin du labyrinthe, on utilise des carre de 2 tiles de longueur et 2 tiles de hauteur.
        #Le tile Haut-Gauche est toujours du mur (par soucis esthetique), le tile Bas-Droit est la case contenant le personnage, il contient donc toujours du sol
        #Les tiles Haut-Droit et Bas-Gauche represente si il y a ou non un mur horizontal (Haut-Droit) ou un mur vertical (Bas-Gauche)    
        caseGH=tileVide
        caseDB=tileSol
        #Initialisation de GB et DH, juste pour eviter une erreur d'execution
        caseGB=tileVide
        caseDH=tileVide
        #On parcourt les lignes Vertical dans lesquelles ont lis directement les valeurs
        for y,ligneVerticale in enumerate([ligneVerticale for y, ligneVerticale in enumerate(lab) if y%2==1]) :
            for x, val in enumerate([val for val in ligneVerticale]) :
                #Case DroiteHaut
                if x != labWidth - 1 :
                    if lab[y*2][x] == "1" :
                        caseDH = tileVide
                    else :
                        caseDH = tileSol
                #Case GaucheBas
                #val est la valeur de la ligne des murs verticaux
                if(val == "1") :
                    caseGB = tileVide
                else :
                    caseGB = tileSol
                #Dessin des 4 case, avec le cas ou on est a la derniere case :
                if x != labWidth - 1 :
                    self.drawTile(caseGH, caseDH, caseGB, caseDB, ecartHorizontal, ecartVertical, x, y)
                else :
                    self.drawTile(caseGH, "", caseGB, "", ecartHorizontal, ecartVertical, x, y)
        #On parcourt la derniere ligne de lab, contenant le mur horizontal
        for x, val in enumerate(lab[labHeight]) :
            if val == "1" :
                self.drawTile(tileVide, tileVide, "", "", ecartHorizontal, ecartVertical, x, (labHeight)/2)
            elif val == "E" :
                self.drawTile(tileVide, tileSol, "", "", ecartHorizontal, ecartVertical, x, (labHeight)/2)
            else :
                self.drawTile(tileVide, tileSol, "", "", ecartHorizontal, ecartVertical, x, (labHeight)/2)
        #Dessin du bord DroitBas
        self.drawTile(tileVide, "", "", "", ecartHorizontal, ecartVertical, labWidth - 1, (labHeight)/2)
        
        #Dessin du personnage
        perso_positionXCanvas = ecartHorizontal+(player_position[1])*32
        perso_positionYCanvas = ecartVertical + player_position[0]*16 - 16
        self.create_image(perso_positionXCanvas, perso_positionYCanvas, anchor=NW, image=perso)
        #On dessin la fenetre
        self.mainloop()

    def drawTile(self, caseGH, caseDH, caseGB, caseDB, ecartHorizontal, ecartVertical, x, y) :
        #Dessin des cases
        if caseGH != "" :
            self.create_image(ecartHorizontal+(x*2*16), ecartVertical+(y*2*16), anchor=NW, image=caseGH)
        if caseDH != "" :
            self.create_image(ecartHorizontal+(x*2*16) +16, ecartVertical+(y*2*16), anchor=NW, image=caseDH)
        if caseGB != "" :
            self.create_image(ecartHorizontal+(x*2*16), ecartVertical+(y*2*16) + 16, anchor=NW, image=caseGB)
        if caseDB != "" :
            self.create_image(ecartHorizontal+(x*2*16) +16, ecartVertical+(y*2*16) + 16, anchor=NW, image=caseDB)
        
    def fpsView(self) :
        """Configure l'affichage en mode FPS"""
        #C'EST DU TOTAL WIP POUR TESTER
        #ON CONSIDERE POUR L'INSTANT QUE LE PERSONNAGE REGARDE VERS LE BAS
        #initialisation des images
        bg = PhotoImage(file="../img/bg.gif")
        f1 = PhotoImage(file="../img/f1.gif")
        f2 = PhotoImage(file="../img/f2.gif")
        f3 = PhotoImage(file="../img/f3.gif")
        f4 = PhotoImage(file="../img/f4.gif")
        f5 = PhotoImage(file="../img/f5.gif")
        l1 = PhotoImage(file="../img/l1.gif")
        l2 = PhotoImage(file="../img/l2.gif")
        l3 = PhotoImage(file="../img/l3.gif")
        l4 = PhotoImage(file="../img/l4.gif")
        l5 = PhotoImage(file="../img/l5.gif")
        r1 = PhotoImage(file="../img/r1.gif")
        r2 = PhotoImage(file="../img/r2.gif")
        r3 = PhotoImage(file="../img/r3.gif")
        r4 = PhotoImage(file="../img/r4.gif")
        r5 = PhotoImage(file="../img/r5.gif")
        #RENDU FPS
        self.create_image(0, 0, anchor=NW, image=bg)
        #Case en face
        if(self.lab[persoPosY+1][persoPosX] == 1) :
            self.create_image(0, 0, anchor=NW, image=f1)
        elif(self.lab[persoPosY+2][persoPosX] == 1) :
            self.create_image(0, 0, anchor=NW, image=f2)
        elif(self.lab[persoPosY+3][persoPosX] == 1) :
            self.create_image(0, 0, anchor=NW, image=f3)
        elif(self.lab[persoPosY+4][persoPosX] == 1) :
            self.create_image(0, 0, anchor=NW, image=f4)
        elif(self.lab[persoPosY+5][persoPosX] == 1) :
            self.create_image(0, 0, anchor=NW, image=f5)
        #Case a gauce
        if(self.lab[persoPosY+1][persoPosX-1] == 1) :
            self.create_image(0, 0, anchor=NW, image=l1)
        if(self.lab[persoPosY+2][persoPosX-1] == 1) :
            self.create_image(0, 0, anchor=NW, image=l2)
        if(self.lab[persoPosY+3][persoPosX-1] == 1) :
            self.create_image(0, 0, anchor=NW, image=l3)
        if(self.lab[persoPosY+4][persoPosX-1] == 1) :
            self.create_image(0, 0, anchor=NW, image=l4)
        if(self.lab[persoPosY+5][persoPosX-1] == 1) :
            self.create_image(0, 0, anchor=NW, image=l5)
        #Case a droite
        if(self.lab[persoPosY+1][persoPosX+1] == 1) :
            self.create_image(0, 0, anchor=NW, image=r1)
        if(self.lab[persoPosY+2][persoPosX+1] == 1) :
            self.create_image(0, 0, anchor=NW, image=r2)
        if(self.lab[persoPosY+3][persoPosX+1] == 1) :
            self.create_image(0, 0, anchor=NW, image=r3)
        if(self.lab[persoPosY+4][persoPosX+1] == 1) :
            self.create_image(0, 0, anchor=NW, image=r4)
        if(self.lab[persoPosY+5][persoPosX+1] == 1) :
            self.create_image(0, 0, anchor=NW, image=r5)
