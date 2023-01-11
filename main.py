import game
import menu


running = True

while running:
    if menu.Menu().start_game==True:
        game.Game()
        
    else:
        running = False
    