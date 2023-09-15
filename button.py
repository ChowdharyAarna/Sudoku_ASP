import pygame
pygame.font.init()

my_font = pygame.font.SysFont('Verdana', 30)

class Button():
    def __init__(self, main_screen, width, height, x, y, color, buttonText, num, onClickFunction):
        self.main_screen = main_screen,
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.buttonText = buttonText
        self.num = num
        self.onClickFunction = onClickFunction
        
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font_rect = pygame.Rect(self.x + (7 * self.width/24), self.y, self.width, self.height)
        self.surf.fill(self.color)
        self.text_surface = my_font.render(buttonText, False, (0, 0, 0))

    
    # def show(self):

        # self.main_screen.blit(self.surf, self.rect)
        # pygame.draw.rect(self.main_screen, self.color, self.rect)
    
    def return_surf(self):
        return self.surf
    
    def return_rect(self):
        return self.rect

    def return_text(self):
        return self.text_surface

    def return_text_rect(self):
        return self.font_rect
    
    def return_num(self):
        return self.num
