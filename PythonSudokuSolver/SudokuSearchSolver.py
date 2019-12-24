from math import sqrt

SIZE = 9
SUDOKU_BOARD = [[1, 0, 6, 0, 0, 2, 3, 0, 0],
                [0, 5, 0, 0, 0, 6, 0, 9, 1],
                [0, 0, 9, 5, 0, 1, 4, 6, 2],
                [0, 3, 7, 9, 0, 5, 0, 0, 0],
                [5, 8, 1, 0, 2, 7, 9, 0, 0],
                [0, 0, 0, 4, 0, 8, 1, 5, 7],
                [0, 0, 0, 2, 6, 0, 5, 4, 0],
                [0, 0, 4, 1, 5, 0, 6, 0, 9],
                [9, 0, 0, 8, 7, 4, 2, 1, 0]]


def check_row(board, row, column):
    for i in range(SIZE):
        if i != column:
            if board[row][i] == board[row][column]:
                return False
        else:
            if board[row][column] > SIZE or board[row][column] <= 0:
                return False
    return True


def check_column(board, row, column):
    for i in range(SIZE):
        if i != row:
            if board[i][column] == board[row][column]:
                return False
        else:
            if board[row][column] > SIZE or board[row][column] <= 0:
                return False
    return True


def check_box(board, row, column):
    box_row = row//sqrt(SIZE)
    box_column = column//sqrt(SIZE)

    for i in range(int(box_row*sqrt(SIZE)), int((box_row + 1)*sqrt(SIZE))):
        for j in range(int(box_column * sqrt(SIZE)), int((box_column + 1) * sqrt(SIZE))):
            if i != row or j != column:
                if board[i][j] == board[row][column]:
                    return False
            else:
                if board[row][column] > SIZE or board[row][column] <= 0:
                    return False
    return True


def check_all(board, row, column):
    return check_box(board, row, column)\
           and check_row(board, row, column)\
           and check_column(board, row, column)


def search_solve(board, position):
    if position[0] == SIZE:
        return True

    if board[position[0]][position[1]]:
        position[1] += 1
        if position[1] == SIZE:
            position[0], position[1] = position[0] + 1, 0
            return search_solve(board, position)
        return search_solve(board, position)

    for i in range(1, SIZE+1):
        row, column = position
        board[row][column] = i
        if check_all(board, row, column):
            column += 1
            if column == SIZE:
                row, column = row+1, 0
            if search_solve(board, [row, column]):
                return True

    board[position[0]][position[1]] = 0
    return False


def print_board(board):
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end=" ")
        print("")
    return


def execute():
    solved_board = SUDOKU_BOARD
    search_solve(solved_board, [0, 0])
    print_board(SUDOKU_BOARD)
    print()
    print_board(solved_board)


execute()

