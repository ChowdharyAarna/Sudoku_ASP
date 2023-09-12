import pygame
pygame.init()

WIDTH, HEIGHT = 900,900
SQUARE_LENGTH = int(WIDTH/9)
screen = pygame.display.set_mode([500, 500])
running = True

class Cell():
    def __init__(self, length, row, col, num, color):
        self.length = length
        self.row = row
        self.col = col
        self.num = num
        self.color = color
        self.surf = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.left = col * SQUARE_LENGTH
        self.rect.top = row * SQUARE_LENGTH

    def show(self):
        screen.blit(self.surf, self.rect)
all_cells = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    screen.fill((255, 255, 255))
    pygame.display.flip()




pygame.quit()