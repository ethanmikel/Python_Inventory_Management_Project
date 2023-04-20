#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:47:23 2023

@author: ethanmikel
"""
#Author: Ethan Mikel and Soham Sharma
#Final Project Name: Inventory Management for a Baking Supply Shop 
#Due Date: April 26 By 11:59 PM
#Program Description:
    
import Mikel_Ethan_Soham_Sharma_Classes

#ValidationClass ensure the user has inputed a correct value for inital and current input. 
class ValidationClass():
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
        return default_value
        
    
    def checkInt2(self, str_value): 
        try:
            default_value = int(str_value)
        except TypeError:
            print()
        except: 
            default_value = -1.01
        return default_value
        