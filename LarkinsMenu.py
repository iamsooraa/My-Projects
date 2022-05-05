"""
File Name: LarkinsMenu
Author: Sora Larkins  
Last Date Modified: 04/19/2022
"""

# Simple algorithm
#

# Import modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo 

# Make a window
ws = Tk()
ws.title("Sora's Menu")
ws.geometry("400x350")
ws.configure(bg = "#e0f8ff")

def about():
  """Displays information about the application"""
  messagebox.showinfo("Menu Example", "How to make a menu in Python using tkinter.")

def select_file():
  """Enables user to select a file"""
  filetype = (
    ("text files", "*.txt"),
    ("All files", "*.*")
  )

  filename = fd.askopenfilename(
    title = "Open a file",
    initialdir = "/",
    filetypes = filetype)
  # shows the path of the file
  showinfo(
    title = "Selected File",
    message = filename
  )
  
# Make a menu bar
menuBar = Menu(ws, bg = "light blue", fg = "white", activebackground = "white", activeforeground = "black")

# Options
file = Menu(menuBar, tearoff = 0, bg = "light blue", fg = "#006796")
file.add_command(label = "New")
file.add_command(label = "Open", command = select_file)
file.add_command(label = "Save")
file.add_command(label = "Save As")
file.add_separator()
file.add_command(label = "Exit", command = ws.quit)
menuBar.add_cascade(label = "File", menu = file)

edit = Menu(menuBar, tearoff = 0, bg = "light blue", fg = "#006796")
edit.add_command(label = "Undo")
edit.add_separator()
edit.add_command(label = "Cut")
edit.add_command(label = "Copy")
edit.add_command(label = "Paste")
menuBar.add_cascade(label = "Edit", menu = edit)

help = Menu(menuBar, tearoff = 0, bg = "light blue", fg = "#006796")
help.add_command(label = "About", command = about)
menuBar.add_cascade(label = "Help", menu = help)

ws.configure(menu = menuBar)
ws.mainloop()