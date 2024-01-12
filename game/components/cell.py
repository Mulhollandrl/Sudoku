import pygame
from enums.CORNERS import *
from enums.COLORS import *

class Cell:
    def __init__(self, corners, number) -> None:
        self.corners = corners
        self.selected = False
        self.correct_number = number
        self.current_number = 0
        self.guessed = False
        self.background_color = BEIGE

    def update_number(self, number):
        self.current_number = number
        self.guessed = True

    def render(self, surface, offset, show_errors):
        font = pygame.font.Font(None, 64)

        if self.selected:
            self.background_color = DARK_BEIGE
        elif show_errors and self.guessed:
            if self.correct_number == self.current_number:
                self.background_color = GREEN
            else:
                self.background_color = RED
        else:
            self.background_color = BEIGE

        pygame.draw.rect(surface, self.background_color,
                         pygame.Rect(self.corners[CORNERS["left"]], self.corners["up"], offset, offset))
        
        if self.guessed:
            text = font.render(self.current_number, True, BROWN)
            text_width, text_height = text.get_size()

            surface.blit(text, 
                         (((offset - text_width) // 2) + CORNERS["left"], 
                          ((offset- text_height) // 2) + CORNERS["up"]))