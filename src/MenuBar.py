#!/usr/bin/env python3.3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sys

class MenuBar(Frame) :
    def __init__(self, mainFrame) :
        Frame.__init__(self, mainFrame)
        self.menuBar = Menu(self)
        self.master.config(menu=self.menuBar)

        #Menu Fichier
        fichierMenu = Menu(self, tearoff = 0)
        self.menuBar.add_cascade(label="Fichier", menu=fichierMenu)
        fichierMenu.add_command(label="Générer un Labyrinthe", command=MenuBar.GenererLabyrinthe)
        fichierMenu.add_command(label="Ouvrir un Labyrinthe", command = MenuBar.OuvrirFichier)
        fichierMenu.add_separator()
        fichierMenu.add_command(label="Quitter", command=MenuBar.Quitter)

        #Menu Aide
        aideMenu=Menu(self, tearoff=0)
        self.menuBar.add_cascade(label="Aide", menu=aideMenu)
        aideMenu.add_command(label="A propos", command=MenuBar.APropos)

    def APropos() :
        import random
        if random.randint(0, 1) == 0 :
            chaine = "\tMehdi Khelifi\n\tRunarvot Loic"
        else :
            chaine = "\tRunarvot Loic\n\tMehdi Khelifi"        
        messagebox.showinfo("A propos", "Dungeon and Python est un projet universitaire développé par deux étudiants : \n" + chaine)

    def GenererLabyrinthe() :
        pass
    
    def OuvrirFichier() :
        directory = filedialog.askopenfilename(parent=None,initialdir="../",title='Veuillez choisir un fichier labyrinthe', filetypes = [('Fichier Labyrinthe', '.lab')])

    def Quitter() :
        sys.exit()
