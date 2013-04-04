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
        fichierMenu.add_command(label="Générer un Labyrinthe", command= self.genererLabyrinthe)
        fichierMenu.add_command(label="Ouvrir un Labyrinthe", command = self.ouvrirFichier)
        fichierMenu.add_separator()
        fichierMenu.add_command(label="Quitter", command=self.quitter)

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

    def genererLabyrinthe(self) :
        jeu = game.game(True, width=20, height=15)
        self.mainFrame.top_view(jeu)

    
    def ouvrirFichier(self) :
        filename = filedialog.askopenfilename(parent=None,initialdir="../",title='Veuillez choisir un fichier labyrinthe', filetypes = [('Fichier Labyrinthe', '.lab')])
        jeu = game.game(False, filename=filename)
        self.mainFrame.top_view(jeu)

    def quitter(self) :
        sys.exit()
