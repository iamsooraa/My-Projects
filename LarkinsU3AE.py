"""
File Name: LarkinsU3AE
Author: Sora Larkins
Last Date Modified: 02/11/2022
The purpose of this program is to demonstrate decimal, binary, and hexadecimal number systems.
"""

# Simple algorithm 
#------------------
# Print title of program
# Welcome user
# - Get user name
# - Check if the user needs instructions
# Get parameters for binary and hexadecimal conversions
# - Number range for input (0-255)
# Create exit function out of conversion
# - Enter 'x' to end program
# Exit/Thank you Dialogue
# - Thank user for using VCA
# Produce conversion table
# - Print handy table at the end of program
# - Displays decimal, binary, and hexadecimal conversions
# End application
#------------------- Begin Code -------------------#

# Title of program
print("%40s" % "VCA Running") 
print()

# Welcome dialogue
name = input("Please provide the name you would like to use for this session: ") # user can input their name
print()
print("Hello, " + name + ". Welcome to the Value Conversion Application (VCA).") # print welcome dialogue with name
print()

# Instructions
answer = input("Do you need instructions, " + name + "?(y/n): ") # ask the user if they want instructions
print("")
if(answer == "y"): # print instructions if user says "yes"
# Print instruction
  print("- The application will ask you for decimal value that is between 0 and 255.")
  print("- Please enter the value and hit the Enter key.")
  print("- The application will respond with the binary and hexadecimal equivalents.")
  print("- The application will continue to ask you for values to convert.")
  print("- When you are ready to exit, enter the letter 'x'.")
  print("- Upon exitting, the application will print a handy conversion table.")
  print()
  print("When you are ready to start converting, hit the Enter key.") 
  input("") # press enter to start conversion
if(answer == "n"): # skip instructions
  print("When you are ready to start converting, hit the Enter key.") 
  input("") # press enter to start conversion

# Hexadecimal and Binary Conversion
x = "x"
while True:
    print("Please enter a positive integer to convert (enter 'x' to end): ") 
    value = input()
    # exit dialogue
    if value == x:
      break # enter "x" to end program
    # converts values
    else:
      num = int(value) # input int value for conversion
      if num <= 255:
        binOut = bin(num) 
        hexOut = hex(num).upper()
        print("Results: ", num, " equals " + binOut[2:] + " in Binary, and " + hexOut[2:] + " in the Hexadecimal notation.") # print binary number and hexadecimal notation
        print() 
print()

# Thank you dialogue
print("Thank you " + name + " for using VCA. Here is a handy table: ") 
print()

# Print handy table
print("Handy Dandy Decimal Binary Hexadecimal Conversion Table") # table title
print("-"*46) # table top border
print("Decimal           Binary           Hexadecimal") # table headers
print("-"*46) # table bottom border
lowerbound = 0
upperbound = 255 
for count in range(lowerbound, upperbound+1):
  value *= count
  bina = bin(count)[2:] # binary conversion
  hexa = hex(count)[2:] # hexademical conversion
  print("%3s%15s" % (count, value) + "%6s%14s" % (bina, hexa)) # print column values (decimal, binary, and hexadecimal)
  