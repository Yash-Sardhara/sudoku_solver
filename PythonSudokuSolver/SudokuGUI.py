from tkinter import *

SIZE = 9


class Cell:
    board = [[0]*SIZE]*SIZE

    def __init__(self, gui_root, row, column):
        self.row = row
        self.column = column
        self.input_cell = Entry(gui_root, width=5)
        self.input_cell.grid(row=self.row, column=self.column)

    def save_number(self):
        input_number = self.input_cell.get()
        if input_number:
            self.board[self.row][self.column] = input_number


root = Tk()
cell_grid = [[None]*9]*9
button_solve = Button(root, text="solve")

root.title("Sudoku Solver")
button_solve.grid(row=9, column=6)
for i in range(9):
    for j in range(9):
        cell_grid[i][j] = Cell(root, i, j)


root.mainloop()
