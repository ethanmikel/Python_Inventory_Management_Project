#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:40:15 2023

@author: ethanmikel
"""
#importing the class file 
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
    
    #print(list_keys)
    
    transaction_list = []
    
    product_purchase(list_keys, qty_available_dict, transaction_list, item_1, item_2, item_3, item_4, item_5, item_6, item_7)
    
    for i in range(0, len(transaction_list)):

     print(transaction_list[i])
 

def create_dictionaries(item_dict, price_dict, qty_available_dict):
    inventory_file = open('Inventory.txt', 'r') 
    id_key = inventory_file.readline().rstrip("\n")
    while id_key != '':
        id_key = int(id_key)
        item = inventory_file.readline().rstrip('\n')
        qty_available = int(inventory_file.readline().rstrip('\n'))
        price = float(inventory_file.readline().rstrip('\n'))
        
        item_dict[id_key] = item
        price_dict[id_key] = price
        qty_available_dict[id_key] = qty_available
        
        id_key = inventory_file.readline().rstrip("\n")
        
    inventory_file.close()
    
def menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7):
    print("ID\t\t\t\t\t\tItem\t\t\tPrice\t\tQty Available")
    print(item_1)
    print(item_2)
    print(item_3)
    print(item_4)
    print(item_5)
    print(item_6)
    print(item_7)
    
def product_purchase(list_keys, qty_available_dict, transaction_list, item_1, item_2, item_3, item_4, item_5, item_6, item_7): 
    product_id = -1
    while product_id == -1 or product_id != 0:
        product_id = validation_object.checkInt(input("\nWhich product ID would you like to purchase? Enter 0 to exit. "))
        if product_id == -1:
            print("Invalid product ID, please try again.")
        elif product_id == 0:
            break
        else: 
            for item in list_keys:
                if item == product_id:
                    #print("FOUND",product_id)
                    item_purchase(product_id, qty_available_dict, list_keys, transaction_list, item_1, item_2, item_3, item_4, item_5, item_6, item_7)
                else: 
                    item+=1
            print()
            menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7)
               #print("Invalid product ID, please try again.")

def item_purchase(desired_product_id, qty_available_dict, list_keys, transaction_list, item_1, item_2, item_3, item_4, item_5, item_6, item_7):
    qty_purchase = -1
    #print(qty_available_dict[desired_product_id])
    while qty_purchase == -1:
        qty_purchase = validation_object.checkInt(input("\nHow many items would you like the purchase? Enter negative number for returns. "))
        if qty_purchase == -1:
            print("This is not a valid quantity. Try again.")
        elif list_keys[0] == desired_product_id: 
            item_1.purchase(qty_purchase)
            transaction_list.append(item_1)
            #print(item_1)
        elif list_keys[1] == desired_product_id: 
            item_2.purchase(qty_purchase)
            #print(item_2)
        elif list_keys[2] == desired_product_id: 
            item_3.purchase(qty_purchase)
            #print(item_3)
        elif list_keys[3] == desired_product_id: 
            item_4.purchase(qty_purchase)
            #print(item_4)
        elif list_keys[4] == desired_product_id: 
            item_5.purchase(qty_purchase)
            #print(item_5)
        elif list_keys[5] == desired_product_id: 
            item_6.purchase(qty_purchase)
            #print(item_6)
        elif list_keys[6] == desired_product_id: 
            item_7.purchase(qty_purchase)
            #print(item_7)

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
