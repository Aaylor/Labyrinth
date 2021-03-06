from tkinter import *
from tkinter import messagebox
from menubar import *
from input_area import *
from gamescreen import *

class MainFrame(Tk) :
	def __init__(self) :
		Tk.__init__(self)

		#MenuBar
		self.menubar = MenuBar(self)
		self.menubar.pack()

		#L'objet jeu
		self.game = None

		#Zone d'Affichage
		self.gamescreenPaneVertical = Frame(self)
		self.gamescreenPaneHorizontal = Frame(self.gamescreenPaneVertical)
		self.scrollbarX = Scrollbar(self.gamescreenPaneVertical, orient=HORIZONTAL)
		self.scrollbarY = Scrollbar(self.gamescreenPaneHorizontal, orient=VERTICAL)
		self.gamescreen = GameScreen(self.gamescreenPaneHorizontal, self, self.scrollbarX, self.scrollbarY)
		self.scrollbarX.config(command=self.gamescreen.xview)
		self.scrollbarY.config(command=self.gamescreen.yview)
		self.gamescreen.pack(side=LEFT)
		self.gamescreenPaneVertical.pack()
		self.gamescreenPaneHorizontal.pack()
		self.scrollbarY.pack(side=RIGHT, fill=Y)
		self.scrollbarX.pack(side=BOTTOM, fill=X)

		#Zone de Controle
		self.inputArea = InputArea(self)
		self.inputArea.pack()

		#Raccourcis clavier
		self.bind('<Control-o>', self.open_file)
		self.bind('<Control-g>', self.generate_labyrinth)
		self.bind('<Control-Shift-G>', self.open_generate_labyrinth_perso)
		self.bind('<Control-Shift-O>', self.open_session)
		self.bind('<Control-s>', self.save_session)
		self.bind('<d>', self.display_path)
		self.bind('<s>', self.display_solution)
		self.bind('<v>', self.change_view)
		self.bind('<Up>', self.move_up)
		self.bind('<Down>', self.move_down)
		self.bind('<Left>', self.move_left)
		self.bind('<Right>', self.move_right)

		#On lance le mode no game
		self.no_game()
		
		
	#Ouverture d'une session de jeu

	def open_file(self, *arg) :
		filename = filedialog.askopenfilename(parent=None,initialdir="../lab/",title='Veuillez choisir un fichier labyrinthe', filetypes = [('Fichier Labyrinthe', '.lab')])
		if filename != "" :
			#On associe le jeu à la fenetre
			self.game = game.game(False, filename=filename)
			if self.game.game_labyrinth.create == True :
				self.init_top_view()
			else :
				messagebox.showinfo("Fichier .lab invalide", "Le fichier Labyrinthe que vous avez séléctionné n'est pas valide.\nVeuillez ouvrir un autre fichier.")

		
	def open_session(self, *arg) :
		filename = filedialog.askopenfilename(parent=None,initialdir="../save/",title='Veuillez choisir un fichier labyrinthe', filetypes = [('Sauvegarde de Session de jeu', '.sav')])
		if filename != "" :
			self.game = game.game(False, filename=filename, loadgame=True)
			if self.game.game_labyrinth.create == True :
				self.init_top_view()
			else :
				messagebox.showinfo("Fichier .sav invalide", "Le fichier Labyrinthe que vous avez séléctionné n'est pas valide.\nVeuillez ouvrir un autre fichier.")
				
	def save_session(self, *arg) :
		if self.gamescreen.mode == "top_view" or self.gamescreen.mode == "fps_view" :
			filename = filedialog.asksaveasfilename(parent=None,initialdir="../save/",title='Veuillez choisir un fichier labyrinthe', filetypes = [('Sauvegarde de Session de jeu', '.sav')])
			self.game.save_game(filename)
		else :
			messagebox.showwarning("Erreur", "Aucune session de jeu lancée.")
			
	def generate_labyrinth(self, *arg) :
		#On associe le jeu à la fenetre
		self.game = game.game(True, width=20, height=10)
		self.init_top_view()
		
	def open_generate_labyrinth_perso(self, *arg) :
		CreateLabFrame(self);
		
	def generate_labyrinth_perso(self, hauteur, longueur, *arg):
		#On associe le jeu à la fenetre
		self.game = game.game(True, width=hauteur, height=longueur)
		self.init_top_view()
	
	#Methode liée au jeu
	
	def display_path(self, *arg) :
		if self.gamescreen.mode == "top_view" or self.gamescreen.mode == "fps_view" :
			if self.gamescreen.display_path == False :
				self.gamescreen.display_path = True
			else :
				self.gamescreen.display_path = False
			self.gamescreen.draw()
		
	def display_solution(self, *arg) :
		if self.gamescreen.mode == "top_view" or self.gamescreen.mode == "fps_view" :
			if self.gamescreen.display_solution == False :
				self.gamescreen.display_solution = True
			else :
				self.gamescreen.display_solution = False
			self.gamescreen.draw()
		
	def game_over(self, *arg) :
		messagebox.showinfo("Félicitation !", "Vous avez résolu le labyrinthe, félicitation !")
		self.no_game()
		
		
	#Methode de vues
	
	def change_view(self, *arg) :
		if self.gamescreen.mode == "top_view" :
			self.init_fps_view()
		elif self.gamescreen.mode == "fps_view" :
			self.init_top_view()

	def no_game(self, *arg) :
		self.gamescreen.no_game()
		self.gamescreen.yview_moveto(0)
		self.gamescreen.xview_moveto(0)
		self.scrollbarX.pack_forget()
		self.scrollbarY.pack_forget()
		self.inputArea.display_no_game()
		
	def init_top_view(self, *arg) :
		#On passe l'ecran de jeu en mode jeu en vue du dessus
		self.gamescreen.init_top_view()
		self.gamescreen.draw()
		#On passe la zone de controle en mode vue du dessus
		self.inputArea.display_top_view()

	def init_fps_view(self, *arg) :
		self.gamescreen.init_fps_view()
		self.gamescreen.yview_moveto(0)
		self.gamescreen.xview_moveto(0)
		self.gamescreen.draw()
		self.scrollbarX.pack_forget()
		self.scrollbarY.pack_forget()
		self.inputArea.display_fps_view()

	#Les méthodes de controle du jeu
	def move(self, direction, *arg) :
		if self.gamescreen.mode != "no_game" :
			if self.gamescreen.mode == "top_view" :
				self.game.move(direction)
				self.game.player.direction = direction
			elif self.gamescreen.mode == "fps_view" :
				if direction == "h" :
					self.game.move(self.game.player.direction)
				elif direction == "b" :
					if self.game.player.direction == "h" :
						self.game.move("b")
					elif self.game.player.direction == "g" :
						self.game.move("d")
					elif self.game.player.direction == "b" :
						self.game.move("h")
					elif self.game.player.direction == "d" :
						self.game.move("g")
				elif direction == "g" :
					if self.game.player.direction == "h" :
						self.game.player.direction = "g"
					elif self.game.player.direction == "g" :
						self.game.player.direction = "b"
					elif self.game.player.direction == "b" :
						self.game.player.direction = "d"
					elif self.game.player.direction == "d" :
						self.game.player.direction = "h"
				elif direction == "d" :
					if self.game.player.direction == "h" :
						self.game.player.direction = "d"
					elif self.game.player.direction == "g" :
						self.game.player.direction = "h"
					elif self.game.player.direction == "b" :
						self.game.player.direction = "g"
					elif self.game.player.direction == "d" :
						self.game.player.direction = "b"
			self.gamescreen.draw()
			if self.game.is_at_exit_point() :
				self.game_over()
								
	def move_up(self, *arg) :
		self.move("h")
	def move_down(self, *arg) :
		self.move("b")
	def move_left(self, *arg) :
		self.move("g")
	def move_right(self, *arg) :
		self.move("d")
				
				
				
class CreateLabFrame(Toplevel) :
	def __init__(self, mainframe, *arg) :
		self.mainframe = mainframe
		Toplevel.__init__(self, mainframe)
		longueurLab = Label(self, text="Longueur du Labyrinthe :")
		longueurLab.pack()
		self.longueurBox = Spinbox(self, from_=10, to=60)
		self.longueurBox.pack()
		hauteurLab = Label(self, text="Hauteur du Labyrinthe :")
		hauteurLab.pack()
		self.hauteurBox = Spinbox(self, from_=10, to=60)
		self.hauteurBox.pack()
		okButton = Button(self, text ="Generer le Labyrinthe", command=self.verify_values)
		okButton.pack()

	def verify_values(self, *arg) :
		try :
			longueur = int(self.longueurBox.get())
			hauteur = int(self.hauteurBox.get())
			if(longueur > 60 or hauteur > 60) :
				self.warning_value_too_high()
			else :
				self.mainframe.generate_labyrinth_perso(longueur, hauteur)
				self.destroy()
		except :
			self.warning_value_non_correct()
	
	def warning_value_too_high(self, *arg) :
		messagebox.showerror("Erreur de saisie", "Les valeurs saisies sont trop élevées")

	def warning_value_non_correct(self) :
		messagebox.showerror("Erreur de saisie", "Les valeurs saisies comportent des caractères non autorisés")
		
