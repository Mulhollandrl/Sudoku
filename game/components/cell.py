import pygame
from enums.CORNERS import *
from enums.COLORS import *

class Cell:
    def __init__(self, dimensions, corners, right_edge, bottom_edge) -> None:
        self.corners = corners
        self.selected = False
        self.right_edge = right_edge
        self.bottom_edge = bottom_edge
        #TODO: Implement logic to find a correct and solvable number
        self.correct_number = 0
        self.current_number = 0
        self.guessed = False
        self.background_color = BEIGE

    def update_number(self, number):
        self.current_number = number
        self.guessed = True

    def render(self, surface, offset, show_errors):
        LINE_WEIGHT = 2
        font = pygame.font.Font(None, 64)
        bottom_line_weight = LINE_WEIGHT
        right_line_weight = LINE_WEIGHT

        if self.selected:
            self.background_color = DARK_BEIGE
        elif show_errors and self.guessed:
            if self.correct_number == self.current_number:
                self.background_color = GREEN
            else:
                self.background_color = RED
        else:
            self.background_color = BEIGE

        if self.bottom_edge:
            bottom_line_weight = 5
        
        if self.right_edge:
            right_line_weight = 5

        pygame.draw.rect(surface, self.background_color,
                         pygame.Rect(self.corners[CORNERS["left"]], self.corners[CORNERS["up"]], offset, offset))
        pygame.draw.line(surface, BROWN, 
                         (self.corners[CORNERS["left"]], self.corners[CORNERS["up"]]),
                         (self.corners[CORNERS["left"]], self.corners[CORNERS["down"]]), LINE_WEIGHT)
        pygame.draw.line(surface, BROWN, 
                         (self.corners[CORNERS["left"]], self.corners[CORNERS["up"]]),
                         (self.corners[CORNERS["right"]], self.corners[CORNERS["up"]]), LINE_WEIGHT)
        pygame.draw.line(surface, BROWN, 
                         (self.corners[CORNERS["right"]], self.corners[CORNERS["up"]]),
                         (self.corners[CORNERS["right"]], self.corners[CORNERS["down"]]), right_line_weight)
        pygame.draw.line(surface, BROWN, 
                         (self.corners[CORNERS["left"]], self.corners[CORNERS["down"]]),
                         (self.corners[CORNERS["right"]], self.corners[CORNERS["down"]]), bottom_line_weight)
        
        if self.guessed:
            text = font.render(self.current_number, True, BROWN)
            text_width, text_height = text.get_size()

            surface.blit(text, 
                         (((offset - text_width) // 2) + self.corners[CORNERS["left"]], 
                          ((offset- text_height) // 2) + self.corners[CORNERS["up"]]))