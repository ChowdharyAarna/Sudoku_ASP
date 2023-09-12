import pygame

class Button():
    def __init__(self, main_screen, length, x, y, color, buttonText, onClickFunction):
        self.main_screen = main_screen,
        self.length = length
        self.x = x
        self.y = y
        self.color = color
        self.buttonText = buttonText
        self.onClickFunction = onClickFunction
        
        self.surf = pygame.Surface((self.length, self.length))
        self.rect = pygame.Rect(self.x, self.y, self.length, self.length)
    
    def show(self):

        self.main_screen.blit(self.surf, self.rect)