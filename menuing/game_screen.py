from game.game import Game

class Game_Screen:
    def __init__(self) -> None:
        self.active = False
        self.game = Game()

    def reset_game(self):
        self.game = Game()

    def game_loop(self):
        self.game.game_loop()