from game.components.cell import Cell

class Board:
    def __init__(self, SCREENHEIGHT) -> None:
        self.SCREENSIZE = SCREENHEIGHT
        self.OFFSET = self.SCREENSIZE//9
        self.game_over = False
        self.cells = []

    def update(self, cells_to_update, selected_cell):
        for cell, number in cells_to_update["number"]:
            cell.update_number(number)

        for index, cell in enumerate(self.cells):
            if index == selected_cell:
                cell.selected = True
            else:
                cell.selected = False
    
    def render(self):
        pass