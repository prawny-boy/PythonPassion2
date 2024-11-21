"""
This is a Python Passion Project by Sean and Dylan.
This is a one-player game where the player plays a snake,
and tries to break walls and collects segments to grow longer.
There are powerups that the player can collect to change the game's difficulty.
The game is a Python game that uses Pygame to create the graphics and sound effects.
"""

import pygame as _pygame
import random as _random


#Initialise Game

_pygame.init()
clock = _pygame.time.Clock()
clock.tick(60)

screen = _pygame.display.set_mode((400, 600))
_pygame.display.set_caption("Tail of the Dragon")
_pygame.display.set_icon(_pygame.image.load("Sprites\\Icon.png"))

_pygame.font.init()
# inktype_font = _pygame.font.Font("Fonts\\InkType.ttf", 20)
# mochalatte_font = _pygame.font.Font("Fonts\\Mochalatte.ttf", 20)
inktype_font = _pygame.font.Font(None, 20)
mochalatte_font = _pygame.font.Font(None, 36)

menu_background_rgb = (30, 36, 54)
colour_black = (0, 0, 0)
colour_white = (255, 255, 255)

# Variables
game_state = "Menu"
button_dict = {}
score = 0

# Classes
class Button:
    def __init__(
            self, 
            text,
            x_pos, y_pos, 
            width=150, height=25, 
            enabled=True, 
            font: _pygame.font.Font=inktype_font, text_colour=colour_black, 
            colour=colour_white, border_colour=colour_white,
            accent_colour=colour_black, disabled_colour=colour_black):
        
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.width = width
        self.height = height
        self.colour = colour
        self.font = font
        self.text_colour = text_colour
        self.border_colour = border_colour
        self.accent_colour = accent_colour
        self.disabled_colour = disabled_colour
        self.draw()
    
    def draw(self):
        button_text = self.font.render(self.text, True, self.text_colour)
        button_rect = _pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        if self.enabled:
            if self.check_hover():
                _pygame.draw.rect(screen, self.accent_colour, button_rect, 0, 5)
            else:
                _pygame.draw.rect(screen, self.colour, button_rect, 0, 5)
            _pygame.draw.rect(screen, self.border_colour, button_rect, 2, 5)
            screen.blit(button_text, (3 + self.x_pos, 3 + self.y_pos)) # fix this
        else:
            pass
    
    def check_click(self):
        mouse_pos = _pygame.mouse.get_pos()
        left_click = _pygame.mouse.get_pressed()[0]
        button_rect = _pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
    def check_hover(self):
        mouse_pos = _pygame.mouse.get_pos()
        button_rect = _pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

# Functions
def manage_interactives():
    buttons_dict = {}
    buttons = [("start", ("Start", 100, 250, 200, 50), "Menu"), 
               ("challenges", ("Challenges", 100, 350, 200, 50), "Menu"),
               ("challenges back", ("Back", 100, 450, 200, 50), "Challenges")]
    for i in range(len(buttons)):
        button = buttons[i]
        if button[2] == game_state:
            enabled = True
        else:
            enabled = False
        buttons_dict[button[0]] = Button(*button[1], enabled=enabled)
    
    return buttons_dict

def check_buttons(game_state):
    if button_dict["start"].check_click():
        game_state = "Game"
    elif button_dict["challenges"].check_click():
        game_state = "Challenges"
    elif button_dict["challenges back"].check_click():
        game_state = "Menu"
    return game_state

def draw_page(game_state, score):
    if game_state == "Menu":
        screen.fill(menu_background_rgb)
        draw_text("Tail of the Dragon", 15, 50, colour=colour_white, font=mochalatte_font)
    elif game_state == "Challenges":
        draw_text("Challenges: Not done yet", 15, 50, colour=colour_white, font=mochalatte_font)
    elif game_state == "Game":
        draw_text(f"Score: {score}", 15, 15, colour=colour_white, font=mochalatte_font)

def draw_text(text:str, x, y, colour=colour_white, font=inktype_font, line_spacing=15):
    # Split text into lines at newline characters
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, colour)
        line_rect = line_surface.get_rect(topleft=(x, y + i * line_spacing))
        screen.blit(line_surface, line_rect)

menu = True
while True:
    if game_state == "Game":
        # Main Game Loop
        while True:
            screen.fill(menu_background_rgb)
            draw_page(game_state, score)
            clock.tick(60)
            for event in _pygame.event.get():
                if event.type == _pygame.QUIT:
                    _pygame.quit()
                    exit("User quit the game.")
                if event.type == _pygame.KEYDOWN:
                    pass
    else:
        # Menu Loop
        while True:
            screen.fill(menu_background_rgb)
            draw_page(game_state, score)
            clock.tick(60)
            button_dict:dict[str, Button] = manage_interactives()
            for event in _pygame.event.get():
                if event.type == _pygame.QUIT:
                    _pygame.quit()
                    exit("User quit the game.")
                if event.type == _pygame.MOUSEBUTTONDOWN:
                    if new_press:
                        game_state = check_buttons(game_state)
                    new_press = False
                else:
                    new_press = True
            _pygame.display.flip()
