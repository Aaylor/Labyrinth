#!/usr/bin/env python3.3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import game
import sys

class MenuBar(Frame) :
	def __init__(self, mainFrame) :
		Frame.__init__(self, mainFrame)
		self.mainFrame = mainFrame
		self.menuBar = Menu(self)
		self.master.config(menu=self.menuBar)

		#Menu Fichier
		fichierMenu = Menu(self, tearoff = 0)
		self.menuBar.add_cascade(label="Fichier", menu=fichierMenu)
		fichierMenu.add_command(label="Générer un Labyrinthe automatiquement", command= self.mainFrame.generate_labyrinth, accelerator="Ctrl-G")
		fichierMenu.add_command(label="Générer un Labyrinthe personnalisé", command= self.mainFrame.open_generate_labyrinth_perso, accelerator="Ctrl-Shift-G")
		fichierMenu.add_command(label="Ouvrir un Labyrinthe", command = self.mainFrame.open_file, accelerator="Ctrl-O")
		fichierMenu.add_separator()
		fichierMenu.add_command(label="Restaurer la session de jeu", command = self.mainFrame.open_session, accelerator="Ctrl-Shift-O")
		fichierMenu.add_command(label="Sauvegarder la session de jeu", command = self.mainFrame.save_session, accelerator="Ctrl-S")
		fichierMenu.add_separator()
		fichierMenu.add_command(label="Quitter", command=self.quitter)
		
		#Menu Jeu
		jeuMenu = Menu(self, tearoff = 0)
		self.menuBar.add_cascade(label="Jeu", menu=jeuMenu)
		jeuMenu.add_command(label="Changer de vue", command= self.mainFrame.change_view, accelerator="v")
		jeuMenu.add_separator()
		jeuMenu.add_command(label="Afficher le chemin parcouru", command= self.mainFrame.display_path, accelerator="d")
		jeuMenu.add_command(label="Afficher la solution du labyrinthe", command= self.mainFrame.display_solution, accelerator="s")
		
		
		#Menu Aide
		aideMenu=Menu(self, tearoff=0)
		self.menuBar.add_cascade(label="Aide", menu=aideMenu)
		aideMenu.add_command(label="A propos", command=self.aPropos)

	def aPropos(self) :
		import random
		if random.randint(0, 1) == 0 :
			chaine = "\tMehdi Khelifi\n\tRunarvot Loic"
		else :
			chaine = "\tRunarvot Loic\n\tMehdi Khelifi"        
		messagebox.showinfo("A propos", "Dungeon and Python est un projet universitaire développé par deux étudiants : \n" + chaine)

	def quitter(self) :
		sys.exit()
