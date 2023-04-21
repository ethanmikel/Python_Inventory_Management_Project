#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:14:21 2023

@author: ethanmikel
"""
#Author: Ethan Mikel and Soham Sharma
#Final Project Name: Inventory Management for a Baking Supply Shop 
#Due Date: April 26 By 11:59 PM
#Program Description: The program writes an application to store and manage existing inventory, and allow customers to purchase or return bakery supplies. This specific file contains the code for creating the classes that will be used in the main program.

#creates the Inventory class that creates a blueprint for storing inventory information
class Inventory:
    
    #defines the init method that initializes id, name, price, and stock attributes
    def __init__(self, new_id, new_name, new_price, new_stock):
        self.__id = new_id #item id
        self.__name = new_name #item name
        self.__price = new_price #item price
        self.__stock = new_stock #stock of the item

    #defines the accessor method to retreive item id 
    def get_id(self):
        return self.__id

    #defines the accessor method to retreive item name 
    def get_name(self):
        return self.__name

    #defines the accessor method to retreive item stock
    def get_stock(self):
        return self.__stock

    #defines the accessor method to retreive item price
    def get_price(self):
        return self.__price

    #defines a method to restock an item in the inventory with the specified amount
    def restock(self, new_stock):
        # if the restock amount is negative, subtract from current stock or else return false
        if new_stock < 0: 
            self.__stock -= new_stock
            return True
        else: 
            return False
        # self.__stock -= new_stock

    # defines a method to purchase an item from the inventory with the specified quantity
    def purchase(self, purch_qty):
        # if the purchased quantity is less than equal to the current stock, subtract the purchase quantity from the current stock or else return false
        if purch_qty <= self.__stock:
            self.__stock -= purch_qty
            return True
        else: 
            return False
    # defines the string method to output the class attributes as a string 
    def __str__(self):
        return str(self.__id) + " \t" + '{:>25}'.format(self.__name) + "\t\t  $" + str(format(self.__price, '6,.2f')) + "\t\t " + str(format(self.__stock, '12,.0f'))

#creates the TransactionItem class that creates a blueprint for storing information about an item purchased or returned
class TransactionItem:

    #defines the init method that initializes id, name, quantity, and price attributes
    def __init__(self):
        self.__id = '' #item id
        self.__name = '' #item name
        self.__quantity = 0 #initializes the item quantity to zero
        self.__price = 0 #initializes the item price to 0
        
    #defines the accessor method to retreive item id
    def get_id(self):
        return self.__id

    #defines the mutator method to set item id to new id
    def set_id(self, new_id):
        self.__id = new_id

    #defines the accessor method to retreive item name 
    def get_name(self):
        return self.__name

    #defines the mutator method to set item name to new name
    def set_name(self, new_name):
        self.__name = new_name

    #defines the accessor method to retreive item quantity 
    def get_qty(self):
        return self.__quantity

    #defines the mutator method to set the item quantity by adding new quantity
    def set_qty(self, new_qty):
        self.__quantity += new_qty

    #defines the accessor method to retreive item price 
    def get_price(self):
        return self.__price

    #defines the mutator method to set item price to new price 
    def set_price(self, new_price):
        self.__price = new_price

    #defines the accessor method to calculate the cost by multiplying item price with item quantity
    def calc_cost(self):
        return self.__price * self.__quantity

    # defines the string method to output the class attributes as a string 
    def __str__(self):
        return str(self.__id) + " \t" + '{:>25}'.format(self.__name) + "\t\t" + str(format(self.__quantity, '12,.0f')) + "\t\t $" + str(format(self.__price, '6,.2f'))









    
    
