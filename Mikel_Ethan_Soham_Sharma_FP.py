#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:40:15 2023

@author: ethanmikel
"""
#Author: Ethan Mikel and Soham Sharma
#Final Project Name: Inventory Management for a Baking Supply Shop 
#Due Date: April 26 By 11:59 PM
#Program Description:


import Mikel_Ethan_Soham_Sharma_Classes
import Final_Project_Validation

validation_object = Final_Project_Validation.ValidationClass()

def main():
    item_dict = {}
    price_dict = {}
    qty_available_dict = {}

    create_dictionaries_inventory(item_dict, price_dict, qty_available_dict)
    
    list_keys = list(item_dict.keys())
    
    item_2_dict = {}
    for i in range(len(item_dict)):
        item_2_dict[list_keys[i]] = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[i], item_dict[list_keys[i]], price_dict[list_keys[i]], qty_available_dict[list_keys[i]])
    
    purchase_dict = {}
    for i in range(len(list_keys)):
        purchase_dict[list_keys[i]] = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    
    purchase_keys = []
    
    menu_print(item_2_dict)
        
    product_purchase(list_keys, qty_available_dict, item_dict, price_dict, item_2_dict, purchase_dict, purchase_keys) 
        
            
def create_dictionaries_inventory(item_dict, price_dict, qty_available_dict):
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
    
def menu_print(item_2_dict):
    print("ID\t\t\t\t\t\tItem\t\t\tPrice\t\tQty Available")
    for i in item_2_dict:
        print(item_2_dict[i])
    
def product_purchase(list_keys, qty_available_dict, item_dict, price_dict, item_2_dict, purchase_dict, purchase_keys): 
    product_id = -1
    count = 0
    while product_id == -1 or product_id != 0:
        product_id = validation_object.checkInt(input("\nWhich product ID would you like to purchase? Enter 0 to exit. "))
        count+=1
        if product_id == -1:
            print("Invalid product ID, please try again.")
        elif product_id == 0:
            if count == 1:
                print("Thank you for visitng our store!")
                update_inventory(list_keys, item_2_dict)
            else:
                update_inventory(list_keys, item_2_dict)
                end_menu(purchase_dict, purchase_keys)
        else: 
            if product_id in item_2_dict:
                item_purchase(product_id, list_keys, qty_available_dict, item_dict, item_2_dict, price_dict, purchase_dict, purchase_keys)
            elif product_id not in item_2_dict:
                print("Invalid product ID, please try again.")
            #menu_print(item_2_dict)
            
def item_purchase(product_id, list_keys, qty_available_dict, item_dict, item_2_dict, price_dict, purchase_dict, purchase_keys):
    #print(list_keys)
    #print(item_dict)
    #print(desired_product_id)
    #print(price_dict)
    #print(qty_available_dict)
    flag = True 
    qty_purchase = -1.01
    position = 0
        
    while qty_purchase == -1.01 or qty_purchase == -1.02:
        qty_purchase = validation_object.checkInt2(input("\nHow many items would you like the purchase? Enter negative number for returns. "))
        if qty_purchase == -1.01 or qty_purchase == 0:
            print("This is not a valid quantity. Try again.")
            qty_purchase = -1.01 
        if qty_purchase > 0: 
            for i in list_keys:
                if i == product_id and qty_purchase != -1.01:
                    temp_quantity = item_2_dict[i].get_stock()
                    flag =item_2_dict[i].purchase(qty_purchase)
                    if flag == False:
                        print("Insufficent stock, please enter a valid quantity and re-enter a product ID.\n")
                        menu_print(item_2_dict)
                    elif flag == True:
                        purchase_dict[i].set_id(i)
                        purchase_dict[i].set_name(item_dict[i])
                        purchase_dict[i].set_price(price_dict[i])
                        purchase_dict[i].set_qty(qty_purchase)
                        print()
                        menu_print(item_2_dict)

        else: 
            for i in list_keys:
                if i == product_id and qty_purchase != -1.01:
                    flag = item_2_dict[i].restock(qty_purchase)
                    if flag == False:
                        qty_purchase == -1.02
                    elif flag == True:
                        purchase_dict[i].set_id(i)
                        purchase_dict[i].set_name(item_dict[i])
                        purchase_dict[i].set_price(price_dict[i])
                        purchase_dict[i].set_qty(qty_purchase)
                        print()
                        menu_print(item_2_dict)
        if product_id not in purchase_keys:
            purchase_keys.append(product_id) 

def update_inventory(list_keys, item_2_dict):          
    updated_inventory = open('UpdatedInventory.txt', 'w')
    for i in item_2_dict:
        updated_inventory.write(str(item_2_dict[i].get_id())+"\n")
        updated_inventory.write(str(item_2_dict[i].get_name())+"\n")
        updated_inventory.write(str(item_2_dict[i].get_stock())+"\n")
        updated_inventory.write(str(item_2_dict[i].get_price())+"\n")
    

def end_menu(purchase_dict, purchase_keys):
    tax = 0.085
    total_item = 0
    subtotal = 0.0
    position = 0
    print("\nOrder Complete. See Invoice Below:\nID\t\t\t\t\t\tName\t\t\tQuantity\t\tPrice\t\tTotal Price")
    for item in purchase_keys:
        #print(purchase_dict[purchase_keys[item]])
        print(purchase_dict[item], "\t$", format(purchase_dict[item].calc_cost(), ',.2f'))
        total_item += purchase_dict[item].get_gty()
        subtotal += purchase_dict[item].calc_cost()
    
    sales_tax = subtotal * tax
    grand_total = subtotal + sales_tax
    print("\nTotal Items:",format(total_item, ',.0f'))
    print("Subtotal: $"+format(subtotal, ',.2f'))
    print("Sales Tax: $"+format(sales_tax, ',.2f'))
    print("Grand Total: $"+format(grand_total, ',.2f'))

main()
