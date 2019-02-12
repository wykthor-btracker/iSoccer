# -*- coding: utf-8 -*-

# #imports
import engine
import tkinter as tk
from tkinter import N,S,E,W
from copy import deepcopy
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

    @staticmethod
    def stack(shape,orientation):
        newShape = deepcopy(shape)
        if(orientation=="h"):
            newShape["row"][0] += 1
        else:
            newShape["column"][0] += 1
        return newShape


class Application(tk.Frame):
    def __init__(self, dataframe, master=None, shape=16):
        super().__init__(master)
        self.master = master
        self.shape = ((0, shape), (0, shape))
        self.header = Grid.top(*self.shape)
        self.body = Grid.bottom(*self.shape)
        self.master.grid_rowconfigure(self.body["row"][0], weight=1)
        self.master.grid_columnconfigure(self.body["column"][0], weight=1)
        
        self.header =tk.Frame(self.master, width=450, height=50, pady=3)
        self.body =tk.Frame(self.master, width=50, height=40, padx=3, pady=3)

        # layout all of the main containers
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1) #The coordinates for the largest frame

        self.header.grid(row=0, sticky="ew")
        self.body.grid(row=1, sticky="nsew")#, column=0 by default


        self.textBox(self.master,dataframe,"bla")
        # self.loginWindow(self.master, dataframe)

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
        Grid.toTk(tk.Button(root, text="Entrar", command=lambda: self.firstScreen(self.master))
                  , butt, sticky=E, rowspan=5)
        self.textBox(root,dataframe,"Titulo")

    def firstScreen(self, root):
        self.clean()
        title = tk.Label(root, text="iSoccer")
        Grid.toTk(title, self.header)
        leftButton = Grid.left(**self.body)
        rightButton = Grid.stack(leftButton,"h")

        Grid.toTk(tk.Button(root, text="Recursos físicos"), leftButton, sticky=E)
        Grid.toTk(tk.Button(root, text="Recursos humanos"), rightButton)

    def textBox(self, root, dataframe, header):
        # create the widgets for the top frame
        model_label =tk.Label(self.header, text='Bem vindo ao iSoccer, o que deseja administrar?')

        # layout the widgets in the top frame
        model_label.grid(row=0, columnspan=3)

        # create the center widgets

        ctr_mid = tk.Frame(self.body)

        ctr_mid.grid(row=0, column=1, sticky="nsew")
        Grid.toTk(tk.Button(ctr_mid, text="Recursos humanos"), Grid.left((0, 4), (0, 4)))
        Grid.toTk(tk.Button(ctr_mid, text="Recursos físicos"), Grid.right((0, 4), (0, 4)))

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
    tela = Application(ff.info(), root, 8)
    tela.mainloop()

# #main


if __name__ == "__main__":
    main()
