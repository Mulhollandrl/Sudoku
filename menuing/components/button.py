import pygame
from enums.COLORS import *

class Button:
    def __init__(self, coords, width, height, text) -> None:
        self.selected = False
        self.coords = coords
        self.width = width
        self.height = height
        self.text = text

    def render(self, surface):
        background_color = BEIGE

        if self.selected:
            background_color = DARK_BEIGE

        pygame.draw.rect(surface, background_color,
                         pygame.Rect(self.coords[0], self.coords[1], self.width, self.height))