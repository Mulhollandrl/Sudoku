import sys
import pygame
from pygame.locals import *
from game.components.board import Board
from enums.COLORS import *

FPS = 60
SCREENHEIGHT = 600
SCREENWIDTH = 800

class Game():
    def __init__(self) -> None:
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT
        self.board = Board(self.SCREENHEIGHT)
        self.cells_to_update = []
        self.selected_cell = 0
        self.game_over = False
        self.reset = False
        self.show_errors = False

        pygame.init()
        pygame.display.set_caption("Sudoku")

        self.DISPLAYSURF = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        self.FPS = pygame.time.Clock()

        self.FPS.tick(FPS)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #If it fails to process the key, then just pass
                if self.process_key(event.key) == 0:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # If the user is clicking in the control panel on the right
                if pos[0] > 600:
                    pass
                    #TODO: Implement logic to see which button they are hitting on the control panel
                else:
                    self.process_mouse(pos)

    def update(self):
        pass

    def render(self):
        self.DISPLAYSURF.fill(BROWN)
        self.board.render(self.DISPLAYSURF, self.show_errors)
        pygame.display.update()

    def game_loop(self):
        self.process_input()
        self.update()
        self.render()

    def process_key(self, key):
        pass

    def process_mouse(self, mouse_position):
        pass