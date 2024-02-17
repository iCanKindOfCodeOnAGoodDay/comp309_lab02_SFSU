"""
    CSC 309 SFSU Spring 2023
    Lab #2
    Created on Wed Feb  7 22:57:28 2024
    Updated Fri Feb 9, 18:00
    @author: scottquashen
    
    


    Description: 
        This program contains random numbers between min, and max, with count amount of numbers.
        Prints the numbers all at once, and also prints the numbers 4 per row, handling
        remainders if any exist in the last row.
    

    Inputs: 
        Functions with inputs
        1) printPythonList - takes in a list
        2) PrintPythonListWith4ItemsPerRow - takes a list
        3) createNumbers - variable min, max, and count
        

    Outputs: 
        1) printPythonList - outputs text in the console
        2) PrintPythonListWith4ItemsPerRow - toutputs text in the console
        3) createNumbers - outputs a list of count with values being
           random between min and max variable values



    Dependencies: Time, Random

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.2.1
"""


# Import all of your modules needed for this project.
import time
import random


# Write a function to print the Python List all at once.
def PrintPythonList(someList):
    """ 

     This function prints the contents of some list in a single line.

     Inputs: a single array, someList

     Output: prints in text in console

     Returns: nothing

     Usage: PrintPythonList(myRandomNumbers)

     """
    print(someList)   

# Write a function to print the Python list 4 numbers per line
def PrintPythonListWith4ItemsPerRow(someList):
     """ 

     This function prints the contents of some list in seperate lines 
     with 4 items accounting for remainders

     Inputs: a single array, someList

     Output: prints text in console

     Returns: nothing

     Usage: PrintPythonListWith4ItemsPerRow(myRandomNumbers)

     """    
     for i in range(0, len(someList)):
       if(i % 4 == 0):
           print("\n")
       print(someList[i], end= ", ")          

# Print name and date
print("Scott Quashen " + time.asctime())

#create a list with 21 random numbers of value 0 - 99
myRandomNumbers = []
def createNumbers(min, max, count):
    """ 

     This function adds specified amount of random values to a list 
     with specified min and max values, 
     and returns a single list containing those numbers.

     Inputs: 3 numeric arguments, min, max, count

     Output: random numbers

     Returns: List of type int 

     Usage: createNumbers(0, 99, 21)

     """
    i = 0
    while (i < count):
        myRandomNumbers.append(random.randint(min, max))
        i += 1
    return myRandomNumbers    
        
#call a function to create a list of random numbs, pass in min, max, and count
createNumbers(0, 99, 21)

# Call a function that will print the Python List, all at once
PrintPythonList(myRandomNumbers)

# Call a 2nd function that will print the Python List 4 numbers per line
PrintPythonListWith4ItemsPerRow(myRandomNumbers)


#
#
#



