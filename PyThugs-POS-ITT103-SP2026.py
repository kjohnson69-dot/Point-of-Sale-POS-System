import datetime

# -----------------------------------------------
# Declaring Variables
cart = []
itemQuantity = []
Subtotal = 0
selectedItem = 0
Tax = 0.10
customerNumber = 0

# Store Info
Store = "Best Buy Retail Store"
Address = "Shop 124, Python Lane, Kingston 10"
Tel = "Tel: 876-345-4567 or 876-765-4321"

"""
#Creating inventory for products
#Products Inventory [Name, Unit Price, Stock, Serial number ]
These correspond to the indices [0, 1, 2, 3] respectively.
"""
products = [
    ["Brown Sugar", 260, 50, "sugar001"],
    ["Apple Juice", 700, 15, "juice001"],
    ["Paper Towel", 1200, 50, "towel001"],
    ["Corn Beef", 450, 70, "beef001"],
    ["Pineapple", 350, 25, "pineapple001"],
    ["Bread", 589, 4, "bread001"],
    ["Apple", 120, 30, "apple001"],
    ["Shrimp", 4212, 28, "shrimp001"],
    ["Butter", 3000, 18, "butter001"],
    ["Rice", 100, 41, "rice001"]
]

#Formatting receipt with multiline f-strings within a function
unit = "Unit Price ($)"
total = "Total Price ($)"
qty = "Qty"
itemselected = "Item"

# -----------------------------------------------
# Functions

#Function that stores receipt heading
def receipt():
  global customerNumber
  print(f"""\nWelcome to Best Buy Retail
  
------------------------------------------------
{Store}
{Address}
{Tel}
Date: {datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')}
""")

#Function to view available products
def view_products():
    print("\nAvailable Products:")
    print(f"{'Item#':<5}   {itemselected:<20}  {unit:>7}    {'Stock':>10}")
    for index, product in enumerate(products):
        print(f"{index}   {product[0]:<20} {product[1]:>7}  {product[2]:>10}", end="")
        if product[2] < 5:
            print(" (LOW STOCK ALERT)") 
        else:
            print()
            
#Function to view cart when option is selected
def view_cart():
    subtotal = 0
    carttotal = 0
    salestax = 0
    if cart == []:
        print("Your Cart is empty. Select items to continue")
    else:
        print("\nCustomer's Cart:")
        print(f"{'#':<5} {qty:<5}   {itemselected:<20}  {unit:>7}    {total:>10}")
        for index, cartItem in enumerate(cart):
            print(f"{index+1:<5} {itemQuantity[index]:<5}   {cartItem[0]:<20} {cartItem[1]:>7}  {itemQuantity[index] * cartItem[1]:>15}")
            subtotal += itemQuantity[index] * cartItem[1]

#Displays bill for customers to determine how they want to proceed
    salestax = subtotal * Tax
    carttotal = subtotal + salestax
    print(f"\n{'Subtotal:': >50} ${subtotal:>10,.2f}")
    print(f"{'Sales Tax:': >50} ${salestax:>10,.2f}")
    print(f"{'Total:': >50} ${carttotal:>10,.2f}")

#Check out function 
def checkout_cart():
    if cart == []: #Checking to ensure that users are not able to proceed with an empty cart
        print("Your Cart is empty. Select items to continue")
        return

    print("\nINVOICE".center(50)) #Customer's receipt 
    receipt()
    print(f"{'#':<5} {qty:<5}   {itemselected:<20}  {unit:>7}    {total:>10}")
    
    Subtotal = 0
    for i, cartItem in enumerate(cart):
        print(f"{i+1:<5} {itemQuantity[i]:<5}   {cartItem[0]:<20} {cartItem[1]:>7}  {itemQuantity[i] * cartItem[1]:>15}")
        Subtotal += itemQuantity[i] * cartItem[1]
#Bill Calculations
    discount = 0
    if Subtotal > 5000:
        discount = Subtotal * 0.05
        print(f"\n Discount (5%): ${discount:,.2f}")
        Subtotal -= discount

    Salestax = Subtotal * Tax
    GrandTotal = Subtotal + Salestax

    print(f"\nSubtotal: ${Subtotal:,.2f}")
    print(f"Sales Tax (10%): ${Salestax:,.2f}")
    print(f"Grand Total: ${GrandTotal:,.2f}")

    payment = int(input("Enter payment: "))
    if payment < GrandTotal:
        print("More Money Needed")
        return

    change = payment - GrandTotal
    print(f"Change: ${change}")
    print("-"*80)
    print(f"{'THANK YOU FOR SHOPPING! NO EXCHANGE OR REFUNDS WITHOUT THIS RECEIPT':^50}")

    # Clear cart after checkout to allow process to start for other custoers
    cart.clear()
    itemQuantity.clear()
    global customerNumber
    customerNumber += 1 #Increments after each checkout to specify the customer being served
    
"""
#Restock function. This is important because processes like 
#remove item and clearing cart is taking place so we wanted to ensure the
#inventory continues to reflect accurate data 
"""
def restockItem(serialNumber, inboundQuantity):  
    for index, product in enumerate(products):
        if product[3] == serialNumber:
            product[2] += inboundQuantity
            print(f"'{products[index][0]}' restocked successfully. Current stock: {products[index][2]}")
            break           

# Print products once at the start
def add_to_cart():
    view_products() #Calling the view products function here when user is ready to add items to cart ensures that the list of available products is only displayed once at the start for each customer '''
    
    while True: #starting of the loop for items to be added to cart
        selectedItem = input("\nEnter item number or select x to go back to main menu: ")
        
        
        if selectedItem.lower() == "x": #once user selects x it should take them back to main menu
            break
        
        if not selectedItem.isdigit() or int(selectedItem) >= len(products):
            print("Invalid Selection. Select a number from the list")
            continue  #validating the input for item selection
        
        selectedItem = int(selectedItem) 
        stock = products[selectedItem]
        
        print (f"You selected: {stock[0]}") #user friendly display message to remind user of their selection
        
        if stock[2] <= 0:
            print(f"SORRY!: '{stock[0]}' out-of-stock") #Ensures that out of stock products are not able to add to cart
            continue
        
        quantity = input("Enter quantity: ") #Prompt user to enter quantity of each item before it is added to cart
        if not quantity.isdigit():
            print("Invalid Selection. Enter a number")
            continue
        quantity = int(quantity)
        
        if quantity <= 0 or quantity > stock[2]:
            print(f"Unable to Process Request: Only {stock[2]} '{stock[0]}' available")
            continue
       
       #Update the inventory based on inventory  
        cart.append(stock[:])
        itemQuantity.append(quantity) #Store the quantity selected for that product
        stock[2] -= quantity #Updates the stock by subtracting selected quantity
        
        if stock[2] < 5:
            print("LOW STOCK ALERT")
        
        cost = quantity * stock[1]
        print(f"{quantity} {stock[0]} ${stock[1]} ${cost}")

def showCartItem(cartItemNum):
    print(f"{cart[cartItemNum][0]}".center(50, "-"))
    print(f"{qty:<5}   {itemselected:<20}  {unit:>7}     {total:>10}")
    print(f"{itemQuantity[cartItemNum]:<5}   {cart[cartItemNum][0]:<20} {cart[cartItemNum][1]:>7}  {itemQuantity[cartItemNum] * cart[cartItemNum][1]:>15}") 

#Function to edit cart by removing item or clearing cart
def editCart():
    print(f"Edit Cart".center(50, "-"))
    item_selected = ""
    clear = ""
   
    while item_selected != "x": #Condition for loop, "x" represents back to menu
        view_cart()
        if cart == []: #Empty cart cannnot be edited, this takes care of that
          print("Your Cart is empty. Select items to continue")
          return
      
      #if user wants to clear entire cart, this takes care of that process
        clear = input ("Enter 'c' to clear cart or press Enter to continue")
        if  clear.lower () == "c":
          for index, item in enumerate(cart):
            restockItem(item[3], itemQuantity[index]) #Very important to update stock once items are not checked out
       
          cart.clear() 
          itemQuantity.clear()
          print (f"Cart cleared successfully")
          item_selected = ""
          break
        elif clear == "": #Users are asked to select enter, this represent that input 
          pass
        else:
          print("Invalid input. Please enter 'c' or press Enter.") #Any selection besides "c" or enter will be noted as invalid
          return
          

#If user selects continue instead of clearing the cart, this will prompt them to make individual edits
        item_selected = input("Enter item # to edit or 'x' to go back: ")
       
        
        if item_selected.lower() == "x": # Accepts 'x' or 'X' as input and exits the loop if selected
            break
        
        # Checks if input is a valid cart item number 
        if not item_selected.isdigit() or int(item_selected) > len(cart) or int(item_selected) < 1:
            print("Invalid selection. Please select a valid item number.")
            continue

        index = int(item_selected) - 1
        showCartItem(index)
 
 #Process to remove a selected item. Will delete the entire item from cart and not by quantity
        confirmation = input("Remove item? (yes - y or no - n): ")
        if confirmation.lower() in ["yes", "y"]:
            restockItem(cart[index][3], itemQuantity[index])
            del cart[index]
            del itemQuantity[index]
            print("Item removed from cart Successfully.")

#DISPLAY MENU DISPLAYED AT THE START FOR USER TO SELECT THEIR DESIRED PROCESS
def main_menu():
    global customerNumber
    print("\nMain Menu".center(50, "-"))
    print(f"Now Serving Customer Number # {customerNumber+1}")
    print("1. Add to Cart")
    print("2. View Cart")
    print("3. Edit Cart")
    print("4. Checkout")
    print("5. View Inventory ")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

# -----------------------------------------------
# Program Start: show main menu once to start the program 
choice = main_menu()

# -----------------------------------------------
# Program Loop
while True:
    if choice == "1":
        add_to_cart()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        editCart()
    elif choice == "4":
        checkout_cart()
    elif choice =="5":
      view_products()
    elif choice == "6":
        print("Thank you for shopping! Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

    # Back to main menu after each process
    choice = main_menu()


