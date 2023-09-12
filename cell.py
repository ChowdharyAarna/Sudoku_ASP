import pygame


class Cell():
    def __init__(self, main_screen, length, row, col, num, color):
        self.main_screen = main_screen
        self.length = length
        self.row = row
        self.col = col
        self.num = num
        self.color = color
        self.surf = pygame.Surface((self.length, self.length))
        # self.surf.fill(color)
        self.rect = self.surf.get_rect()
        # self.Rect()
        self.rect.left = col * self.length + 10
        self.rect.top = row * self.length + 10

    def show(self):
        # screen.blit(self.surf, self.rect)
        pygame.draw.rect(self.main_screen, self.color, self.rect, 2)


