#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:14:21 2023

@author: ethanmikel
"""

class Inventory:
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price
    
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_stock(self):
        return self.__stock
    def get_price(self):
        return self.__price
    
    def restock(self, new_stock):
        self.__stock += new_stock
    def purchase(self, purch_qty):
        self.__stock -= purch_qty
    
    def __str__(self):
        return self.__id + " \t\t " + self.__name + " \t\t " + str(format(self.__stock, '12,.2f')) + " \t\t " + str(format(self.__price, '12,.0f'))
    
   # print(str(current_year) + " \t" + format(additional_savings,'12,.0f') + "\t " + format(interest_earned, '12,.0f') + "\t\t " + format(total_savings, '12,.0f'))
