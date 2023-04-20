#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:14:21 2023

@author: ethanmikel
"""
#Author: Ethan Mikel and Soham Sharma
#Final Project Name: Inventory Management for a Baking Supply Shop 
#Due Date: April 26 By 11:59 PM
#Program Description:

class Inventory:
    def __init__(self, new_id, new_name, new_price, new_stock):
        self.__id = new_id
        self.__name = new_name
        self.__price = new_price
        self.__stock = new_stock
    
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_stock(self):
        return self.__stock
    def get_price(self):
        return self.__price
    
    def restock(self, new_stock):
        if new_stock < 0:
            self.__stock -= new_stock
            return True
        else: 
            return False
        # self.__stock -= new_stock
    def purchase(self, purch_qty):
        if purch_qty <= self.__stock:
            self.__stock -= purch_qty
            return True
        else: 
            return False
    
    def __str__(self):
        return str(self.__id) + " \t" + '{:>25}'.format(self.__name) + "\t\t  $" + str(format(self.__price, '6,.2f')) + "\t\t " + str(format(self.__stock, '12,.0f'))

class TransactionItem:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__quantity = 0
        self.__price = 0
    
    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_gty(self):
        return self.__quantity
    def set_qty(self, new_qty):
        self.__quantity += new_qty
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price
    
    def calc_cost(self):
        return self.__price * self.__quantity
    
    def __str__(self):
        return str(self.__id) + " \t" + '{:>25}'.format(self.__name) + "\t\t" + str(format(self.__quantity, '12,.0f')) + "\t\t $" + str(format(self.__price, '6,.2f'))









    
    