from tkinter import *
from math import sqrt
from SudokuSearchSolver import SudokuSearchSolver
from SudokuSearchSolver import print_board

SIZE = 9


class Cell:
    def __init__(self, gui_root, row, column):
        self.row = row
        self.column = column
        self.input_cell = Entry(gui_root, width=5)
        self.input_cell.grid(row=self.row, column=self.column)

    def get_number(self):
        input_number = self.input_cell.get()
        if input_number:
            return input_number
        else:
            return 0

    def clear(self):
        self.input_cell.delete(0, END)


def solve_board(cell_grid, size):
    sudoku_board = []

    for i in range(size):
        sudoku_board_row = []
        for j in range(size):
            sudoku_board_row.append(cell_grid[i][j].get_number())
        sudoku_board.append(sudoku_board_row)

    SudokuSearchSolver.search_solve(sudoku_board, [0, 0])
    print_board(sudoku_board)


def clear_grid(cell_grid, size):
    for i in range(size):
        for j in range(size):
            cell_grid[i][j].clear()


root = Tk()
root.title("Sudoku Solver")

cell_grid = []
for i in range(9):
    cell_grid_row = []
    for j in range(9):
        cell_grid_row.append(Cell(root, i, j))
    cell_grid.append(cell_grid_row)

button_solve = Button(root, text="solve", command=lambda: solve_board(cell_grid, SIZE))\
    .grid(row=SIZE, column=int((sqrt(SIZE)-1)*sqrt(SIZE)), columnspan=int((sqrt(SIZE)-1)*sqrt(SIZE)))

button_clear = Button(root, text="Clear", command=lambda: clear_grid(cell_grid, SIZE))\
    .grid(row=SIZE, column=int((sqrt(SIZE)-2)*sqrt(SIZE)), columnspan=int((sqrt(SIZE)-1)*sqrt(SIZE)))

root.mainloop()
