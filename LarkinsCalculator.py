"""
Author: Sora Larkins
File Name: LarkinsCalculator
Last Dat Modified: 4/12/2022
Purpose: The purpose of this program is to create a simple calculator using the Tkinter Python binding to the Tk GUI toolkit.
"""

# Simple Algorithm
#-----------------------------------------------#
# Import tkinter module
# Define a press number fucntion for number buttons
# Defnie an equal button function
# Define a clear button function
# Create a main loop for GUI
# Create a GUI window using tkinter
# - Set background color
# - Set the title of GUI
# - Set the size of the window
# - Create the text entry box
# Create number buttons for the calculator
# Create math function buttons for the calculator
# Start GUI
#----------------- Begin Code ------------------#

# import everything from tkinter mod
from tkinter import *

expression = ""

# Define a press number function
def press(num):
  # point out global expression variable
  global expression
  # concatenate button press
  expression += str(num)
  # update expression using the set method
  equation.set(expression)

# Define an equal button function
def equalPress():
  global expression
  total = str(eval(expression))
  equation.set(total)
  # empty the expression 
  expression = ""

# Define a clear button function
def clear():
  global expression
  expression = ""
  equation.set("")

# GUI Main Loop
if __name__ == "__main__":
  # create GUI window
  gui = Tk()
  # set background color
  gui.configure(bg = "light pink")
  # set the title of the GUI
  gui.title("   Sora's Calculator")
  # set the size of the window
  gui.geometry("310x170")
  # create and place the expression window
  equation = StringVar()
  expression_field = Entry(gui, textvariable = equation)
  expression_field.grid(columnspan = 4, ipadx = 70)

  # create and place buttons and functions
  button1 = Button(gui, text = " 1 ", fg = "magenta", bg = "white", command = lambda: press(1), height = 1, width = 6)
  button1.grid(row = 2, column = 0) 

  button2 = Button(gui, text = " 2 ", fg = "magenta", bg = "white", command = lambda: press(2), height = 1, width = 6)
  button2.grid(row = 2, column = 1)

  button3 = Button(gui, text = " 3 ", fg = "magenta", bg = "white", command = lambda: press(3), height = 1, width = 6)
  button3.grid(row = 2, column = 2)

  button4 = Button(gui, text = " 4 ", fg = "magenta", bg = "white", command = lambda: press(4), height = 1, width = 6)
  button4.grid(row = 3, column = 0)

  button5 = Button(gui, text = " 5 ", fg = "magenta", bg = "white", command = lambda: press(5), height = 1, width = 6)
  button5.grid(row = 3, column = 1)

  button6 = Button(gui, text = " 6 ", fg = "magenta", bg = "white", command = lambda: press(6), height = 1, width = 6)
  button6.grid(row = 3, column = 2)

  button7 = Button(gui, text = " 7 ", fg = "magenta", bg = "white", command = lambda: press(7), height = 1, width = 6)
  button7.grid(row = 4, column = 0)

  button8 = Button(gui, text = " 8 ", fg = "magenta", bg = "white", command = lambda: press(8), height = 1, width = 6)
  button8.grid(row = 4, column = 1)

  button9 = Button(gui, text = " 9 ", fg = "magenta", bg = "white", command = lambda: press(9), height = 1, width = 6)
  button9.grid(row = 4, column = 2)

  button0 = Button(gui, text = " 0 ", fg = "magenta", bg = "white", command = lambda: press(0), height = 1, width = 6)
  button0.grid(row = 5, column = 1)

  plus = Button(gui, text = " + ", fg = "magenta", bg = "white", command = lambda: press("+"), height = 1, width = 6)
  plus.grid(row = 2, column = 3)

  minus = Button(gui, text = " - ", fg = "magenta", bg = "white", command = lambda: press("-"), height = 1, width = 6)
  minus.grid(row = 3, column = 3)

  mult = Button(gui, text = " * ", fg = "magenta", bg = "white", command = lambda: press("*"), height = 1, width = 6)
  mult.grid(row = 4, column = 3)

  div = Button(gui, text = " / ", fg = "magenta", bg = "white", command = lambda: press("/"), height = 1, width = 6)
  div.grid(row = 5, column = 3)

  equal = Button(gui, text = " = ", fg = "magenta", bg = "white", command = equalPress, height = 1, width = 6)
  equal.grid(row = 5, column = 2)

  clear = Button(gui, text = " Clear ", fg = "magenta", bg = "white", command = clear, height = 1, width = 6)
  clear.grid(row = 6, column = 3)

  dec = Button(gui, text = " . ", fg = "magenta", bg = "white", command = lambda: press("."), height = 1, width = 6)
  dec.grid(row = 5, column = 0)

  sq = Button(gui, text = " ** ", fg = "magenta", bg = "white", command = lambda: press("**"), height = 1, width = 6)
  sq.grid(row = 6, column = 2)

  # start the GUI
  gui.mainloop()