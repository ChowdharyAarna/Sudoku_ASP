import pygame
from puzzle import unsolved_board
from cell import Cell
from button import Button

pygame.init()


WIDTH, HEIGHT = 600,600
SQUARE_LENGTH = int(WIDTH/9)
BUTTON_LENGTH = 40
screen = pygame.display.set_mode([1000, 1000])
running = True


all_cells = []
all_buttons = []
button_y = 20
for num in range(9):
    
    all_buttons.append(Button(screen, BUTTON_LENGTH, 650, button_y, (255, 255, 255), str(num + 1), None))
    button_y += 65

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
        # (x, y)= pygame.mouse.get_pos()
        # if event.type == pygame.MOUSEBUTTONDOWN:
            
    screen.fill((0, 0, 0))
    for row in all_cells:
        for cell in row:
            cell.show()
    for button in all_buttons:
        # button.show()
        screen.blit(button.return_surf(), button.return_rect())
        screen.blit(button.return_text(), button.return_text_rect())

    # pygame.draw.rect(screen, (0, 255, 0) ,pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()


pygame.quit()