import pygame
pygame.font.init()

my_font = pygame.font.SysFont('Verdana', 30)

# creating a class for all the cells 

class Cell():
    def __init__(self, main_screen, length, row, col, num, color, changable, answer):
        self.main_screen = main_screen
        self.length = length
        self.row = row
        self.col = col
        self.num = num
        self.color = color
        self.ogcolor = color
        self.changable = changable
        self.answer = answer

        # creating the surface and rectangle of the cell
        self.surf = pygame.Surface((self.length, self.length))
        self.rect = self.surf.get_rect()

        # positioning the cell based on its order in the board
        self.rect.left = col * self.length + 10
        self.rect.top = row * self.length + 10

        # if there is already a designated number
        if self.num:
            # display that number
            self.new_num(self.num - 1)
        

    def show(self):
        # screen.blit(self.surf, self.rect)
        pygame.draw.rect(self.main_screen, self.color, self.rect, 4)
        if(self.num):
            self.main_screen.blit(self.text_surface, self.font_rect)

    def return_rect(self):
        return self.rect
    
    def selected(self):
        self.color = (0, 0, 255)
        # print(str(self.num))
    
    def unselect(self):
        self.color = self.ogcolor
    
    def new_num(self, num, font_color = (255,255,255)):
        self.num = num + 1
        self.text_surface = my_font.render(str(self.num), False, font_color)
        self.font_rect = pygame.Rect(self.rect.left + (self.length/4), self.rect.top + (self.length/5), self.length, self.length)

    def return_changable(self):
        return self.changable

    def check(self):
        if self.answer != self.num:
            self.color = (255, 0, 0)


