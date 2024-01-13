import sys
import pygame
from pygame.locals import *
from game.components.board import Board
from enums.COLORS import *
from enums.KEYBINDINGS import *

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
        self.board.update(self.cells_to_update, self.selected_cell)
        self.cells_to_update = []

    def render(self):
        self.DISPLAYSURF.fill(BROWN)
        self.board.render(self.DISPLAYSURF, self.show_errors)
        pygame.display.update()

    def game_loop(self):
        self.process_input()
        self.update()
        self.render()

    def process_key(self, key):
        if key in KEYBINDINGS.keys():
            if key in NUMBERS_CONTROLS:
                self.cells_to_update.append((self.selected_cell, KEYBINDINGS[key]))

            elif key in MOVEMENT_CONTROLS:
                if KEYBINDINGS[key] == "Move Left" or KEYBINDINGS[key] == "Move Left Alt":
                    if self.selected_cell > 0:
                        self.selected_cell -= 1
                    else:
                        self.selected_cell = 80

                if KEYBINDINGS[key] == "Move Right" or KEYBINDINGS[key] == "Move Right Alt":
                    if self.selected_cell < 80:
                        self.selected_cell += 1
                    else:
                        self.selected_cell = 0

                if KEYBINDINGS[key] == "Move Down" or KEYBINDINGS[key] == "Move Down Alt":
                    if self.selected_cell < 72:
                        self.selected_cell += 9
                    else:
                        self.selected_cell = 8 - (self.selected_cell % 9)

                if KEYBINDINGS[key] == "Move Up" or KEYBINDINGS[key] == "Move Up Alt":
                    if self.selected_cell > 8:
                        self.selected_cell -= 9
                    else:
                        self.selected_cell = 80 - (9 - self.selected_cell)

            else:
                if KEYBINDINGS[key] == "Menu":
                    #TODO: Finish Menu
                    pass
                
                if KEYBINDINGS[key] == "Show Errors":
                    self.show_errors = not self.show_errors

                if KEYBINDINGS[key] == "Solve":
                    #TODO: Implement Solving Logic
                    pass

        else:
            return 0

    def process_mouse(self, mouse_position):
        pass