"""
Author: Sora Larkins
File Name: Calculator
Last Dat Modified: 4/12/2022
"""
"""
expression = "3 * 4"
total = str(eval(expression))
print(total)
"""

# import everything from tkinter mod
from tkinter import *

expression = ""

def press(num):
  # point out global expression variable
  global expression
  # concatenate button press
  expression += str(num)
  # update expression using the set method
  equation.set(expression)

def equalPress():
  global expression
  total = str(eval(expression))
  equation.set(total)
  # empty the expression 
  expression = ""

def clear():
  global expression
  expression = ""
  equation.set("")

if __name__ == "__main__":
  # create GUI window
  gui = Tk()
  # set background color
  gui.configure(bg = "light pink")
  # set the title of the GUI
  gui.title("Sora's Calculator")
  # set the size of the window
  gui.geometry("305x170")
  # create and place the expression window
  equation = StringVar()
  expression_field = Entry(gui, textvariable = equation)
  expression_field.grid(columnspan = 4, ipadx = 70)

  # create and place buttons and functions
  button1 = Button(gui, text = " 1 ", fg = "black", bg = "white", command = lambda: press(1), height = 1, width = 5)
  button1.grid(row = 2, column = 0)

  button2 = Button(gui, text = " 2 ", fg = "black", bg = "white", command = lambda: press(2), height = 1, width = 5)
  button2.grid(row = 2, column = 1)

  button3 = Button(gui, text = " 3 ", fg = "black", bg = "white", command = lambda: press(3), height = 1, width = 5)
  button3.grid(row = 2, column = 2)

  button4 = Button(gui, text = " 4 ", fg = "black", bg = "white", command = lambda: press(4), height = 1, width = 5)
  button4.grid(row = 3, column = 0)

  button5 = Button(gui, text = " 5 ", fg = "black", bg = "white", command = lambda: press(5), height = 1, width = 5)
  button5.grid(row = 3, column = 1)

  button6 = Button(gui, text = " 6 ", fg = "black", bg = "white", command = lambda: press(6), height = 1, width = 5)
  button6.grid(row = 3, column = 2)

  button7 = Button(gui, text = " 7 ", fg = "black", bg = "white", command = lambda: press(7), height = 1, width = 5)
  button7.grid(row = 4, column = 0)

  button8 = Button(gui, text = " 8 ", fg = "black", bg = "white", command = lambda: press(8), height = 1, width = 5)
  button8.grid(row = 4, column = 1)

  button9 = Button(gui, text = " 9 ", fg = "black", bg = "white", command = lambda: press(9), height = 1, width = 5)
  button9.grid(row = 4, column = 2)

  button0 = Button(gui, text = " 0 ", fg = "black", bg = "white", command = lambda: press(0), height = 1, width = 5)
  button0.grid(row = 5, column = 1)

  plus = Button(gui, text = " + ", fg = "black", bg = "white", command = lambda: press("+"), height = 1, width = 5)
  plus.grid(row = 2, column = 3)

  minus = Button(gui, text = " - ", fg = "black", bg = "white", command = lambda: press("-"), height = 1, width = 5)
  minus.grid(row = 3, column = 3)

  mult = Button(gui, text = " * ", fg = "black", bg = "white", command = lambda: press("*"), height = 1, width = 5)
  mult.grid(row = 4, column = 3)

  div = Button(gui, text = " / ", fg = "black", bg = "white", command = lambda: press("/"), height = 1, width = 5)
  div.grid(row = 5, column = 3)

  equal = Button(gui, text = " = ", fg = "black", bg = "white", command = equalPress, height = 1, width = 5)
  equal.grid(row = 5, column = 2)

  clear = Button(gui, text = " Clear ", fg = "black", bg = "white", command = clear, height = 1, width = 5)
  clear.grid(row = 5, column = 0)

  dec = Button(gui, text = " . ", fg = "black", bg = "white", command = lambda: press("."), height = 1, width = 5)
  dec.grid(row = 6, column = 3)
  
  # start the GUI
  gui.mainloop()

  
  