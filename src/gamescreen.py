#!/usr/bin/env python3
from tkinter import *

class GameScreen(Canvas) :

    def __init__(self, mainFrame) :
        Canvas.__init__(self, mainFrame, bg="ivory", width=800, height=450)
        self.mainFrame = mainFrame

    def no_game(self) :
        """Configure l'affichage lorsque aucun labyrinthe n'est lancé"""
        ###METTRE UNE IMAGE "DUNGEON AND PYTHON"
        coord = 1, 1, 800, 450, 1, 450, 800, 1, 1, 1
        self.create_line(coord, fill="red")

    def top_view(self, game) :
        ##Recupération des composants du jeu
        lab = game.game_labyrinth.labyrinth
        labWidth = game.game_labyrinth.width_on_odd_line + 1
        labHeight = game.game_labyrinth.height
        player_position = game.player_position
        
        ##Debut de la construction du canevas
        #Dessin de fond
        self.create_rectangle(0,0, 801, 451, fill="ivory")

        #Dessin du labyrinthe
        """Configure l'affichage en mode vue du dessus"""
        tileSol = PhotoImage(file="../img/tile_sol.gif")
        tileVide = PhotoImage(file="../img/tile_vide.gif")
        persoImg = PhotoImage(file="../img/personnage.gif")

        #Calcul des ecarts
        #Ecart = (Taille de l'écran - (taille d'un tiles * 2)*nb de case du labyrinte /2
        ecartHorizontal = (800 - 16*2*(labWidth+1))/2
        ecartVertical = (450 - 16*(labHeight+1))/2

        #Dessin du labyrinthe
        #Pour le dessin du labyrinthe, on utilise des carre de 2 tiles de longueur et 2 tiles de hauteur.
        #Le tile Haut-Gauche est toujours du mur (par soucis esthetique), le tile Bas-Droit est la case contenant le personnage, il contient donc toujours du sol
        #Les tiles Haut-Droit et Bas-Gauche represente si il y a ou non un mur horizontal (Haut-Droit) ou un mur vertical (Bas-Gauche)
        compteurX, compteurY = 0,0
        #Parcours vertical
        while compteurY <= labHeight - 2 :
            #Parcours horizontal
            compteurX = 0
            while(compteurX <= labWidth - 2) :
                #Horizontal : 0
                if(lab[compteurY][compteurX] == "0") :
                    #Vertical : 0
                    if(lab[compteurY+1][compteurX] == "0") :
                        #Gestion du cas où un mur est présent en haut ainsi qu'à gauche
                        caseDH=tileSol
                        caseGB=tileSol
                    #Vertical : 1
                    if(lab[compteurY+1][compteurX] == "1") :
                        caseDH=tileSol
                        caseGB=tileVide
                #Horizontal : 1
                elif(lab[compteurY][compteurX] == "1") :
                    #Vertical : 0
                    if(lab[compteurY+1][compteurX] == "0") :
                        caseDH=tileVide
                        caseGB=tileSol

                    #Vertical : 1
                    if(lab[compteurY+1][compteurX] == "1") :
                        caseDH=tileVide
                        caseGB=tileVide

                #AFFICHAGE DU  TRUC
                caseGH=tileVide
                caseDB=tileSol
                self.create_image(ecartHorizontal+(compteurX*2*16), ecartVertical+(compteurY*16), anchor=NW, image=caseGH)
                self.create_image(ecartHorizontal+(compteurX*2*16) +16, ecartVertical+(compteurY*16), anchor=NW, image=caseDH)
                self.create_image(ecartHorizontal+(compteurX*2*16), ecartVertical+(compteurY*16) + 16, anchor=NW, image=caseGB)
                self.create_image(ecartHorizontal+(compteurX*2*16) +16, ecartVertical+(compteurY*16) + 16, anchor=NW, image=caseDB)
                
                #Incrementation de X
                compteurX += 1
            #Incrementation Y
                
            compteurY += 2
        #Dessin des bords droit et bas
        i,j=0,1
        #Bord bas
        while i <= labWidth - 2 :
            if(lab[labHeight][i] == "1") :
                caseGH = tileVide
                caseDH = tileVide
            elif(lab[labHeight][i] == "E") :
                caseGH = tileVide
                caseDH = tileSol
            else :
                caseGH = tileVide
                caseDH = tileSol
            self.create_image(ecartHorizontal+(i*2*16), ecartVertical+(labHeight*16), anchor=NW, image=caseGH)
            self.create_image(ecartHorizontal+(i*2*16) +16, ecartVertical+(labHeight*16), anchor=NW, image=caseDH)
            i += 1
        #Bord droit
        while j<= labHeight - 1 :
            if(lab[j][labWidth - 1] == "1") :
                caseGH = tileVide
                caseGB = tileVide
            elif(lab[j][labWidth - 1] == "E") :
                caseGH = tileVide
                caseGB = tileSol
            else :
                caseGH = tileSol
                caseGB = tileSol
            self.create_image(ecartHorizontal + (labWidth - 1)*2*16, ecartVertical+(j-1)*16, anchor=NW, image=caseGH)
            self.create_image(ecartHorizontal + (labWidth - 1)*2*16, ecartVertical+(j*16), anchor=NW, image=caseGB)
            j += 2
        #Puis la case en bas à droite
            self.create_image(ecartHorizontal + (labWidth-1)*2*16, ecartVertical+(labHeight*16), anchor=NW, image=tileVide)

        #Dessin du personnage
        perso = PhotoImage(file="../img/personnage.gif")
        print(player_position)
        perso_positionXCanvas = ecartHorizontal+(player_position[1])*32
        perso_positionYCanvas = ecartVertical + player_position[0]*16 - 16
        self.create_image(perso_positionXCanvas, perso_positionYCanvas, anchor=NW, image=perso)
        mainloop()

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


        mainloop()
