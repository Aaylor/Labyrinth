#!/usr/bin/env python3
from tkinter import *

class GameScreen(Canvas) :
	def __init__(self, mainFrame) :
		Canvas.__init__(self, mainFrame, bg="ivory", width=800, height=450)
		self.mainframe = mainFrame
		self.mode = "no_game"
		self.display_path = False
		self.display_solution = False

	def no_game(self) :
		"""Configure l'affichage lorsque aucun labyrinthe n'est lancé"""
		###METTRE UNE IMAGE "DUNGEON AND PYTHON"
		self.mode = "no_game"
		self.ecran_titre = PhotoImage(file="../img/ecran_titre.gif")
		self.create_image(0, 0, anchor=NW, image=self.ecran_titre)

	def init_top_view(self, *arg) :
		##Recupération des composants du jeu
		self.mode = "top_view"
		self.lab = self.mainframe.game.game_labyrinth.labyrinth
		self.labWidth = self.mainframe.game.game_labyrinth.width_on_odd_line + 1
		self.labHeight = self.mainframe.game.game_labyrinth.height
		###Initialisation des images
		self.tileSolIMG = PhotoImage(file="../img/tile_sol.gif")
		self.tileVideIMG = PhotoImage(file="../img/tile_vide.gif")
		self.perso_up = PhotoImage(file="../img/personnage-haut.gif")
		self.perso_down = PhotoImage(file="../img/personnage-bas.gif")
		self.perso_left = PhotoImage(file="../img/personnage-gauche.gif")
		self.perso_right = PhotoImage(file="../img/personnage-droit.gif")
		self.path_right = PhotoImage(file="../img/path-right.gif")
		self.path_up = PhotoImage(file="../img/path-up.gif")
		self.path_down = PhotoImage(file="../img/path-down.gif")
		self.path_left = PhotoImage(file="../img/path-left.gif")

	def init_fps_view(self, *arg) :
		##Recupération des composants du jeu
		self.mode = "fps_view"
		self.lab = self.mainframe.game.game_labyrinth.labyrinth
		self.labWidth = self.mainframe.game.game_labyrinth.width_on_odd_line + 1
		self.labHeight = self.mainframe.game.game_labyrinth.height
		self.bg = PhotoImage(file="../img/background.gif")
		self.f1 = PhotoImage(file="../img/f1.gif")
		self.f2 = PhotoImage(file="../img/f2.gif")
		self.f3 = PhotoImage(file="../img/f3.gif")
		self.f4 = PhotoImage(file="../img/f4.gif")
		self.l1 = PhotoImage(file="../img/l1.gif")
		self.l2 = PhotoImage(file="../img/l2.gif")
		self.l3 = PhotoImage(file="../img/l3.gif")
		self.l4 = PhotoImage(file="../img/l4.gif")
		self.l5 = PhotoImage(file="../img/l5.gif")
		self.r1 = PhotoImage(file="../img/r1.gif")
		self.r2 = PhotoImage(file="../img/r2.gif")
		self.r3 = PhotoImage(file="../img/r3.gif")
		self.r4 = PhotoImage(file="../img/r4.gif")
		self.r5 = PhotoImage(file="../img/r5.gif")
		self.f1_end = PhotoImage(file="../img/f1_end.gif")
		self.f2_end = PhotoImage(file="../img/f2_end.gif")
		self.f3_end = PhotoImage(file="../img/f3_end.gif")
		self.f4_end = PhotoImage(file="../img/f4_end.gif")

	def draw(self, *arg) :
		if self.mode == "top_view" :
			self.draw_top_view()
		elif self.mode == "fps_view" :
			self.draw_fps_view()
	
	def draw_top_view(self) : 
		lab = self.lab
		labWidth = self.labWidth
		labHeight = self.labHeight
		player_position = self.mainframe.game.player_position
		tileSol = self.tileSolIMG
		tileVide= self.tileVideIMG
		direction = self.mainframe.game.player.direction #direction du personnage
		if direction == "h" :
			perso = self.perso_up
		elif direction =="b" :
			perso = self.perso_down
		elif direction =="g" :
			perso = self.perso_left
		else :
			perso = self.perso_right
			
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
					if lab[y*2][x][0] == "1" :
						caseDH = tileVide
					else :
						caseDH = tileSol
				#Case GaucheBas
				#val est la valeur de la ligne des murs verticaux
				if(val[0] == "1") :
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
			if val[0] == "1" :
				self.drawTile(tileVide, tileVide, "", "", ecartHorizontal, ecartVertical, x, (labHeight)/2)
			else :
				self.drawTile(tileVide, tileSol, "", "", ecartHorizontal, ecartVertical, x, (labHeight)/2)
		#Dessin du bord DroitBas
		self.drawTile(tileVide, "", "", "", ecartHorizontal, ecartVertical, labWidth - 1, (labHeight)/2)
		
		#Dessin du chemin parcouru
		if self.display_path == True :
			self.draw_path_top_view(self.mainframe.game.path_of_the_player, ecartHorizontal, ecartVertical)
		
		#Dessin de la solution
		if self.display_solution == True :
			self.mainframe.game.give_solution()
			self.draw_path_top_view(self.mainframe.game.way_list, ecartHorizontal, ecartVertical)
			
		#Dessin du personnage
		if(player_position[1] == labWidth-1) :
			ajustementX = -16
		else :
			ajustementX = 0
		perso_positionXCanvas = ecartHorizontal+(player_position[1])*32 + ajustementX
		perso_positionYCanvas = ecartVertical + player_position[0]*16 - 16
		self.create_image(perso_positionXCanvas, perso_positionYCanvas, anchor=NW, image=perso)
		
		#On dessin la fenetre
		self.update()

	def drawTile(self, caseGH, caseDH, caseGB, caseDB, ecartHorizontal, ecartVertical, x, y) :
		"""Dessine une case des 4 tiles précisés en parametre aux coordonnées x/y en tenant compte des écart horizontaux et verticaux"""
		if caseGH != "" :
			self.create_image(ecartHorizontal+(x*2*16), ecartVertical+(y*2*16), anchor=NW, image=caseGH)
		if caseDH != "" :
			self.create_image(ecartHorizontal+(x*2*16) +16, ecartVertical+(y*2*16), anchor=NW, image=caseDH)
		if caseGB != "" :
			self.create_image(ecartHorizontal+(x*2*16), ecartVertical+(y*2*16) + 16, anchor=NW, image=caseGB)
		if caseDB != "" :
			self.create_image(ecartHorizontal+(x*2*16) +16, ecartVertical+(y*2*16) + 16, anchor=NW, image=caseDB)
			
	def draw_path_top_view(self, liste_chemin, ecartHorizontal, ecartVertical) :
		for indice, coord in enumerate(liste_chemin) :
			if coord[1] < self.labWidth - 1 : #Pour éviter que le chemin s'affiche en dehors du labyrinthe
				#On se relie à la position précédente
				if indice > 0 :
					if(liste_chemin[indice - 1][0] == coord[0]) : #Sur la même ligne
						if(liste_chemin[indice - 1][1] > coord[1]) : #Position précédente à droite
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_right, fill="red")
						else : #Position précédente à gauche
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_left)
					else : #Sur la même colone
						if(liste_chemin[indice - 1][0] > coord[0]) : #Position précédente en haut
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_down)
						else : #Position précédente à gauche
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_up)
				#On se relie à la position précédente
				if indice < len(liste_chemin) - 1 :
					if(liste_chemin[indice + 1][0] == coord[0]) : #Sur la même ligne
						if(liste_chemin[indice + 1][1] > coord[1]) : #Position suivante à droite
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_right)
						else : #Position suivante à gauche
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_left)
					else : #Sur la même colone
						if(liste_chemin[indice + 1][0] > coord[0]) : #Position suivant en haut
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_down)
						else : #Position suivante à gauche
							self.create_image(ecartHorizontal+(coord[1]*2*16), ecartVertical+(coord[0]*16) - 16, anchor=NW, image=self.path_up)
		
	def draw_fps_view(self) :
		"""Configure l'affichage en mode FPS"""
		direction = self.mainframe.game.player.direction #direction du personnage
		posX = self.mainframe.game.player_position[1] #position X du personnage
		posY = self.mainframe.game.player_position[0] #position Y du personnage
		finalPosX = self.mainframe.game.game_labyrinth.exit_position[1]
		finalPosY = self.mainframe.game.game_labyrinth.exit_position[0]
		game = self.mainframe.game
		self.delete("all")
		#Arriere plan
		self.create_image(0, 0, anchor=NW, image=self.bg)

		#Calcul des variation
		if direction == "h" :
			varY = -1
			varX = 0
			caseGauche = "g"
			caseFace = "h"
			caseDroite = "d"
		elif direction == "b" :
			varY = 1
			varX = 0
			caseGauche = "d"
			caseFace = "b"
			caseDroite = "g"
		elif direction == "g" :
			varY = 0
			varX = -1
			caseGauche = "b"
			caseFace = "g"
			caseDroite = "h"
		else : #La direction est : droite
			varY = 0
			varX = +1
			caseGauche = "h"
			caseFace = "d"
			caseDroite = "b"

		#C5
		if game.is_a_possible_movement(game.is_a_possible_movement(game.is_a_possible_movement(game.is_a_possible_movement((posY, posX), caseFace), caseFace), caseFace), caseFace) :
			y,x = game.is_a_possible_movement(game.is_a_possible_movement(game.is_a_possible_movement(game.is_a_possible_movement((posY, posX), caseFace), caseFace), caseFace), caseFace)
			if not game.is_a_possible_movement((y,x), caseGauche) :
				self.create_image(0, 0, anchor=NW, image=self.l5)
			if not game.is_a_possible_movement((y,x), caseDroite) :
				self.create_image(0, 0, anchor=NW, image=self.r5)
		#C4
		if game.is_a_possible_movement(game.is_a_possible_movement(game.is_a_possible_movement((posY, posX), caseFace), caseFace), caseFace) :
			y,x = game.is_a_possible_movement(game.is_a_possible_movement(game.is_a_possible_movement((posY, posX), caseFace), caseFace), caseFace)
			
			if not game.is_a_possible_movement((y,x), caseFace) :
				if y == finalPosY and x == finalPosX :
					self.create_image(0, 0, anchor=NW, image=self.f4_end)
				else :
					self.create_image(0, 0, anchor=NW, image=self.f4)
			if not game.is_a_possible_movement((y,x), caseGauche) :
				self.create_image(0, 0, anchor=NW, image=self.l4)
			if not game.is_a_possible_movement((y,x), caseDroite) :
				self.create_image(0, 0, anchor=NW, image=self.r4)
		#C3
				
		if game.is_a_possible_movement(game.is_a_possible_movement((posY, posX), caseFace), caseFace) :
			y,x = game.is_a_possible_movement(game.is_a_possible_movement((posY, posX), caseFace), caseFace)
			if not game.is_a_possible_movement((y, x), caseFace) :
				if y == finalPosY and x == finalPosX :
					self.create_image(0, 0, anchor=NW, image=self.f3_end)
				else :
					self.create_image(0, 0, anchor=NW, image=self.f3)
			if not game.is_a_possible_movement((y, x), caseGauche) :
				self.create_image(0, 0, anchor=NW, image=self.l3)
			if not game.is_a_possible_movement((y, x), caseDroite) :
				self.create_image(0, 0, anchor=NW, image=self.r3)
		#C2
		if game.is_a_possible_movement((posY, posX), caseFace) :
			y, x = game.is_a_possible_movement((posY, posX), caseFace)
			if not game.is_a_possible_movement((y, x), caseFace) :
				if y == finalPosY and x == finalPosX :
					self.create_image(0, 0, anchor=NW, image=self.f2_end)
				else :
					self.create_image(0, 0, anchor=NW, image=self.f2)
			if not game.is_a_possible_movement((y, x), caseGauche) :
				self.create_image(0, 0, anchor=NW, image=self.l2)
			if not game.is_a_possible_movement((y, x), caseDroite) :
				self.create_image(0, 0, anchor=NW, image=self.r2)
		#C1
		if not game.is_a_possible_movement((posY, posX), caseFace) :
			if posY == finalPosY and posX == finalPosX :
				self.create_image(0, 0, anchor=NW, image=self.f1_end)
			else :
				self.create_image(0, 0, anchor=NW, image=self.f1)
		if not game.is_a_possible_movement((posY, posX), caseGauche) :
			self.create_image(0, 0, anchor=NW, image=self.l1)
		if not game.is_a_possible_movement((posY, posX), caseDroite) :
			self.create_image(0, 0, anchor=NW, image=self.r1)
			
		#On dessine la fenetre
		self.update()
		
