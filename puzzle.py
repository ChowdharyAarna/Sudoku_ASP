solved_board = [
    [8, 7, 5, 9, 2, 1, 3, 4, 6],
    [3, 6, 1, 7, 5, 4, 8, 9, 2],
    [2, 4, 9, 8, 6, 3, 7, 1, 5],
    [5, 8, 4, 6, 9, 7, 1, 2, 3],
    [7, 1, 3, 2, 4, 8, 6, 5, 9],
    [9, 2, 6, 1, 3, 5, 4, 8, 7],
    [6, 9, 7, 4, 1, 2, 5, 3, 8],
    [1, 5, 8, 3, 7, 9, 2, 6, 4],
    [4, 3, 2, 5, 8, 6, 9, 7, 1]
    ]

unsolved_board = [
    [None, 7, None, None, 2, None, None, 4, 6],
    [None, 6, None, None, None, None, 8, 9, None],
    [2, None, None, 8, None, None, 7, 1, 5],
    [None, 8, 4, None, 9, 7, None, None, None],
    [7, 1, None, None, None, None, None, 5, 9],
    [None, None, None, 1, 3, None, 4, 8, None],
    [6, 9, 7, None, None, 2, None, None, 8],
    [None, 5, 8, None, None, None, None, 6, None],
    [4, 3, None, None, 8, None, None, 7, None]
    ]

def check_full_puzzle(unsolved, solved):
    for row_num in range(9):
        for col_num in range(9): 
            if solved[row_num][col_num] != unsolved[row_num][col_num]:
                return False
    return True

def check_one_square(square_row, square_column, unsolved, solved):
    return unsolved[square_row][square_column] == solved[square_row][square_column]


# print(check_full_puzzle(unsolved_board, solved_board))