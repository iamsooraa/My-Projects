"""
File Name: LarkinsU6AE
Author: Sora Larkins 
Last Date Modified: 03/27/2022
The purpose of this program is to demonstrate how to create and invoke my own version of each of the statistics functions for a descriptive statistics reports for the values contained in the file. 
"""

# Simple Algorithm
#-------------------------------
# Print title of program
# Welcome user
# - Get user name
# - Check if the user needs instructions
# Let the user choose a data file 
# Open data file
# Import any necessary Python modules
# Define functions for each descriptive statistic
# Print descriptive statistics report
# Allow user to analyze another file
# - Ask user if they want to analyze another file
# - Print descriptive statistics report for new file
# End application
#------------------ Begin code ------------------#

# Title of program
print("%40s" % "Descriptive Statistics App Running") 
print()

# Welcome dialogue
name = input("Please provide the name you would like to use for this session: ") # user can input their name
print()
print("Hello, " + name + ". Welcome to the Descriptive Statistics Application.") # print welcome dialogue with name
print()

# Instructions
while True:
  answer = input("Do you need instructions, " + name + "?(y/n): ") # ask the user if they want instructions
  print()
  if(answer == "y" or answer == "Y"): # print instructions if user says "yes"
    # Print instruction
    print("- The application will ask you to select a data file.")
    print("- Type the name of the data file you want to analyze (For example: filename.txt).")
    print("- The application will respond with a descriptive statistics table for the values in the file.")
    print("- The application will ask you if you want to analyze another file.")
    print("- If you wish to analyze another file, enter 'y'.")
    print("- When you are ready to exit, enter the letter 'n'.")
    print()
    break
  elif(answer == "n" or answer == "N"): # skip instructions  
    break
  else:
    print("Sorry, I do not understand. Please enter 'y' or 'n'.") # repeat the question if the answer is not 'y' or 'n'
    print()

# Allow the user to select a data file
file = input("Please provide the name of the file you want to analyze: ")
print()
print("File " + file + " found in the current working directory.")
print()
print(name + " entered " + file + ".")
print()

while True:
  # read the data file and demo on statistical method
  f = open(file, 'r')
  myValues = [] # an empty list
  for line in f: # Traverse the file
    value = line.strip() # Use strip to remove the newline
    number = int(value) # Convert the text to integer
    myValues.append(number) # Add the value to the list
    
  
  # Print descriptive statistics report
  print(name + ", please see the Descriptive Statistics for the values in the " + file + " file listed in the table below:")
  print()
  print("Measure                  Results") # table heading
  print("-" * 35) # table line
  
  # Mean
  def myMean(aList):
    # This fucntion expects a list of values and returns the statistical average of those values
    sum = 0.0
    for i in range(len(aList)):
      sum += aList[i]
    return sum/len(aList)
  print("%-20s" % "Mean:", "%10.2f" % myMean(myValues))
  
  # Median
  def myMedian(aList):
    n = len(aList)
    median = n // 2
    # odd number of observations
    if n % 2:
      return sorted(aList)[median]
    # even number of observations
    return sum(sorted(aList)[median - 1: median + 1]) / 2 # returns the median of the values in the file
  print("%-20s" % "Median:", "%10.2f" % myMedian(myValues))
  
  # Mode
  def myMode(aList):
      m = max([aList.count(a) for a in aList])
      return [x for x in aList if aList.count(x) == m][0] if m>1 else None # returns the mode of the values in the file
  print("%-20s" % "Mode:", "%10.2f" % myMode(myValues)) 
  
  # Standard Deviation
  import math # imported for square root
  def myStddev(aList):
  # Finding Mean value
    sum = 0
    for i in range(len(aList)):
      sum += aList[i]
    mean = sum / len(aList)
  # Finding square of difference of mean and each value
    difference_squared = 0
    for i in range(len(aList)):
      difference_squared += (aList[i] - mean) ** 2
  # Finding Square Root
    std_dev = math.sqrt(difference_squared / ((len(aList)) - 1))
    return std_dev # returns the std dev of the values in the file
  print("%-20s" % "Std Dev (Sample):", "%10.2f" % myStddev(myValues))
  
  # Variance
  def myVariance(aList):
    n = len(aList)
    mean = sum(aList) / n
    deviations = [(x - mean) ** 2 for x in aList]
    variance = sum(deviations) / n
    return variance # returns the variance of the values in the file
  print("%-20s" % "Variance (Sample):", "%10.2f" % myVariance(myValues))
  
  # Minimum
  def myMinimum(aList):
    s = aList[0]
    for num in aList:
      if num < s:
        s = num
    return s # returns the minimum value of the values in the file
  print("%-20s" % "Minimum:", "%10.2f" % myMinimum(myValues))
  
  # Maximum
  def myMaximum(aList):
    l = aList[0]
    for num in aList:
      if num > l:
        l = num
    return l # returns the maximum value of the values in the file
  print("%-20s" % "Maximum:", "%10.2f" % myMaximum(myValues))
    
  # Sum
  def mySum(aList):
    sum = 0.0
    for i in range(len(aList)):
      sum += aList[i]
    return sum # returns the sum of the values in the file
  print("%-20s" % "Sum:", "%10.2f" % mySum(myValues))
  
  # Count
  def myCount(aList):
    n = len(aList)
    return n # returns the count of the values in the file
  print("%-20s" % "Count:", "%10.2f" % myCount(myValues))
  print()
  
  response = input("Would you like to analyze another data file?(y/n): ") # ask the user if they want analyze another file
  print()
  if(response == "y" or response == "Y"): # allow user to enter another file
    file = input("Please provide the name of the file you want to analyze: ")
    print()
    print("File " + file + " found in the current working directory.")
    print()
    print(name + " entered " + file + ".")
    print()
  elif(response == "n" or response == "N"): # end application
    break
  else:
    print("Sorry, I do not understand. Please enter 'y' or 'n'.")
    print()

# Application Exit Dialogue  
print("Thank you " + name + " for using Descriptive Statistics. The application has now ended.")

