import pygame
from puzzle import unsolved_board
from cell import Cell
from button import Button

pygame.init()


WIDTH, HEIGHT = 600,600
SQUARE_LENGTH = int(WIDTH/9)
screen = pygame.display.set_mode([1000, 1000])
running = True

all_cells = []
buttons = []

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