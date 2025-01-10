import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x600+100+100")
        self.titlefont = tkFont.Font(family="Courier", size=40, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=40)
        self.output = tk.Label(text="Output",fg="#111111", bg="#a3f7f1", font=self.titlefont)
        self.output.grid(column=0, row=0, columnspan=4, sticky="NSEW")
        self.b7 = tk.Button(text="7", font=self.buttonFont, command = lambda: self.digitPressed(7))
        self.b7.grid(row=1,column=0, sticky="NSEW")
        self.b8 = tk.Button(text="8", font=self.buttonFont, command = lambda: self.digitPressed(8))
        self.b8.grid(row=1,column=1, sticky="NSEW")
        self.b9 = tk.Button(text="9", font=self.buttonFont, command = lambda: self.digitPressed(9))
        self.b9.grid(row=1,column=2, sticky="NSEW")
        self.b4 = tk.Button(text="4", font=self.buttonFont, command = lambda: self.digitPressed(4))
        self.b4.grid(row=2,column=0, sticky="NSEW")
        self.b5 = tk.Button(text="5", font=self.buttonFont, command = lambda: self.digitPressed(5))
        self.b5.grid(row=2,column=1, sticky="NSEW")
        self.b6 = tk.Button(text="6", font=self.buttonFont, command = lambda: self.digitPressed(6))
        self.b6.grid(row=2,column=2, sticky="NSEW")
        self.b1 = tk.Button(text="1", font=self.buttonFont, command = lambda: self.digitPressed(1))
        self.b1.grid(row=3,column=0, sticky="NSEW")
        self.b2 = tk.Button(text="2", font=self.buttonFont, command = lambda: self.digitPressed(2))
        self.b2.grid(row=3,column=1, sticky="NSEW")
        self.b3 = tk.Button(text="3", font=self.buttonFont, command = lambda: self.digitPressed(3))
        self.b3.grid(row=3,column=2, sticky="NSEW")
        self.plus = tk.Button(text="+", font=self.buttonFont)
        self.plus.grid(row=2,column=3, sticky="NSEW")
        self.minus = tk.Button(text="-", font=self.buttonFont)
        self.minus.grid(row=1,column=3, sticky="NSEW")
        self.equals = tk.Button(text="=", font=self.buttonFont)
        self.equals.grid(row=3,column=3, rowspan=2, sticky="NSEW")
        self.b0 = tk.Button(text="0", font=self.buttonFont, command = lambda: self.digitPressed(0))
        self.b0.grid(row=4,column=1, sticky="NSEW")
        self.bb1 = tk.Button(text="", font=self.buttonFont)
        self.bb1.grid(row=4,column=0, sticky="NSEW")
        self.bb2 = tk.Button(text="", font=self.buttonFont)
        self.bb2.grid(row=4,column=2, sticky="NSEW")

        self.columnconfigure(0,weight=100)
        self.columnconfigure(1,weight=100)
        self.columnconfigure(2,weight=100)
        self.columnconfigure(3,weight=100)
        self.rowconfigure(0,weight=100)
        self.rowconfigure(1,weight=100)
        self.rowconfigure(2,weight=100)
        self.rowconfigure(3,weight=100)
        self.rowconfigure(4,weight=100)
        self.currentNumber = ""
        self.total = 0
        self.operation = "add"
        self.mainloop()  

    def digitPressed(self,num):
        self.currentNumber += str(num)
        self.output.config(text=self.currentNumber)

    def plusPressed(self):
        # set current operation to add
        # put current number into the total
        # start a new current number
        pass

    def minuspressed(self):
        # set current operation to subtract
        # put current number into the total
        # start a new current number
        pass

    def equalsPressed(self):
        # if the current operation is "add"
        #    Add the current number to the total
        #    output the result
        # if the current operation is "subtract"
        #    subtract the current number from the total
        #    output the result
        pass
    
   
app = App()
