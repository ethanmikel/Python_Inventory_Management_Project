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

    create_dictionaries_inventory(item_dict, price_dict, qty_available_dict)
    
    list_keys = list(item_dict.keys())
    
    purchase_keys = []
    
    item_1 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[0], item_dict[list_keys[0]], price_dict[list_keys[0]], qty_available_dict[list_keys[0]])
    item_2 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[1], item_dict[list_keys[1]], price_dict[list_keys[1]], qty_available_dict[list_keys[1]])
    item_3 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[2], item_dict[list_keys[2]], price_dict[list_keys[2]], qty_available_dict[list_keys[2]])
    item_4 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[3], item_dict[list_keys[3]], price_dict[list_keys[3]], qty_available_dict[list_keys[3]])
    item_5 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[4], item_dict[list_keys[4]], price_dict[list_keys[4]], qty_available_dict[list_keys[4]])
    item_6 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[5], item_dict[list_keys[5]], price_dict[list_keys[5]], qty_available_dict[list_keys[5]])
    item_7 = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[6], item_dict[list_keys[6]], price_dict[list_keys[6]], qty_available_dict[list_keys[6]])
    
    purchase_1 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    purchase_2 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    purchase_3 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    purchase_4 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    purchase_5 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    purchase_6 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
    purchase_7 = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()
        
    menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7)
        
    product_purchase(list_keys, qty_available_dict, item_dict, price_dict, item_1, item_2, item_3, item_4, item_5, item_6, item_7, purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_keys)      
    
    end_menu(purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_keys)

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
    
def menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7):
    print("ID\t\t\t\t\t\tItem\t\t\tPrice\t\tQty Available")
    print(item_1)
    print(item_2)
    print(item_3)
    print(item_4)
    print(item_5)
    print(item_6)
    print(item_7)
    
def product_purchase(item_dict, price_dict, list_keys, qty_available_dict, item_1, item_2, item_3, item_4, item_5, item_6, item_7, purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_keys): 
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
                    item_purchase(item_dict, price_dict, product_id, qty_available_dict, list_keys, item_1, item_2, item_3, item_4, item_5, item_6, item_7, purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_keys)
                else: 
                    item+=1
            print()
            menu_print(item_1, item_2, item_3, item_4, item_5, item_6, item_7)
            #print("Invalid product ID, please try again.")

def item_purchase(list_keys, qty_available_dict, desired_product_id, price_dict, item_dict, item_1, item_2, item_3, item_4, item_5, item_6, item_7, purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_keys):
    #print(list_keys)
    #print(item_dict)
    #print(desired_product_id)
    #print(price_dict)
    #print(qty_available_dict)
    qty_purchase = -1.01
    #print(qty_available_dict[desired_product_id])
    while qty_purchase == -1.01:
        qty_purchase = validation_object.checkInt2(input("\nHow many items would you like the purchase? Enter negative number for returns. "))
        if qty_purchase == -1.01:
            print("This is not a valid quantity. Try again.")
        elif list_keys[0] == desired_product_id: 
            item_1.purchase(qty_purchase)
            purchase_1.set_id(list_keys[0])
            purchase_1.set_name(item_dict[list_keys[0]])
            purchase_1.set_price(price_dict[list_keys[0]])
            purchase_1.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)
        elif list_keys[1] == desired_product_id: 
            item_2.purchase(qty_purchase)
            purchase_2.set_id(list_keys[1])
            purchase_2.set_name(item_dict[list_keys[1]])
            purchase_2.set_price(price_dict[list_keys[1]])
            purchase_2.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)
        elif list_keys[2] == desired_product_id: 
            item_3.purchase(qty_purchase)
            purchase_3.set_id(list_keys[2])
            purchase_3.set_name(item_dict[list_keys[2]])
            purchase_3.set_price(price_dict[list_keys[2]])
            purchase_3.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)
        elif list_keys[3] == desired_product_id: 
            item_4.purchase(qty_purchase)
            purchase_4.set_id(list_keys[3])
            purchase_4.set_name(item_dict[list_keys[3]])
            purchase_4.set_price(price_dict[list_keys[3]])
            purchase_4.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)
        elif list_keys[4] == desired_product_id: 
            item_5.purchase(qty_purchase)
            purchase_5.set_id(list_keys[4])
            purchase_5.set_name(item_dict[list_keys[4]])
            purchase_5.set_price(price_dict[list_keys[4]])
            purchase_5.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)
        elif list_keys[5] == desired_product_id: 
            item_6.purchase(qty_purchase)
            purchase_6.set_id(list_keys[5])
            purchase_6.set_name(item_dict[list_keys[5]])
            purchase_6.set_price(price_dict[list_keys[5]])
            purchase_6.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)
        elif list_keys[6] == desired_product_id: 
            item_7.purchase(qty_purchase)
            purchase_7.set_id(list_keys[6])
            purchase_7.set_name(item_dict[list_keys[6]])
            purchase_7.set_price(price_dict[list_keys[6]])
            purchase_7.set_qty(qty_purchase)
            purchase_keys.append(desired_product_id)

def end_menu(purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_keys):
    tax = 0.085
    #print(purchase_keys)
    print("\nOrder Complete. See Invoice Below:\nID\t\t\t\t\t\tName\t\t\tQuantity\t\tPrice\t\tTotal Price")
    for item in purchase_keys:
        if item == purchase_1.get_id():
            print(purchase_1, "\t$", format(purchase_1.calc_cost(), ',.2f'))
        elif item == purchase_2.get_id():
            print(purchase_2, "\t$", format(purchase_2.calc_cost(), ',.2f'))
        elif item == purchase_3.get_id():
            print(purchase_3, "\t$", format(purchase_3.calc_cost(), ',.2f'))
        elif item == purchase_4.get_id():
            print(purchase_4, "\t$", format(purchase_4.calc_cost(), ',.2f'))
        elif item == purchase_5.get_id():
            print(purchase_5, "\t$", format(purchase_5.calc_cost(), ',.2f'))
        elif item == purchase_6.get_id():
            print(purchase_6, "\t$", format(purchase_6.calc_cost(), ',.2f'))
        elif item == purchase_7.get_id():
            print(purchase_7, "\t$", format(purchase_7.calc_cost(), ',.2f'))
        else: 
            item+=1
    
    total_items = purchase_1.get_gty() + purchase_2.get_gty() + purchase_3.get_gty() + purchase_4.get_gty() + purchase_5.get_gty() + purchase_6.get_gty() + purchase_7.get_gty()
    subtotal = purchase_1.calc_cost() + purchase_2.calc_cost() + purchase_3.calc_cost() + purchase_4.calc_cost() + purchase_5.calc_cost() + purchase_6.calc_cost() + purchase_7.calc_cost()
    sales_tax = subtotal * tax
    grand_total = subtotal + sales_tax
    print("\nTotal Items: $"+format(total_items, ',.2f'))
    print("Subtotal: $"+format(subtotal, ',.2f'))
    print("Sales Tax: $"+format(sales_tax, ',.2f'))
    print("Grand Total: $"+format(grand_total, ',.2f'))

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
