import pygame
from puzzle import unsolved_board
from puzzle import solved_board
from cell import Cell
from button import Button

pygame.init()

is_cell_clicked = True
clicked_cell = None
button_pressed = None
WIDTH, HEIGHT = 600,600
SQUARE_LENGTH = int(WIDTH/9)
BUTTON_LENGTH = 40
screen = pygame.display.set_mode([1000, 1000])
running = True



all_cells = []
all_buttons = []
button_y = 20
for num in range(9):
    
    all_buttons.append(Button(screen, BUTTON_LENGTH, BUTTON_LENGTH, 650, button_y, (255, 255, 255), str(num + 1), num, None))
    button_y += 65

all_buttons.append(Button(screen, 200, 80, 750, 200, (255, 255, 255), "Check Puzzle", None, None))

for row in range(9):
    row_of_cells = []
    for col in range(9):
        color = (255, 255, 255)
        if ((row < 3 or row > 5) and (col < 3 or col > 5)) or ((row < 6 and row > 2 and col < 6 and col > 2)):
            color = (255, 255, 0)
            # new_cell = Cell(screen, SQUARE_LENGTH, row, col, unsolved_board[row][col], (255, 255, 0))
        num = unsolved_board[row][col]
        changable = True
        if num:
            changable = False
        new_cell = Cell(screen, SQUARE_LENGTH, row, col, num, color, changable, solved_board[row][col])
        row_of_cells.append(new_cell)
    all_cells.append(row_of_cells)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
        # (x, y)= pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clicked_cell != None:
                found_it = False
                for button in all_buttons:
                    if button.return_rect().collidepoint(event.pos):
                        # button_pressed = button
                        clicked_cell.new_num(button.return_num())
                        clicked_cell.unselect()
                        clicked_cell.check()
                        clicked_cell = None
                        found_it = True
                
                if found_it == False:
                    clicked_cell.unselect()
                    clicked_cell = None
                


            else:
                for row in all_cells:
                    for cell in row:
                        if cell.return_rect().collidepoint(event.pos):
                            if cell.return_changable():
                                cell.selected()
                                clicked_cell = cell
            
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