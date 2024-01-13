from menuing.game_screen import Game_Screen
from enums.MENUS import MENUS

if __name__ == "__main__":
    current_screen = MENUS["Game"]
    game_screen = Game_Screen()

    while True:
        if current_screen == MENUS["Game"]:
            game_screen.active = True

        if game_screen.active:
            game_screen.game_loop()