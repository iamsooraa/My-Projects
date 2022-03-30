"""
Program: Dice Roll Simulation Application
Author: Sora Larkins
Last Date Modified: 03/19/2022
The purpose of this program is to demonstrate the use of lists, dictionaries, iand Python modules to create a dice simulation .
"""

# Simple algorithm
#-----------------------------------------------------
# Welcome user
# - Get user name
# - Check if the user needs instructions
# Import any necessary Python modules
# Allow user to select the number of dice, the number of faces, manual or automatic roll
# Produce descriptive statistics report
# Produce a visualization of the results of the simulation
# - Print dice roll
# - Print list contents
# - Print bar chart with possible outcomes, counts, & percentages
# End application
#------------------ Begin code ------------------#

# Import Python modules
import random 
from time import sleep # pause the program between rolls
import statistics # for the descriptive statistics table

# Initialize similation variables
rollSimulation = True # Boolean for loop

# Welcome user
print("%40s" % "Dice Simulation App")
print()
name = input("Please provide the name you would like to use for this session: ")
print()
print("Hello, " + name + ". Welcome to the Dice Simulation App (DSA).")
print()

# Instructions
while True:
  instructions = input("Do you need instructions " + name + "? (y/n): ")
  print()
  if (instructions == "y" or instructions == "Y"):
    print("- The application will ask you the desired number of dice and dice faces you want to simulate.")
    print("- Your responses should be an integer greater than 0.")
    print("- The application will ask you if you want to manually, 'm', or automatically, 'a', roll the simulated dice.")
    print("- Enter 'x' to exit the simulation.")
    print("- The application will print the simulated roll results.")
    print("- The application will print a descriptive statistics table when the dice is rolled at least 2 times.")
    print()
    ready = input("When you are ready to start the simulation, hit the Enter key.")
    print()
    break
  elif (instructions == "n" or instructions == "N"):
    ready = input("When you are ready to start the application, hit the Enter key.")
    print()
    break
  else:
    print("Sorry, I do not understand. Please enter 'y' or 'n'.")
    print()

# Main Loop
while True: # while loop for the main loop
  rollDice = 0 # set the number of times the app rolls the dice
  
  # Number of Dice
  while True: 
    answer = input("How many dice to you want to roll? : ")
    print()
    DICE_NUMBER = int(answer) # convert the answer to an integer
    if DICE_NUMBER > 0: # user must enter a number larger than 0
      break
    else:
      print("Please enter an integer greater than zero.")
      print()
  
  # Number of Sides 
  while True: 
    answer = input("How many faces do you want on each die? :  ")
    print()
    faces = int(answer)  # convert the answer to an integer
    if faces > 0: # user must enter a number larger than 0
      break
    else:
      print("Please enter an integer greater than zero.")
      print()
  
  # Rolling the Dice
  while True: 
    print("Do you want to roll manually or automaticly ('m' or 'a')?")
    answer = input("If neither, exit the application by entering 'x'.: ")
    print()
    if answer == "x" or answer == "X": # user chose to leave application
      print("You selected to exit the application.")
      print()
      break
    elif answer == "a" or answer == "A": # user chose automatic roll
      rollDice = input("How many automatic rolls do you want to make?: ")
      rollDice = int(rollDice) # convert the answer to an integer
      print()
      break
    elif answer == "m" or answer == "M": # user chose manual roll
      print("You selected to manually roll the dice. The simmulation will now begin.")
      rollDice = 1 # set the number of rolls to one
      print()
      break
    else:
      print("Sorry, I do not understand. Please enter 'm', 'a', or 'x'.")
      print()

  # Simulation Dictionaries and Lists
  count = 0 # count the number of simulated rolls
  rollAgain = True # assume one run if true

  # Empty dictionaries to record the counts of each roll
  rollResults = {} # empty dictionary for roll results
  percentage = {} # empty dictionary for percentages
  barGraph = {} # empty dictionary for bar graph
  
  # Values for dictionaries
  for x in range(DICE_NUMBER, (DICE_NUMBER * faces) + 1):
    rollResults[x] = 0
    percentage[x] = 0
    barGraph[x] = "|"
    
  # List keeping track of roll simulation results
  results = [] # keep track of results from roll simulation
  if answer == "x" or answer == "X": # user chose to end simulation
    rollAgain = False # do not run simulation

# Start the dice roll simulations
  while rollAgain:
    TOTAL = 0
    count += 1
    for x in range (DICE_NUMBER):
      TOTAL += random.randint(1, faces) # roll results
    results.append(TOTAL)
    print()
    rollResults[TOTAL] += 1
    for x in range(DICE_NUMBER, (DICE_NUMBER * faces) + 1):
      percentage[x] = 100 * rollResults[x] / count # percentage of roll results
      barGraph[x] = "|" + round(percentage[x]) * "|" # produces bar graph from the results percentages
    print()
    print("Dice Roll " + str(count) + ": Dice TOTAL = " + str(TOTAL)) # print dice roll number and total
    print("rollDice Simulation Results:") 
    print(results)
    print()
    print(" #  Count    Percentage     Graph") # table header
    print("-" * 65) # table line
    # Produce a visualization of the results of the simulation 
    for x in range(DICE_NUMBER, (DICE_NUMBER * faces) + 1):
      print("%3d" % x + ": " + "%3d" % rollResults[x] + 5*" " + "%5.2f" % percentage[x] + " %" + 5*" " + barGraph[x])
    print("-" * 65) # table line
    print("Sum:" + "%4d" % sum(rollResults.values()) + 5*" " + "%5.2f" % sum(percentage.values()) + " %") # print sum of count and percentages
    print()
    if rollDice > 1: 
      sleep(1) # one second pause inbetweeen rolls
    # Manual dice roll
    if answer == "m":
      rollResponse = input("Roll again? (y/n): ")
      if (rollResponse != "y"):
        break
    if (count >= rollDice and answer == 'a'):
      rollAgain = False

  # Print descriptive statistics 
  if count >= 2: # dice is rolled at least twice
    print()
    print("Descriptive Statistics for dice roll simulation:")
    print("-" * 40) # table line
    print("Mean                     ", statistics.mean(results)) # print mean of simulation results
    print("Median                   ", statistics.median(results)) # print median of simulation results
    print("Mode                     ", statistics.mode(results)) # print mode of simulation results
    print("Std Dev (sample)         ", statistics.stdev(results)) # print standard deviation of simulation results
    print("Variance (sample)        ", statistics.variance(results)) # print variance of simulation results
    print("Minimum                  ", min(results)) # print minimum value of simulation results
    print("Maximum                  ", max(results)) # print maximum value of simulation results
    print("Range                    ", (max(results) - (min(results)))) # print range of simulation results
    print("Sum                      ", sum(results)) # print sum of simulation results
    print("Count                    ", len(results)) # print count of simulation results
    print()
  else:
    print("You must roll at least two times to produce a Descriptive Statistics Report.") # user didn't roll the dice at least two times
    print()
  answer = input("Would you like to try a new simulation? (y/n): ") # ask user if they want to roll again
  print()
  if (answer != "y"): # end the application if user does not enter "y"
    break
print("Thank you, " + name + ". The Dice Roll Simulation Application is closing.")