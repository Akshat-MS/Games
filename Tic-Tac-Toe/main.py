import pygame as pg
import tictactoe
import sys

pg.init()

# Define Windoe Size
WIN_SIZE = 900


class Game:

    # Description - Constructor or Initializer
    def __init__(self):
        
        # Setup the drawing window.
        self.screen = pg.display.set_mode([WIN_SIZE] * 2) 

        #instant of Clock class to set the framerate.
        self.clock = pg.time.Clock()

        # Create class contains main logic of the Game.
        self.tic_tac_toe = tictactoe.TicTacToe(self)
    
    def new_game(self):
        self.tic_tac_toe = tictactoe.TicTacToe(self)

    # Description - Method to check Evnets.
    def check_events(self):

        # Checking for the events. 
        # Check for Quit Event.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

    # Description - Application Launch Method.
    def run_game(self):
        while True:

            self.tic_tac_toe.run_tic_tac_toe()
            # call check for the events
            self.check_events()

            # Update the rendoring surface
            pg.display.update()

            # Set the framerate
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run_game()
