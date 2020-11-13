from tkinter import *
from tkinter import ttk
import math
EPSILON = 0.000001
class Calculator:
  def __init__(self, root, padding = "3 3 12 12", sticky = (N, W, E, S), weight = 1):
    root.title("Calculator")
    self.padding = padding
    self.sticky = sticky
    self.weight = weight
    mainframe = self.setupMainframe(root)
    self.previous = 0.0
    self.result = 0.0
    self.op = ""
    self.setupEntryA(mainframe)
    self.setupLabelResult(mainframe)
    self.setupLabelResult(mainframe)
    self.setupOperatorButtons(mainframe)
    self.addPadding(mainframe, 10)
    #self.createCanvas(mainframe)
  def setupMainframe(self, root):
    mainframe = ttk.Frame(root, padding = self.padding)
    mainframe.grid(column=0, row=0, sticky = self.sticky)
    root.columnconfigure(0, weight=self.weight)
    root.rowconfigure(0, weight=self.weight)
    return mainframe
  def setupEntryA(self, mainframe):
    self.operandA = StringVar()
    operandA_entry = ttk.Entry(mainframe, width = 10, textvariable = self.operandA)
    operandA_entry.grid(column = 2, row = 1, sticky = (W, E))
  def setupLabelResult(self, mainframe):
    self.resultString = StringVar()
    self.resultString.set("0.0")
    ttk.Label(mainframe, textvariable = self.resultString).grid(column = 3, row = 1, sticky=W)
  def setupOperatorButtons(self, mainframe):
    ttk.Button(mainframe, text="+", command=self.add).grid(column=1, row=3, sticky=W)
    ttk.Button(mainframe, text="—", command=self.minus).grid(column=2, row=3, sticky=W)
    ttk.Button(mainframe, text="x", command=self.multiply).grid(column=3, row=3, sticky=W)
    ttk.Button(mainframe, text="/", command=self.divide).grid(column=4, row=3, sticky=W)
    ttk.Button(mainframe, text="=", command=self.display).grid(column=1, row=4, sticky=W)
    ttk.Button(mainframe, text="CLEAR", command=self.clear).grid(column=5, row=3, sticky=W)
  ##def createCanvas(self, mainframe):
    #tk.Canvas(mainframe, top, bg="blue", height=250, width=300)

  def doOperation(self):
    if self.op == '+':
      self.result = self.previous + float(self.operandA.get())
    elif self.op == "-":
      self.result = self.previous - float(self.operandA.get())
    elif self.op == "x":
      self.result = self.previous * float(self.operandA.get())
    elif self.op == "/":
      div = float(self.operandA.get())
      if abs(div) < EPSILON:
        self.resultString.set("YOU TRYING TO BREAK THIS!!! *censored*")
      else:
        self.result = self.previous / float(self.operandA.get())
    self.previous = self.result
    self.operandA.set("")
    self.resultString.set(str(self.result))
  def add(self, *args):
    self.op = "+"
    self.doOperation()
  def minus(self, *args):
    self.op = "-"
    self.doOperation()
  def multiply(self, *args):
    self.op = "x"
    self.doOperation()
  def divide(self, *args):
    self.op = "/"
    self.doOperation()
  def clear(self, *args):
    self.operandA.set("")
    self.resultString.set("0.0")
    self.result = 0
    self.previous = 0
    self.op = ""
  def display(self, *args):
    self.doOperation()
    self.resultString.set(str(self.result))
  def addPadding(self, mainframe, pad = 5): 
    for child in mainframe.winfo_children(): 
            child.grid_configure(padx=pad, pady=pad)

root = Tk()
Calculator(root)
root.mainloop()