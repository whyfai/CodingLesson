# Functions
def sell_item():
        global stock
        os.system("cls")
        if stock == 0:
            print("No stock left! Please restock")
            return
        while True:
            global quantity
            quantity = int(input(f"Input item's quantity [1-{stock}]"))
            if quantity >= 1 and quantity <= stock:
                stock -= quantity
                break
        
        while True:
            global discount
            discount = int(input("Input item's discount [0%-50%]"))
            if discount <= 50:
                break
        
        print("ES Companies Portal - Invoice")
        print("===================================")
        print(f"Item's name     : {item_name}")
        print(f"Item's price    : ${item_price}")
        print(f"Item's quantity : {quantity}")
        print(f"Item's discount : {discount}%")
        print("\n")
        subtotal = item_price * quantity
        total = subtotal - (subtotal * discount / 100)
        print(f"You have to pay ${total}")
        
        while True:
            payment = float(input(f"Input your money [use decimal numbers | min {total}] : $"))
            if payment >= total:
                break
            
        print("Thanks for purchasing!")
        print(f"Change: ${payment-total}")


def restock_item():
    global stock
    space_left = 100-stock
    if space_left == 0:
        print("There is no space left! Sell your items")
        return
    while True:
        restock = int(input(f"Input stock to add [1-{space_left}] :"))
        if restock <= space_left and restock >= 1:
            stock += restock
            print("Success add stock!")
            break


# ===================================
print("")
print("===================================")
print("ES Companies Portal - Cashier App 3")
print("===================================")
while True:
    item_name = input("Input item name [5-30 characters] :")
    if len(item_name) <= 30 and len(item_name) >= 5:
        break

while True:
    item_price = int(input("Input item price [$10-$2000] :"))
    if item_price >= 10 and item_price <= 2000:
        break

import os

os.system("cls")

stock = 50

while True:
    print("What will you do?")
    print("===================================")
    print("1. Sell Item")
    print("2. Restock Item")
    print("3. Exit")

    option = input("Choose :")
    
    if option == "1":
        sell_item()
    if option == "2":
        restock_item()
    if option == "3":
        break