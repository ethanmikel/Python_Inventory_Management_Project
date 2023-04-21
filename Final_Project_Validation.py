#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:47:23 2023

@author: ethanmikel
"""
#Author: Ethan Mikel and Soham Sharma
#Final Project Name: Inventory Management for a Baking Supply Shop 
#Due Date: April 26 By 11:59 PM
#Program Description: The program writes an application to store and manage existing inventory, and allow customers to purchase or return bakery supplies. This specific file contains the code for creating the validation class and functions that will be used in the main program to validate user input


#imports the class file 
import Mikel_Ethan_Soham_Sharma_Classes

#defines the ValidationClass to ensure the user has inputed a correct value for inital and current input. 
class ValidationClass():
    #setting default value variable to -1
    default_value = -1

    #defines the checkFloat method that ensures that the users input for inital and current value is a float and not any type of string, left empty, or a negative value. If it encounters any of these, it returns -1 back to the main class to prompt the user for a new input, so the cycle can repeat. If it validates that it is a positive value it returns the float back to the main program. 
    def checkFloat(self, str_value):
        #creating a try-except-else block
        try:
            default_value = float(str_value) #convert input to a float and set default_value variable to user input
        except TypeError: #if the input is of wrong type, catch the error and print a line
            print()
        except: 
            default_value = -1 #if the input is not a float or cant be converted to a float, set default_value variable to -1
        else:
            if default_value < 0: #if the input is a value less than 0, set default_value variable to -1
                default_value = -1
        return default_value #returns the value stored in the default_value variable
    
    #defines the checkInteger method that ensures that the users input for inital and current value is a int and not any type of string, left empty, or a negative value. If it encounters any of these, it returns -1 back to the main class to prompt the user for a new input, so the cycle can repeat. If it validates that it is a positive value it returns the float back to the main program. However, for this homework we do not call this instead it is for future and learning purposes.  
    def checkInt(self, str_value):
        #creating a try-except-else block
        try:
            default_value = int(str_value)  #convert input to an integer and set default_value variable to user input
        except TypeError: #if the input is of wrong type, catch the error and print a line
            print()
        except: # If the input is not an int or can't be converted to an int, set default_value to -1
            default_value = -1
        else:
            if default_value < 0: #if the input is a value less than 0, set default_value variable to -1
                default_value = -1
        return default_value #returns the value stored in the default_value variable
        
    #defines the checkInt2 method to ensure that user input is an integer and not any type of string, left empty or negative value. If it encounters any of these, it returns -1.01 back to the main class to prompt the user for a new input, so the cycle can repeat. 
    def checkInt2(self, str_value):
        #try except block
        try: 
            default_value = int(str_value) #convert input to an integer and set default_value variable to user input
        except TypeError: #if the input is of wrong type, catch the error and print a line
            print()
        except: # If the input is not an int or can't be converted to an int, set default_value to -1.01
            default_value = -1.01
        return default_value #returns the value stored in the default_value variable
        
