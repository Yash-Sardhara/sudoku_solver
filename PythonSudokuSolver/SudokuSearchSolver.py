from math import sqrt
from time import time


class SudokuSearchSolver:
    SIZE = 9

    @staticmethod
    def check_row(board, row, column):
        for i in range(SudokuSearchSolver.SIZE):
            if i != column:
                if board[row][i] == board[row][column]:
                    return False
            else:
                if board[row][column] > SudokuSearchSolver.SIZE or board[row][column] <= 0:
                    return False
        return True

    @staticmethod
    def check_column(board, row, column):
        for i in range(SudokuSearchSolver.SIZE):
            if i != row:
                if board[i][column] == board[row][column]:
                    return False
            else:
                if board[row][column] > SudokuSearchSolver.SIZE or board[row][column] <= 0:
                    return False
        return True

    @staticmethod
    def check_box(board, row, column):
        box_row = row // sqrt(SudokuSearchSolver.SIZE)
        box_column = column // sqrt(SudokuSearchSolver.SIZE)

        for i in range(int(box_row * sqrt(SudokuSearchSolver.SIZE)),
                       int((box_row + 1) * sqrt(SudokuSearchSolver.SIZE))):
            for j in range(int(box_column * sqrt(SudokuSearchSolver.SIZE)),
                           int((box_column + 1) * sqrt(SudokuSearchSolver.SIZE))):
                if i != row or j != column:
                    if board[i][j] == board[row][column]:
                        return False
                else:
                    if board[row][column] > SudokuSearchSolver.SIZE or board[row][column] <= 0:
                        return False
        return True

    @staticmethod
    def check_all(board, row, column):
        return SudokuSearchSolver.check_box(board, row, column) \
               and SudokuSearchSolver.check_row(board, row, column) \
               and SudokuSearchSolver.check_column(board, row, column)

    @staticmethod
    def search_solve(board, position):
        if position[0] == SudokuSearchSolver.SIZE:
            return True

        if board[position[0]][position[1]]:
            position[1] += 1
            if position[1] == SudokuSearchSolver.SIZE:
                position[0], position[1] = position[0] + 1, 0
                return SudokuSearchSolver.search_solve(board, position)
            return SudokuSearchSolver.search_solve(board, position)

        for i in range(1, SudokuSearchSolver.SIZE + 1):
            row, column = position
            board[row][column] = i
            if SudokuSearchSolver.check_all(board, row, column):
                column += 1
                if column == SudokuSearchSolver.SIZE:
                    row, column = row + 1, 0
                if SudokuSearchSolver.search_solve(board, [row, column]):
                    return True

        board[position[0]][position[1]] = 0
        return False


'''
SUDOKU_BOARD = [[1, 0, 6, 0, 0, 2, 3, 0, 0],
                [0, 5, 0, 0, 0, 6, 0, 9, 1],
                [0, 0, 9, 5, 0, 1, 4, 6, 2],
                [0, 3, 7, 9, 0, 5, 0, 0, 0],
                [5, 8, 1, 0, 2, 7, 9, 0, 0],
                [0, 0, 0, 4, 0, 8, 1, 5, 7],
                [0, 0, 0, 2, 6, 0, 5, 4, 0],
                [0, 0, 4, 1, 5, 0, 6, 0, 9],
                [9, 0, 0, 8, 7, 4, 2, 1, 0]]
'''

SUDOKU_BOARD = [[8, 0, 0, 4, 0, 6, 0, 0, 7],
                [0, 0, 0, 0, 0, 0, 4, 0, 0],
                [0, 1, 0, 0, 0, 0, 6, 5, 0],
                [5, 0, 9, 0, 3, 0, 7, 8, 0],
                [0, 0, 0, 0, 7, 0, 0, 0, 0],
                [0, 4, 8, 0, 2, 0, 1, 0, 3],
                [0, 5, 2, 0, 0, 0, 0, 9, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [3, 0, 0, 9, 0, 2, 0, 0, 5]]

SIZE = 9

def print_board(board):
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end=" ")
        print("")
    return


def execute():
    start_time = time()
    solved_board = SUDOKU_BOARD
    SudokuSearchSolver.search_solve(solved_board, [0, 0])
    print_board(SUDOKU_BOARD)
    print()
    print_board(solved_board)
    print("Execution Time: ", time()-start_time)

