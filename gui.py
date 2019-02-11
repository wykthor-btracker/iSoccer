# -*- coding: utf-8 -*-

# #imports
import engine
import tkinter as tk
import numpy as np
from math import log
# #imports

# #variables
# #variables

# #classes


class Grid:

    @staticmethod
    def top(columns, rows):
        if int(log(columns[0]-columns[1] * rows[0]-rows[1], 2)) != log(columns[0]-columns[1] * rows[0]-rows[1], 2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(columns, rows))
        indexes = [(column, row) for column in range(columns[0], int(columns[1]/2)) for row in range(rows[0], rows[1])]
        columns = [columns[0], int(columns[1]/2)]
        return (columns, rows), indexes

    @staticmethod
    def bottom(columns, rows):
        if int(log(columns[0]-columns[1] * rows[0]-rows[1], 2)) != log(columns[0]-columns[1] * rows[0]-rows[1], 2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(columns, rows))
        indexes = [(column, row) for column in range(int(columns[1]/2), columns[1]) for row in range(rows[0], rows[1])]
        columns = [int(columns[1]/2), columns[1]]
        return (columns, rows), indexes

    @staticmethod
    def left(columns, rows):
        if int(log(columns[0] - columns[1] * rows[0] - rows[1], 2)) != log(columns[0] - columns[1] * rows[0] - rows[1],
                                                                           2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(columns, rows))
        indexes = [(column, row) for column in range(columns[0], columns[1]) for row in
                   range(rows[0], int(rows[1]/2))]
        rows = [rows[0], rows[1]/2]
        return (columns, rows), indexes

    @staticmethod
    def right(columns, rows):
        if int(log(columns[0] - columns[1] * rows[0] - rows[1], 2)) != log(columns[0] - columns[1] * rows[0] - rows[1],
                                                                           2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(columns, rows))
        indexes = [(column, row) for column in range(columns[0], columns[1]) for row in
                   range(rows[1]/2, rows[1])]
        rows = [int(rows[1]/2), rows[1]]
        return (columns, rows), indexes


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.shape = ((0, 4), (0, 4))
        self.header = Grid.top(*self.shape)
        self.body = Grid.bottom(*self.shape)

    def createWindow(self, title=""):
        newWindow = tk.Toplevel(self)
        newWindow.wm_title(title)
        return newWindow


class Tela(Application):
    def __init__(self, master):
        super().__init__(master)
# #classes

# #functions
# #functions

# #main


def main():
    root = tk.Tk()
    tela = Tela(root)
    tela.mainloop()

# #main


if __name__ == "__main__":
    main()
