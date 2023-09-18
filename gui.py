# importing libraries + classes + 2d arrays
import pygame
from puzzle import unsolved_board
from puzzle import solved_board
from cell import Cell
from button import Button

pygame.init()


clicked_cell = None
button_pressed = None
WIDTH, HEIGHT = 600,600
SQUARE_LENGTH = int(WIDTH/9)
BUTTON_LENGTH = 40

# creating the pygame screen
screen = pygame.display.set_mode([725, 650])
pygame.display.set_caption("Sudoku")
running = True

# printing instructions in the terminal
print("""Welcome to Playing Sudoku!

""")
print("""Rules
_____________________________
The rules are as any other Sudoku game, the numbers used on the board are 
the integers from 1 to 9. In each row, column, and three by three square, there 
must be one and only one occurance of each of these integers.
 
 """)
print("""How to Play
_____________________________
All of the white numbers on the board are the starting numbers [they are fixed].
Start by clicking on any empty cell on the board. The cell borders will turn 
blue to indicate this selection. From here, you can either click on of the number
buttons on the right to enter that number, or click the same cell again to 
deselect. Autocheck is enabled so the cell borders will either turn red to indicate
an incorrect entry, or stay the same color if it is correct. Keep entering numbers utill
the board is completed! Have fun!

""")


all_cells = []
all_buttons = []
button_y = 20

# creating the 9 buttons

for num in range(9):
    
    all_buttons.append(Button(screen, BUTTON_LENGTH, 650, button_y, (181, 80, 43), str(num + 1), num, None))
    # increasing the y coordinate to stagger buttons
    button_y += 65

# creating a 2d array acting as a board of cells
for row in range(9):
    row_of_cells = []
    for col in range(9):
        color = (230, 155, 57)
        # making it so alternating groups of 3x3 cells on the board are different colors
        if ((row < 3 or row > 5) and (col < 3 or col > 5)) or ((row < 6 and row > 2 and col < 6 and col > 2)):
            color = (224, 216, 101)
        num = unsolved_board[row][col]
        changable = True
        # if there is already a number filled in in the board, the player will not be able to change it
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            # if there has already been a cell that was clicked ...
            if clicked_cell != None:
                found_it = False
                for button in all_buttons:
                    # and then a button was clicked ...
                    if button.return_rect().collidepoint(event.pos):
                        # change the cell to enter the number
                        clicked_cell.new_num(button.return_num(), (93, 135, 240))
                        clicked_cell.unselect()
                        clicked_cell.check()
                        clicked_cell = None
                        found_it = True
                # and a button was not clicked ...
                if found_it == False:
                    # deselect the cell
                    clicked_cell.unselect()
                    clicked_cell = None
                
            # finding the cell that was clicked
            else:
                for row in all_cells:
                    for cell in row:
                        if cell.return_rect().collidepoint(event.pos):
                            if cell.return_changable():
                                cell.selected()
                                clicked_cell = cell
            
    screen.fill((0, 0, 0))
    # displaying all the cells
    for row in all_cells:
        for cell in row:
            cell.show()

    # displaying all the buttons
    for button in all_buttons:
        screen.blit(button.return_surf(), button.return_rect())
        screen.blit(button.return_text(), button.return_text_rect())


    pygame.display.flip()


pygame.quit()