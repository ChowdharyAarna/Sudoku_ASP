import pygame
pygame.font.init()

my_font = pygame.font.SysFont('Verdana', 30)

# creating a class for all the buttons 

class Button():
    def __init__(self, main_screen, length, x, y, color, buttonText, num, onClickFunction):
        self.main_screen = main_screen,
        self.length = length
        self.x = x
        self.y = y
        self.color = color
        self.buttonText = buttonText
        self.num = num
        self.onClickFunction = onClickFunction
        

        # creating the surface and rectangle of the cell
        self.surf = pygame.Surface((self.length, self.length))
        self.rect = pygame.Rect(self.x, self.y, self.length, self.length)

        # creating a rectangle to display the font - making sure the number will be in the center
        self.font_rect = pygame.Rect(self.x + (7 * self.length/24), self.y, self.length, self.length)
        self.surf.fill(self.color)
        self.text_surface = my_font.render(buttonText, False, (255, 255, 255))

    # below are functions to return various values

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
