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
    def __init__(self, dataframes, master=None, shape=16):
        super().__init__(master)
        self.dataframes = dataframes
        self.master = master
        self.shape = ((0, shape), (0, shape))
        self.header = Grid.top(*self.shape)
        self.body = Grid.bottom(*self.shape)
        self.master.grid_rowconfigure(self.body["row"][0], weight=1)
        self.master.grid_columnconfigure(self.body["column"][0], weight=1)
        
        self.header =tk.Frame(self.master, width=450, height=50, pady=3,background="blue")
        self.body =tk.Frame(self.master, width=50, height=40, padx=3, pady=3,background="black")

        # layout all of the main containers
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1) #The coordinates for the largest frame

        self.header.grid(row=0, sticky="ew")
        self.body.grid(row=1, sticky="ew")#, column=0 by default
        self.loginWindow()

    def loginWindow(self):
        self.clean()
        name = tk.Label(self.header, text="Nome")
        textInput = tk.Entry(self.header)

        password = tk.Label(self.header, text="Senha")
        passInput = tk.Entry(self.header)

        butt = tk.Button(self.body, text="Entrar", command=lambda: self.firstScreen())

        name.grid(column=0,row=0)
        textInput.grid(column=0,row=1,sticky=E)

        password.grid(column=1,row=0)
        passInput.grid(column=1,row=1,sticky=E)

        butt.grid()

    def firstScreen(self):
        self.clean()
        # create the widgets for the top frame
        model_label = tk.Label(self.header, text='Bem vindo ao iSoccer, o que deseja administrar?')

        # layout the widgets in the top frame
        model_label.grid(row=0, columnspan=3)

        # create the center widgets

        ctr_mid = tk.Frame(self.body)

        ctr_mid.grid(row=0, column=1, sticky="nsew")
        buttHuman = tk.Button(ctr_mid, text="Recursos humanos",command= lambda: self.humanWindow())
        buttPhysic = tk.Button(ctr_mid, text="Recursos físicos")

        buttHuman.grid(column=0, row=0)
        buttPhysic.grid(column=1, row=0)

    def humanWindow(self):
        self.clean()
        buttTime = tk.Button(self.body, text="Informações do Time", command=lambda: self.textBox(self.humanWindow,
                                                                                                 self.dataframes[0]))
        buttFunc = tk.Button(self.body, text="Informações dos funcionários", command=lambda: self.textBox(self.humanWindow,
                                                                                                 self.dataframes[0]))
        buttSoci = tk.Button(self.body, text="Informações dos sócios", command=lambda: self.textBox(self.humanWindow,
                                                                                                 self.dataframes[0]))
        buttTime.grid(row=0, sticky=E+W)
        buttFunc.grid(row=1, sticky=E+W)
        buttSoci.grid(row=2, sticky=E+W)

    def textBox(self, lastWindow, data):
        self.clean()
        text = tk.Label(self.header, text=data)
        butt = tk.Button(self.body, text="Voltar", command=lambda: lastWindow())
        text.grid()
        butt.grid()

    def createWindow(self):
        newWindow = tk.Toplevel(self.master)
        newWindow.header = Grid.top(*self.shape)
        newWindow.body = Grid.bottom(*self.shape)
        newWindow.wm_title(title)
        return newWindow

    def clean(self):
        [instance.destroy() for instance in self.header.winfo_children()]
        [instance.destroy() for instance in self.body.winfo_children()]

# #classes

# #functions
# #functions

# #main


def main():
    ff = engine.Pessoas([engine.Funcionario("wykthor", "a@a.a", "9999-9999", "00000000000", "30", cargo="Médico", crm=24),
                         engine.Funcionario("wykthorr", "a@a.aa", "9999-9998", "10000000000", "32", cargo="Técnico")])
    root = tk.Tk()
    tela = Application([ff.info()], root, 8)
    tela.mainloop()

# #main


if __name__ == "__main__":
    main()
