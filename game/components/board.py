from game.components.cell import Cell

BOARDSIZE = 9

class Board:
    def __init__(self, SCREENHEIGHT) -> None:
        self.SCREENSIZE = SCREENHEIGHT
        self.OFFSET = self.SCREENSIZE//9
        self.game_over = False
        self.cells = []

        for i in range(BOARDSIZE*BOARDSIZE):
            x_index = i % BOARDSIZE
            y_index = i // BOARDSIZE
            right_edge = False
            bottom_edge = False

            if i % 9 == 2 or i % 9 == 5:
                right_edge = True

            if (i + 9) % 27 < 9:
                bottom_edge = True

            self.cells.append(Cell(self.SCREENSIZE//BOARDSIZE, 
                                   (x_index * self.OFFSET, y_index * self.OFFSET, 
                                    (x_index + 1) * self.OFFSET, (y_index + 1) * self.OFFSET), 
                                    right_edge, bottom_edge))
            
    def update(self, cells_to_update, selected_cell):
        for cell, number in cells_to_update:
            self.cells[cell].update_number(number)

        for index, cell in enumerate(self.cells):
            if index == selected_cell:
                cell.selected = True
            else:
                cell.selected = False
    
    def render(self, surface, show_errors):
        for cell in self.cells:
            cell.render(surface, self.OFFSET, show_errors)