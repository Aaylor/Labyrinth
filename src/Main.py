#!/dev/bin/python
from MainFrame import *

if __name__ == "__main__":
    fenetre = MainFrame()
    #fenetre.gameScreen.noGame()
    #fenetre.gameScreen.topView()
    fenetre.gameScreen.fpsView()
    fenetre.mainloop()

