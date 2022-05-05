"""
File Name: LarkinsU7AE
Author: Sora Larkins 
Last Date Modified: 04/24/2022
The purpose of this program is to demonstrate an understanding of application development, the creation and use of classes and objects in Python, and using the other tools (selection, iterations, functions, etc.).
"""

# Simple Algorithm
#-------------------------------
# Print title of program
# Welcome user
# - Get user name
# - Check if the user needs instructions
# Use the grid class to create a 20 x 20 cell game board
# Create a class called animal with two attributes: location and lives
# Create a method called 'move' that changes the animal's location one cell up (N), one cell right (E), one cell down (S), or one cell left (W). 
# Extend the animal class to a subclass called cat, and another subclass called dog
# Cat inherits the animal attributes and methods, but also has the following attributes and methods:
# - An attribute called 'attitude' which can have values of 'calm', 'strut' or 'panic'
# - An attribute called 'response' which can have values of 'meow', 'hiss', or 'claw'
# - A method called 'loseLife' which decreases the animal attribute 'lives' by one 
# Dog inherits the animal class attributes and methods, but also has the following attributes:
# - An attribute called 'demeanor' which can have values of 'happy' or 'angry'
# - An attribute called 'action' which can have values of 'sleeping', 'walking', 'barking', 'growling', or 'attacking'
# - A method called 'makePuppies' which resets the current dog to the default state at a random location on the game board and creates another dog object at a random position on the game board with the default state
# Create a tree object that can have a grid position (use an asterisk character to represent a tree.)
# - The number of trees = two per level with random positions on the game board. Tree do not move within the level.
# Create a catNip object that can have a grid position (use 'N' to represent the catNip on the game board)
# - One catNip object per level at a random position on the game board
# Create a player object that can have a name and score
# Create a games object that has a list of names and scores
# End application
#------------------ Begin code ------------------#

# Title of program
print("%40s" % "Stray Cat Strut") 
print()

# Welcome dialogue
name = input("Please enter Player's Name: ") # user can input their name
print()
print("Hello, " + name + ". Welcome to Stray Cat Strut!") # print welcome dialogue with name
print("-" * 40)
print()

def highscore(dictionary, fn = "./high.txt", top_n=0):
  """Store the dict into a file, only store top_n highest values."""
  with open(fn,"w") as f:
    for idx,(name,pts) in enumerate(sorted(dictionary.items(), key= lambda x:-x[1])):
      f.write(f"{name}:{pts}\n")
      if top_n and idx == top_n-1:
        break

def loadHighscore(fn = "./high.txt"):
  """Retrieve dict from file"""
  hs = {}
  try:
    with open(fn,"r") as f:
      for line in f:
        name,_,points = line.partition(":")
        if name and points:
          hs[name]=int(points)
  except FileNotFoundError:
    return ""
  return hs
k = loadHighscore()

print("Player               High Scores:")
print("-"*35)
print(name + "                      " + str(k))
print()

# Instructions
while True:
  answer = input("Do you need instructions, " + name + "?(y/n): ") # ask the user if they want instructions
  print()
  if(answer == "y" or answer == "Y"): # print instructions if user says "yes"
    # Print instruction
    print()
    print("- Objective: The player makes points by moving the cat toward the catNip,")
    print("  and getting the catNip while avoiding any dogs.")
    print("- Actions:")
    print("-- Player can move: N, E, S, W")
    print("-- Player can Meow (M): Makes dogs go to sleep for two turns,") 
    print("   cat goes from Panic to Calm.")
    print("-- Player can Hiss (H): Makes dogs within one grid unit back")
    print("   off one space, token goes from 'C' for calm to 'P' for panic,")
    print("   can now claw.")
    print("-- Player can Claw (C): Makes dogs within one grid reset at a random")
    print("   position, but creates another dog. The cat must have an attitude")
    print("   of panic to enable the claw action. ")
    print()
    break
  elif(answer == "n" or answer == "N"): # skip instructions 
    print("Great, let's get started.")
    print()
    break
  else:
    print("Sorry, I do not understand. Please enter 'y' or 'n'.") # repeat the question if the answer is not 'y' or 'n'
    print()

print("Player: " + name + " Level: 1" + " Score: 0")
print()

# Create Gameboard
class Grid(object):
  """Represents a 20 grid"""
  def __init__(self, rows, columns, fillValue = None):
    self.data = []
    for row in range(rows):
      dataInRow = []
      for column in range(columns):
        dataInRow.append(fillValue)
      self.data.append(dataInRow)
  
  def getWidth(self):
    """Returns the number of columns"""
    return len(self.data[0])

  def getHeight(self):
    """Returns the number of rows"""
    return len(self.data)
  
  def __str__(self):
    """Returns a string representation of the 20 grid."""
    result = "" # initialize the return string
    result += " " + "_"*2 * self.getWidth() + "\n"
    for row in range(self.getHeight()):
      result += "|"
      for col in range(self.getWidth()):
        result += str(self.data[row][col] + " ")
      result += "|\n"
    result += " " + "-" * 2 * self.getWidth() + "\n"
    return result
  def setItem(self, row, column, value):
      """Place an item on the grid"""
      self.data[row][column] = value
  
  def find(self, value):
    """Return the position of a value if found"""
    for row in range(self.getHeight()):
      for column in range(self.getWidth()):
        if self.data[row][column] == value:
          return (row, column)
    return None

class Animal(object):
  """Used to model game icons"""
  def __init__(self, row, column, icon, lives, maxRow, maxCol):
    """Initialize game character"""
    self.currentRowPosition = row
    self.currentColPosition = column
    self.location = chr(self.getCol() + 65) + str(self.getRow())
    self.icon = icon
    self.lives = lives
    self.maxRow = maxRow
    self.maxCol = maxCol
    

  def getRow(self):
    """Return the current row"""
    return self.currentRowPosition

  def getCol(self):
    """Return the current column"""
    return self.currentColPosition

  def getLocation(self):
    """Return the current location"""
    return self.location

  def getIcon(self):
    """Return the current icon"""
    return self.icon

  def __str__(self):
    """Return a string representation of the animal"""
    result = ""
    result += "Icon: " + self.getIcon() + "\n"
    result += "Location: " + self.getLocation() + "\n"
    return result

gameboard = Grid(20, 20, " ") # gameboard dimensions
tom = Animal(0, 0, "C", 9, 20, 20)

for i in range(1):
  gameboard.setItem(i, i, tom.getIcon())
  print(gameboard)
  print(tom)
  gameboard.setItem(i, i, " ")
print()
while True:
  moving = input("Your move (N, S, E, W, H, C, S, X): ")
  if(moving == "N" or moving == "n"):
    break
  elif(moving == "S" or moving == "s"):
    break
  elif(moving == "E" or moving == "e"):
    break
  elif(moving == "W" or moving == "w"):
    break
  elif(moving == "H" or moving == "h"):
    break
  elif(moving == "C" or moving == "c"):
    break
  elif(moving == "S" or moving == "s"):
    break
  elif(moving == "X" or moving == "x"):
    break
print()
print("Thanks for playing the Stray Cat Strut!")