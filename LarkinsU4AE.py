"""
File name: LarkinsU4AE
Author: Sora Larkins 
Last Date Modified: 02/23/2022
The purpose of this program is to demonstrate opening text files and providing descriptive statistics reports for the values contained in the files. 
"""

# Simple Algorithm
#-------------------------------
# Print title of program
# Welcome user
# - Get user name
# - Check if the user needs instructions
# Let the user choose a data file 
# Import necessary modules
# Open data file
# Print descriptive statistics report
# Allow user to analyze another file
# - Ask user if they want to analyze another file
# - Print descriptive statistics report for new file
# End application
#------------------ Begin code ------------------#

# Title of program
print("%40s" % "Descriptive Statistics") 
print()

# Welcome dialogue
name = input("Please provide the name you would like to use for this session: ") # user can input their name
print()
print("Hello, " + name + ". Welcome to Descriptive Statistics.") # print welcome dialogue with name
print()

# Instructions
while True:
  answer = input("Do you need instructions, " + name + "?(y/n): ") # ask the user if they want instructions
  print("")
  if(answer == "y" or answer == "Y"): # print instructions if user says "yes"
    # Print instruction
    print("- The application will ask you to select a data file.")
    print("- Type the name of the data file you want to analyze (For example: filename.txt).")
    print("- The application will respond with a descriptive statistics table for the values in the file.")
    print("- The application will ask you if you want to analyze another file.")
    print("- If you wish to analyze another file, enter 'y'.")
    print("- When you are ready to exit, enter the letter 'n'.")
    print()
    enter = input("When you are ready to start the application, hit the Enter key.") 
    print()
    break
  elif(answer == "n" or answer == "N"): # skip instructions 
    enter = input("When you are ready to start the application, hit the Enter key.") 
    print()
    break
  else:
    print("Sorry, I do not understand. Please enter 'y' or 'n'.") # repeat the question if the answer is not 'y' or 'n'
    print()

# Allow the user to select a data file
file = input("Please provide the name of the file you want to analyze: ")
print()

# import Python modules
import statistics

# read the data file and demo on statistical method
f = open(file, 'r')
myValues = [] # an empty list
for line in f: # Traverse the file
  value = line.strip() # Use strip to remove the newline
  number = int(value) # Convert the text to integer
  myValues.append(number) # Add the value to the list
  

# Print descriptive statistics report
print("Descriptive Statistics Report") # report title
print("-"*45) # table border
print("Mean                               ", statistics.mean(myValues)) # print mean of values
print("Median                             ", statistics.median(myValues)) # print median of values
print("Mode                               ", statistics.mode(myValues)) # print mode of values
print("Standard Deviation (sample)        ", statistics.stdev(myValues)) # print standard deviation of values
print("Variance (sample)                  ", statistics.variance(myValues)) # print variance of values
print("Minimum                            ", min(myValues)) # print the minimum value
print("Maximum                            ", max(myValues)) # print the maximum value
print("Range                              ", (max(myValues) - min(myValues))) # print the range of values
print("Sum                                ", sum(myValues)) # print the sum of values
print("Count                              ", len(myValues)) # print the count value
print() 

# Allow the user to select another data file
while True:
  response = input("Do you want to analyze another file, " + name + "?(y/n): ") # ask the user if they want instructions
  print("")
  if(response == "y" or response == "Y"): # print instructions if user says "yes"
    # Print instruction
    fileName = input("Please provide the name of the file you want to analyze: ")
    print() # press enter to start application
  
    # import Python modules
    import statistics

    # read the data file and demo on statistical method
    f = open(fileName, 'r')
    myValues = [] # an empty list
    for line in f: # Traverse the file
      value = line.strip() # Use strip to remove the newline
      number = int(value) # Convert the text to integer
      myValues.append(number) # Add the value to the list

    
    # Print descriptive statistics report
    print("Descriptive Statistics Report") # report title
    print("-"*45) # table border
    print("Mean                               ", statistics.mean(myValues)) # print mean of values
    print("Median                             ", statistics.median(myValues)) # print median of values
    print("Mode                               ", statistics.mode(myValues)) # print mode of values
    print("Standard Deviation (sample)        ", statistics.stdev(myValues)) # print standard deviation of values
    print("Variance (sample)                  ", statistics.variance(myValues)) # print variance of values
    print("Minimum                            ", min(myValues)) # print the minimum value
    print("Maximum                            ", max(myValues)) # print the maximum value
    print("Range                              ", (max(myValues) - min(myValues))) # print the range of values
    print("Sum                                ", sum(myValues)) # print the sum of values
    print("Count                              ", len(myValues)) # print the count value
    print() 
  elif(response == "n" or response == "N"): # end application
    print("Thank you " + name + " for using Descriptive Statistics. The application has now ended.")
    break
  else:
    print("Sorry, I do not understand. Please enter 'y' or 'n'.") # repeat the question if the answer is not 'y' or 'n'
    print()

