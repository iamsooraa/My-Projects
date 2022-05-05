"""
Program Name: LarkinsSDLCproject
Author: Sora Larkins
Date Modified: 04/21/2022
Purpose: The purpose of this program is to conduct a linear regression model to determine if there is a correlation between deaths caused by COVID and poverty.
"""
# Simple Algorithm
#-----------------------------------------------------#
# Import Python modules
# Greet the user
# Provide instructions
# Print analysis of variance
# Print descriptive statistics report
# Print data table
# - Print the first 10 rows of the data frame
# Produce data visualization
# - Read CSV file 
# - Create variable for 'deaths' from the data frame
# - Create variable for 'poverty' from the data frame
# - Create scatter plot
# - Create regression lines
#-------------------End application-------------------#

# Import Modules
import numpy as np # import numpy to create arrays
import pandas as pd # import pandas to clean and manipulate data set
import matplotlib.pyplot as plt # import matplotlib to create scatter plot
import statsmodels.api as sm # import statsmodels to create linear regression descriptive analysis
import statsmodels.formula.api as smf # import statsmodels to create linear regression descriptive analysis
from scipy.stats import skew # import scipy to calculate skewness
from scipy.stats import kurtosis # import scipy to calculate kurtosis

# Welcome user
print("%40s" % "COVID-19 Deaths Linear Regression Model") 
print()
print("Welcome to the COVID-19 Deaths Linear Regression Model.")
print("This model contains the analysis of the relationship between COVID deaths & poverty.")
print("-" * 80)
print()
df = pd.read_csv('covid.csv') # pandas reading the CSV file
y = df['Deaths'].values # define y value as deaths
x = df['Poverty'].values # define x value as poverty
my_model = smf.ols(formula='Deaths ~ Poverty', data=df) # statsmodels analyzing deaths and poverty from csv file
# fit model to data to obtain parameter estimates
my_model_fit = my_model.fit()
# print summary of linear regression
print(my_model_fit.summary())
# show anova table
anova_table = sm.stats.anova_lm(my_model_fit, typ = 2)
print(anova_table)
# create variables for descriptive statistics report
mean1 = df['Deaths'].mean() # mean of deaths
sum1 = df['Deaths'].sum() # sum of deaths
max1 = df['Deaths'].max() # maximum value of deaths
min1 = df['Deaths'].min() # minimum value of deaths
count1 = df['Deaths'].count() # count of deaths
median1 = df['Deaths'].median() # median of deaths
std1 = df['Deaths'].std() # std dev of deaths
var1 = df['Deaths'].var() # variance of deaths
mode1 = df['Deaths'].mode() # mode of deaths
range1 = max1-min1 # range of deaths
mean2 = df['Poverty'].mean() # mean of poverty
mode2 = df['Poverty'].mode() # mode of poverty
sum2 = df['Poverty'].sum() # sum of poverty
max2 = df['Poverty'].max() # maximum value of poverty
min2 = df['Poverty'].min() # minimum value of poverty
count2 = df['Poverty'].count() # count of poverty
median2 = df['Poverty'].median() # median of poverty
std2 = df['Poverty'].std() # std dev of poverty
var2 = df['Poverty'].var() # variance of poverty
range2 = max2-min2 # range of poverty
print()
# print descriptive statistics report (round 2 decimal places)
print("Descriptive Statistics Report")
print("-" * 70)
print("          Deaths       Poverty")
print()
print('Mean:     ' + str(round(mean1, 2)) + "         " + str(round(mean2, 2)))
print('Median:   ' + str(round(median1, 2)) + "         " + str(round(median2, 2)))
print('Mode:     ' + str(round(mode1, 2)) + "         " + str(round(mode2, 2)))
print('Sum:      ' + str(round(sum1, 2)) + "     " + str(round(sum2, 2)))
print('Maximum:  ' + str(round(max1, 2)) + "        " + str(round(max2, 2)))
print('Minimum:  ' + str(round(min1, 2)) + "          " + str(round(min2, 2)))
print('Range:    ' + str(round(range1, 2)) + "        " + str(round(range2, 2)))
print('Count:    ' + str(round(count1, 2)) + "         " + str(round(count2, 2)))
print('Std Dev:  ' + str(round(std1, 2)) + "         " + str(round(std2, 2)))
print('Var:      ' + str(round(var1, 2)) + "        " + str(round(var2, 2)))
print('Skewness: ' + str(round(skew(y), 2)) + "        " + str(round(skew(x),2)))
print('Kurtosis: ' + str(round(kurtosis(y), 2)) + "        " + str(round(kurtosis(x),2)))
print()
print("-" * 75)
print(df.head(10)) # print the first 10 rows of the data frame
deaths = df.Deaths  # create variable for 'deaths' from the data frame
poverty = df.Poverty # create variable for 'poverty' from the data frame
plt.scatter(poverty, deaths) # create scatter plot for deaths and poverty
plt.plot(poverty, poverty + -5, '-g') # regression line
plt.xlabel("Poverty", fontsize = 10) # x-axis label
plt.ylabel("Deaths", fontsize = 10) # y-axis label
plt.show() # display scatter plot graph
