#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:40:15 2023

@author: ethanmikel
"""

import Mikel_Ethan_Soham_Sharma_Classes
import Final_Project_Validation

validation_object = Final_Project_Validation.ValidationClass()

def main():
    item_dict = {}
    price_dict = {}
    qty_available_dict = {}

    create_dictionaries(item_dict, price_dict, qty_available_dict)
    
    list_keys = list(item_dict.keys())

    
    item_1 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[0], item_dict[list_keys[0]], price_dict[list_keys[0]], qty_available_dict[list_keys[0]])
    item_2 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[1], item_dict[list_keys[1]], price_dict[list_keys[1]], qty_available_dict[list_keys[1]])
    item_3 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[2], item_dict[list_keys[2]], price_dict[list_keys[2]], qty_available_dict[list_keys[2]])
    item_4 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[3], item_dict[list_keys[3]], price_dict[list_keys[3]], qty_available_dict[list_keys[3]])
    item_5 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[4], item_dict[list_keys[4]], price_dict[list_keys[4]], qty_available_dict[list_keys[4]])
    item_6 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[5], item_dict[list_keys[5]], price_dict[list_keys[5]], qty_available_dict[list_keys[5]])
    item_7 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[6], item_dict[list_keys[6]], price_dict[list_keys[6]], qty_available_dict[list_keys[6]])


    menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7)
    product_purchase()

def create_dictionaries(item_dict, price_dict, qty_available_dict):
    inventory_file = open('Inventory.txt', 'r') 
    id_key = inventory_file.readline().rstrip("\n")
    while id_key != '':
        item = inventory_file.readline().rstrip('\n')
        qty_available = int(inventory_file.readline().rstrip('\n'))
        price = float(inventory_file.readline().rstrip('\n'))
        
        item_dict[id_key] = item
        price_dict[id_key] = price
        qty_available_dict[id_key] = qty_available
        
        id_key = inventory_file.readline().rstrip("\n")
        
    inventory_file.close()
    
def menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7):
    print("ID\t\t\t\tItem\t\t\tPrice\t\tQty Available")
    print(item_1)
    print(item_2)
    print(item_3)
    print(item_4)
    print(item_5)
    print(item_6)
    print(item_7)
    
def product_purchase(): 
    product_id = -1
    while product_id == -1:
        product_id = validation_object.checkFloat(input("Which product ID would you like to purchase? Enter 0 to exit. "))
        if product_id == -1:
            print("Invalid product ID, please try again.")

main()

#%%
def inventory_list():
    inventory_managemt = []
    
    id_data = inventory_file.readline().rstrip('\n')
    while id_data != '':
        item = inventory_file.readline().rstrip('\n')
        qty_available = inventory_file.readline().rstrip('\n')
        price = inventory_file.readline().rstrip('\n')
        inventory_managemt+=[[id_data,item,price,qty_available]]
        id_data = inventory_file.readline().rstrip('\n')
    return inventory_managemt