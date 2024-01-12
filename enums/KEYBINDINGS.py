import pygame

KEYBINDINGS = {
    pygame.K_ESCAPE: "Menu",
    pygame.K_e: "Show Errors",
    pygame.K_v: "Solve",
    pygame.K_LEFT: "Move Left",
    pygame.K_a: "Move Left Alt",
    pygame.K_RIGHT: "Move Right",
    pygame.K_d: "Move Right Alt",
    pygame.K_DOWN: "Move Down",
    pygame.K_s: "Move Down Alt",
    pygame.K_UP: "Move Up",
    pygame.K_w: "Move Up Alt",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_8: "8",
    pygame.K_9: "9"
}

KEYBINDINGS_REVERSED = {
    "Menu": pygame.K_ESCAPE,
    "Show Errors": pygame.K_e,
    "Solve": pygame.K_v,
    "Move Left": pygame.K_LEFT,
    "Move Left Alt": pygame.K_a,
    "Move Right": pygame.K_RIGHT,
    "Move Right Alt": pygame.K_d,
    "Move Down": pygame.K_DOWN,
    "Move Down Alt": pygame.K_s,
    "Move Up": pygame.K_UP,
    "Move Up Alt": pygame.K_w,
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9
}

NUMBERS_CONTROLS = [KEYBINDINGS_REVERSED["1"], KEYBINDINGS_REVERSED["2"], KEYBINDINGS_REVERSED["3"], 
                    KEYBINDINGS_REVERSED["4"], KEYBINDINGS_REVERSED["5"], KEYBINDINGS_REVERSED["6"], 
                    KEYBINDINGS_REVERSED["7"], KEYBINDINGS_REVERSED["8"], KEYBINDINGS_REVERSED["9"]]

MOVEMENT_CONTROLS = [KEYBINDINGS_REVERSED["Move Left"], KEYBINDINGS_REVERSED["Move Left Alt"],
                     KEYBINDINGS_REVERSED["Move Right"], KEYBINDINGS_REVERSED["Move Right Alt"],
                     KEYBINDINGS_REVERSED["Move Down"], KEYBINDINGS_REVERSED["Move Down Alt"],
                     KEYBINDINGS_REVERSED["Move Up"], KEYBINDINGS_REVERSED["Move Up Alt"],]