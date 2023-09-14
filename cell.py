import pygame
pygame.font.init()

my_font = pygame.font.SysFont('Verdana', 30)

class Cell():
    def __init__(self, main_screen, length, row, col, num, color):
        self.main_screen = main_screen
        self.length = length
        self.row = row
        self.col = col
        self.num = num
        self.color = color
        self.ogcolor = color
        self.surf = pygame.Surface((self.length, self.length))
        # self.surf.fill(color)
        self.rect = self.surf.get_rect()
        # self.Rect()
        self.rect.left = col * self.length + 10
        self.rect.top = row * self.length + 10
        if self.num:
            self.text_surface = my_font.render(str(self.num), False, (255, 255, 255))
            self.font_rect = pygame.Rect(self.rect.left + (2 * self.length), self.rect.top + (self.length/2), self.length, self.length)
        

    def show(self):
        # screen.blit(self.surf, self.rect)
        pygame.draw.rect(self.main_screen, self.color, self.rect, 2)
        if(self.num):
            self.main_screen.blit(self.text_surface, self.rect)

    def return_rect(self):
        return self.rect
    
    def selected(self):
        self.color = (0, 0, 255)
        # print(str(self.num))
    
    def unselect(self):
        self.color = self.ogcolor
    
    def new_num(self, num):
        self.num = num + 1
        self.text_surface = my_font.render(str(self.num), False, (255, 255, 255))
        self.font_rect = pygame.Rect(self.rect.left + (2 * self.length), self.rect.top + (self.length/2), self.length, self.length)


