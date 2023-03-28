# Adding libraries used in the Project.
import pygame as pg
from random import randint
import ui
import validation_mod

INF = float('inf')
vec2 = pg.math.Vector2

class TicTacToe:
    def __init__(self,game):
        self.game = game
        self.win_size = 900
        self.cell_size = self.win_size // 3
        self.cell_center = vec2(self.cell_size/2)
        self.board_image = self.get_image(path='res/board.png',res=[self.win_size] * 2)
        self.O_image = self.get_image(path='res/OO.png',res=[self.cell_size] * 2)
        self.X_image = self.get_image(path='res/XX.png',res=[self.cell_size] * 2)

        self.arr = [[INF,INF,INF],
                    [INF,INF,INF],
                    [INF,INF,INF]]
        
        self.win_combinations_arr = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]
        
        self.winner = None
        self.game_steps = 0
        self.font = pg.font.SysFont('Verdana', self.cell_size // 4, True)
        
        self.player = randint(0,1)

    def check_winner(self):
        for win_comb in self.win_combinations_arr:
            sum_line = sum([self.arr[i][j] for i, j in win_comb])
            if sum_line in {0, 3}:
                self.winner = 'XO'[sum_line == 0]
                self.winner_line = [vec2(win_comb[0][::-1]) * self.cell_size + self.cell_center,
                                    vec2(win_comb[2][::-1]) * self.cell_size + self.cell_center]

    def game_process(self):
        current_cell = vec2(pg.mouse.get_pos()) // self.cell_size
        col,row = map(int,current_cell)
        left_click = pg.mouse.get_pressed()[0]

        if left_click and self.arr[row][col] == INF and not self.winner:
            self.arr[row][col] = self.player
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()
        
    def draw_objects(self):
        for y , row in enumerate(self.arr):
            for x,obj in enumerate(row):
                if obj != INF:
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x,y) *self.cell_size)

    def draw_winner(self):
        if self.winner:
            pg.draw.line(self.game.screen, 'red', *self.winner_line, self.cell_size // 8)
            label = self.font.render(f'Player "{self.winner}" wins!', True, 'white', 'black')
            self.game.screen.blit(label, (self.win_size // 2 - label.get_width() // 2, self.win_size // 4))
        elif self.game_steps == 9:
            label = self.font.render(f'Match Draw!!', True, 'black', 'green')
            self.game.screen.blit(label, (self.win_size // 2 - label.get_width() // 2, self.win_size // 4))

    # Description - Display the Board.
    # Parameters - None
    def draw_board(self):
        self.game.screen.blit(self.board_image,(0,0))
        self.draw_objects()
        self.draw_winner()

    # Static method to load or scale images.
    def get_image(self,path,res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img,res)
    
    def print_caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')
        print("Games Steps",self.game_steps)
        if self.winner:
            pg.display.set_caption(f'Player "{self.winner}" wins! Press Space to Restart')
        elif self.game_steps == 9:
            pg.display.set_caption(f'Game Draw! Press Space to Restart')


    def run_tic_tac_toe(self):
        self.print_caption()
        self.draw_board()
        self.game_process()
