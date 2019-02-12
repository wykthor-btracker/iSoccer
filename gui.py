# -*- coding: utf-8 -*-

# #imports
import engine
import tkinter as tk
from tkinter import N,S,E,W
import numpy as np
from math import log
# #imports

# #variables
# #variables

# #classes


class Grid:

    @staticmethod
    def top(column, row):
        if int(log(abs(column[0]-column[1] * row[0]-row[1]), 2)) != log(abs(column[0]-column[1] * row[0]-row[1]), 2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(column, row))
        # indexes = [(column, row) for column in range(column[0], int(column[1]/2)) for row in range(row[0], row[1])]
        column = [column[0], int((column[0]+column[1])/2)]
        return {"column": column, "row": row}#, indexes

    @staticmethod
    def bottom(column, row):
        if int(log(abs(column[0]-column[1] * row[0]-row[1]), 2)) != log(abs(column[0]-column[1] * row[0]-row[1]), 2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(column, row))
        # indexes = [(column, row) for column in range(int(column[1]/2), column[1]) for row in range(row[0], row[1])]
        column = [int((column[0]+column[1])/2), column[1]]
        return {"column": column, "row": row}#, indexes

    @staticmethod
    def left(column, row):
        if int(log(abs(column[0] - column[1] * row[0] - row[1]), 2)) != log(abs(column[0] - column[1] * row[0] - row[1]),
                                                                           2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(column, row))
        # indexes = [(column, row) for column in range(column[0], column[1]) for row in
        #            range(row[0], int(row[1]/2))]
        row = [row[0], int((row[0]+row[1]))/2]
        return {"column": column, "row": row}#, indexes

    @staticmethod
    def right(column, row):
        if int(log(abs(column[0] - column[1] * row[0] - row[1]), 2)) != log(abs(column[0] - column[1] * row[0] - row[1]),
                                                                            2):
            raise Exception(
                "({},{}) são dimensões inválidas, linha*coluna deve ser uma potência de 2.".format(column, row))
        # indexes = [(column, row) for column in range(column[0], column[1]) for row in
        #            range(row[1]/2, row[1])]
        row = [int((row[0]+row[1])/2), row[1]]
        return {"column": column, "row": row}#, indexes

    @staticmethod
    def toTk(widget, shape, **kwargs):
        widget.grid(column=shape["row"][0], row=shape["column"][0],**kwargs) # Tkinter is weird


class Application(tk.Frame):
    def __init__(self, dataframe, master=None):
        super().__init__(master)
        self.master = master
        self.shape = ((0, 16), (0, 16))
        self.header = Grid.top(*self.shape)
        self.body = Grid.bottom(*self.shape)
        self.loginWindow(self.master, dataframe)

    def loginWindow(self, root, dataframe):
        self.clean()
        username = Grid.top(**self.body)
        password = Grid.bottom(**self.body)

        name = tk.Label(root, text="Nome")
        textInput = tk.Entry(root)

        passwor = tk.Label(root, text="Senha")
        passInput = tk.Entry(root)

        Grid.toTk(name, Grid.left(**username))
        Grid.toTk(textInput, Grid.right(**username))

        Grid.toTk(passwor, Grid.left(**password))
        Grid.toTk(passInput, Grid.right(**password))

        butt = Grid.right(**Grid.bottom(**password))
        Grid.toTk(tk.Button(root, text="Entrar", command=lambda: self.textBox(root, dataframe, "Sobre os funcionários"))
                  , butt, sticky=E, rowspan=5)

    def textBox(self, root, dataframe, header):
        self.clean()
        name = tk.Label(root, text=dataframe)
        Grid.toTk(tk.Label(root, text=header),self.header)
        Grid.toTk(name, self.body)

    def createWindow(self, title=""):
        newWindow = tk.Toplevel(self.master)
        newWindow.header = Grid.top(*self.shape)
        newWindow.body = Grid.bottom(*self.shape)
        newWindow.wm_title(title)
        return newWindow

    def clean(self):
        [instance.destroy() for instance in self.master.winfo_children()]

# #classes

# #functions
# #functions

# #main


def main():
    ff = engine.Pessoas([engine.Funcionario("wykthor", "a@a.a", "9999-9999", "00000000000", "30", cargo="Médico", crm=24),
                         engine.Funcionario("wykthorr", "a@a.aa", "9999-9998", "10000000000", "32", cargo="Técnico")])
    root = tk.Tk()
    tela = Application(ff.info(),root)
    tela.mainloop()

# #main


if __name__ == "__main__":
    main()
