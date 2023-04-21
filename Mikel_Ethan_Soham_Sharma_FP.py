#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:40:15 2023

@author: ethanmikel
"""
#Author: Ethan Mikel and Soham Sharma
#Final Project Name: Inventory Management for a Baking Supply Shop 
#Due Date: April 26 By 11:59 PM
#Program Description: The program writes an application to store and manage existing inventory, and allow customers to purchase or return bakery supplies. This specific file contains the code for writing the main file for the program.


#imports the classes and validation files
import Mikel_Ethan_Soham_Sharma_Classes
import Final_Project_Validation

#creates an instance of the validation class from Final_Project_Validation file
validation_object = Final_Project_Validation.ValidationClass()

#defines the main funtion
def main():
    #creates three seperate empty dictionaries to store item id, price and item quantity available respectively
    item_dict = {}
    price_dict = {}
    qty_available_dict = {}

    #calls the create_dictionaries_inventory function that populates the dictionary with data from Inventory.txt
    create_dictionaries_inventory(item_dict, price_dict, qty_available_dict)

    #creates a list to store the key values on item dictionary
    list_keys = list(item_dict.keys())

    #creates a second dictionary to store inventory objects
    item_2_dict = {}
    
    #loops through the keys of the item_dict dictionary to create an inventory object and store it in item_2_dict dictionary 
    for i in range(len(item_dict)):
        item_2_dict[list_keys[i]] = Mikel_Ethan_Soham_Sharma_Classes.Inventory(list_keys[i], item_dict[list_keys[i]], price_dict[list_keys[i]], qty_available_dict[list_keys[i]])

    #creates a second dictionary to store TransactionItem objects
    purchase_dict = {}

    #loops through the values in list_keys list and adds a new key value pair to purchase_dict dictionary for every item name in the list_keys list
    for i in range(len(list_keys)):
        purchase_dict[list_keys[i]] = Mikel_Ethan_Soham_Sharma_Classes.TransactionItem()

    #creates an empty list to store the keys of items that have been purchased
    purchase_keys = []

    #calls the menu_print function to display the menu of available products
    menu_print(item_2_dict)

    #calls the product_purchase function that starts the purchase process
    product_purchase(list_keys, qty_available_dict, item_dict, price_dict, item_2_dict, purchase_dict, purchase_keys) 
        
#defines a function to populate the item, price, and quantity dictionaries with data from Inventory.txt
def create_dictionaries_inventory(item_dict, price_dict, qty_available_dict):
    
    #opens the Inventory.txt file in read mode
    inventory_file = open('Inventory.txt', 'r')
    
    #reads the first line of the file and remove \n
    id_key = inventory_file.readline().rstrip("\n")

    #while loop that loops until the end of the file is reached 
    while id_key != '':
        #converts the id_key to an integer
        id_key = int(id_key)
        #reads the next three lines from the file and remove \n
        item = inventory_file.readline().rstrip('\n')
        qty_available = int(inventory_file.readline().rstrip('\n'))
        price = float(inventory_file.readline().rstrip('\n'))

        #adds the information to the corresponding dictionaries
        item_dict[id_key] = item
        price_dict[id_key] = price
        qty_available_dict[id_key] = qty_available

        #reads the next line which is the id key for the next item and removes the \n
        id_key = inventory_file.readline().rstrip("\n")

    #closes the file
    inventory_file.close()

#defines a function to display the available products in the inventory
def menu_print(item_2_dict):
    #prints the header of the display meny
    print("ID\t\t\tItem\t\t\tPrice\t\t\tQty Available")
    #loops through the keys in the item_2_dictionary and displays the values 
    for i in item_2_dict:
        print(item_2_dict[i])

#defines a function that allows user to purchase product by entering item id
def product_purchase(list_keys, qty_available_dict, item_dict, price_dict, item_2_dict, purchase_dict, purchase_keys): 

    #sets the initial values of the product_id and count variables
    product_id = -1
    count = 0

    #while loops that runs until the user enters 0 to exit
    while product_id == -1 or product_id != 0:
        
        #prompts the user for a product ID and increments the count variable
        product_id = validation_object.checkInt(input("\nWhich product ID would you like to purchase? Enter 0 to exit. "))
        count+=1

        #displays an error message if the user enters invalid product id
        if product_id == -1:
            print("Invalid product ID. Please try again.")
<<<<<<< HEAD

        #if the user enters 0 to exit, either thank the user for visiting the store if its their first purchase or print the end menu
=======
>>>>>>> 7a046ab7362d988ff818d9478f319aae8f129618
        elif product_id == 0:
            #thanks the user for visiting the store if its their first purchase and updates the inventory in dictionary
            if count == 1:
                print("Thank you for visiting our store!")
                update_inventory(list_keys, item_2_dict)

            #prints the end menu if the user has made a purchase before and updates the inventory dictionary
            else:
                update_inventory(list_keys, item_2_dict)
                end_menu(purchase_dict, purchase_keys)
                
        #if the user entered a valid product id, checks if it exists in the inventory dictionary
        else: 
            if product_id in item_2_dict:
                 #if it exists, it prompts the user for the quantity they want to purchase and calls the item_purchase function
                item_purchase(product_id, list_keys, qty_available_dict, item_dict, item_2_dict, price_dict, purchase_dict, purchase_keys)
            #if it doesn't exist in the inventory dictionary, it prompts the user to try again
            elif product_id not in item_2_dict:
                print("Invalid product ID. Please try again.")
            #menu_print(item_2_dict)

#defines a function that allows a user to purchase a certain quantity of a product or return a specific quantity
def item_purchase(product_id, list_keys, qty_available_dict, item_dict, item_2_dict, price_dict, purchase_dict, purchase_keys):
    #initializes flag variable to True
    flag = True 
    #initialize quantity purchased to -1.01 (invalid value)
    qty_purchase = -1.01
    #initialize position to 0
    position = 0
        
    #while loop that asks for quantity purchased until a valid value is entered
    while qty_purchase == -1.01 or qty_purchase == -1.02:
<<<<<<< HEAD
        
        #asks the user for quantity to purchase
        qty_purchase = validation_object.checkInt2(input("\nHow many items would you like the purchase? Enter negative number for returns. "))
        
        #checks if the entered quantity is invalid and prints an error message if the quantity for purchase is invalid
        if qty_purchase == -1.01 or qty_purchase == 0:
            print("This is not a valid quantity. Try again.")
            qty_purchase = -1.01
            
        #if the entered quantity is positive, it updates item stock and purchase history
=======
        qty_purchase = validation_object.checkInt2(input("\nHow many items would you like to purchase? Enter negative number for returns. "))
        if qty_purchase == -1.01 or qty_purchase == 0:
            print("That is not a valid quantity. Try again.")
            qty_purchase = -1.01 
>>>>>>> 7a046ab7362d988ff818d9478f319aae8f129618
        if qty_purchase > 0: 
            #loops through the list of keys of product id
            for i in list_keys:
                if i == product_id and qty_purchase != -1.01:
                    #gets the current stock quantity for the item
                    temp_quantity = item_2_dict[i].get_stock()
                    #attempts to purchase the desired quantity of the item
                    flag = item_2_dict[i].purchase(qty_purchase)
                    #if there is insufficient stock, prints an error message and reprints the menu
                    if flag == False:
                        print("There is not enough inventory to purchase this amount. Try again.\n")
                        menu_print(item_2_dict)
                    #if the purchase is successful, updates the purchase history and reprints the menu
                    elif flag == True:
                        purchase_dict[i].set_id(i)
                        purchase_dict[i].set_name(item_dict[i])
                        purchase_dict[i].set_price(price_dict[i])
                        purchase_dict[i].set_qty(qty_purchase)
                        print()
                        menu_print(item_2_dict)

        #if the entered quantity is negative for returns, it updates item stock and purchase history
        else: 
            #finds the position of the item in the list of keys
            for i in list_keys:
                if i == product_id and qty_purchase != -1.01:
                    #attempts to restock the desired quantity of the item
                    flag = item_2_dict[i].restock(qty_purchase)
                    #if there is insufficient stock to restock, sets quantity purchased to -1.02 (invalid value)
                    if flag == False:
                        qty_purchase == -1.02
                    #if the restock is successful, updates the purchase history and reprint the menu
                    elif flag == True:
                        purchase_dict[i].set_id(i)
                        purchase_dict[i].set_name(item_dict[i])
                        purchase_dict[i].set_price(price_dict[i])
                        purchase_dict[i].set_qty(qty_purchase)
                        print()
                        menu_print(item_2_dict)
                        
        #adds the product ID to the purchase keys list if it is not already in the list
        if product_id not in purchase_keys:
            purchase_keys.append(product_id) 

# defines a function that updates the inventory file with the current stock of each item in the dictionary
def update_inventory(list_keys, item_2_dict):

    #opens the file UpdatedInventory.txt in writing mode
    updated_inventory = open('UpdatedInventory.txt', 'w')
    #loops through keys in item_2_dict dictionary and writes the id, name, stock, and price of the item to the file, each on a new line
    for i in item_2_dict:
        updated_inventory.write(str(item_2_dict[i].get_id())+"\n")
        updated_inventory.write(str(item_2_dict[i].get_name())+"\n")
        updated_inventory.write(str(item_2_dict[i].get_stock())+"\n")
        updated_inventory.write(str(item_2_dict[i].get_price())+"\n")
    
#defines a function that displays the invoice for a customer's purchase
def end_menu(purchase_dict, purchase_keys):

    #sets the tax rate to 8.5%
    tax = 0.085

    #initializes the variables for tracking total items, subtotal, and position
    total_item = 0
    subtotal = 0.0
    position = 0

    #prints the message after completing the order and the header for the menu
    print("\nOrder Complete. See Invoice Below:\nID\t\t\tName\t\t\t\tQuantity\tPrice\t\tTotal Price")

    #loops through the items in the list that stores the keys of items that have been purchased
    for item in purchase_keys:
        #prints the item name, quantity, price, and total price 
        #print(purchase_dict[purchase_keys[item]])
        print(purchase_dict[item], "\t$", format(purchase_dict[item].calc_cost(), ',.2f'))
        #updates the total number of items and the subtotal
        total_item += purchase_dict[item].get_qty()
        subtotal += purchase_dict[item].calc_cost()

    #calculates and saves the sales tax on purchase in the sales_tax variable
    sales_tax = subtotal * tax
    #calculates the grand total by adding sales tax to subtotal and saves in the grand_total variable
    grand_total = subtotal + sales_tax
    #prints the total items, subtotal, sales, tax and grand total formatted as per the requirements
    print("\nTotal Items:",format(total_item, ',.0f'))
    print("Subtotal: $"+format(subtotal, ',.2f'))
    print("Sales Tax: $"+format(sales_tax, ',.2f'))
    print("Grand Total: $"+format(grand_total, ',.2f'))

#calls the main function
main()

