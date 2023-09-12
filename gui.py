import pygame
from puzzle import unsolved_board

pygame.init()


WIDTH, HEIGHT = 600,600
SQUARE_LENGTH = int(WIDTH/9)
screen = pygame.display.set_mode([1000, 1000])
running = True

class Cell():
    def __init__(self, main_screen, length, row, col, num, color):
        self.main_screen = main_screen
        self.length = length
        self.row = row
        self.col = col
        self.num = num
        self.color = color
        self.surf = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
        # self.surf.fill(color)
        self.rect = self.surf.get_rect()
        # self.Rect()
        self.rect.left = col * SQUARE_LENGTH + 10
        self.rect.top = row * SQUARE_LENGTH + 10

    def show(self):
        # screen.blit(self.surf, self.rect)
        pygame.draw.rect(self.main_screen, self.color, self.rect, 2)


class Button():
    def __init__(self, main_screen, length, x, y, color, buttonText, onClickFunction):
        self.main_screen = main_screen,
        self.length = length
        self.x = x
        self.y = y
        self.color = color
        self.buttonText = buttonText
        self.onClickFunction = onClickFunction

all_cells = []

for row in range(9):
    row_of_cells = []
    for col in range(9):
        color = (255, 255, 255)
        if ((row < 3 or row > 5) and (col < 3 or col > 5)) or ((row < 6 and row > 2 and col < 6 and col > 2)):
            color = (255, 255, 0)
            # new_cell = Cell(screen, SQUARE_LENGTH, row, col, unsolved_board[row][col], (255, 255, 0))
        new_cell = Cell(screen, SQUARE_LENGTH, row, col, unsolved_board[row][col], color)
        row_of_cells.append(new_cell)
    all_cells.append(row_of_cells)




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    screen.fill((0, 0, 0))
    for row in all_cells:
        for cell in row:
            cell.show()
    
    # pygame.draw.rect(screen, (0, 255, 0) ,pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()


pygame.quit()