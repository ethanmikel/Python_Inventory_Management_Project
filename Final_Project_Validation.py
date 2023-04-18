#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:47:23 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 8 Employee Management
#Due Date: April 17 by 11:59 PM
#Program Description: Validates that the user inputs are either a float or an integer value, and return them back to the EmployeeFile to then be able to used in other programs. For the CheckInt method it is for if the production worker works day or night shift and will only return the proper vlaue if the user inputs a 1 or 2. For both class, if there is an incorrect entry it will return -1. 

#ValidationClass ensure the user has inputed a correct value for inital and current input. 
class ValidationClass:
    default_value = -1

    #checkFloat method ensures that the users input for inital and current value is a float and not any type of string, left empty, or a negative value. If it encounters any of these, it returns -1 back to the main class to prompt the user for a new input, so the cycle can repeat. If it validates that it is a positive value it returns the float back to the main program. 
    def checkFloat(self, str_value): 
        try:
            default_value = float(str_value)
        except TypeError:
            print()
        except: 
            default_value = -1
        else:
            if default_value < 0: 
                default_value = -1
        return default_value
    
    #checkInteger method ensures that the users input for inital and current value is a int and not any type of string, left empty, or a negative value. If it encounters any of these, it returns -1 back to the main class to prompt the user for a new input, so the cycle can repeat. If it validates that it is a positive value it returns the float back to the main program. However, for this homework we do not call this instead it is for future and learning purposes.  
    def checkInt(self, str_value): 
        try:
            default_value = int(str_value)
        except TypeError:
            print()
        except: 
            default_value = -1
        else:
            if default_value < 0: 
                default_value = -1
            elif default_value == 1 or default_value == 2:
                print("")
            else: 
                default_value = -1
        return default_value
        
        