from FrontEndLogic import Frontend
from BusinessLogic import BikeRental, Customer
import time

Frontend.DeclareStartingInventory()
BikeRental.GetBikeType()
Frontend.DeclareInvType()

global currentCustID
global lstCustID
global lstCustLName

count = 0

################################################
# Name: New Customer Menu
# Abstract: This goes displays and prompts the new customer menu
################################################
def NewCustomerMenu():
    while True:
        print("""
        ----New Customer Menu----""")
        
        if(int(len(lstCustID)) != 0):
            print("""
        Current Customer: {}""".format(lstCustLName[currentCustID]))
        
        print("""
        1. Register as New Customer
        2. Rent Bike by Hour - $5
        3. Rent Bike by Day - $20
        4. Rent Bike by Week - $60
        5. Go to Main Menu""")

        choice = input("""         
        Enter choice: """)

        try:
            choice = int(choice)

        except ValueError:

            print("""
        That's not an int!""")

            continue
        if choice == 1:
            display = Frontend.DeclareNewCustomer()
            currentCustID, strLName = display
            
            #store customer information in array
            lstCustID.append(currentCustID)
            lstCustLName.append(strLName)

        elif choice == 2:
            Frontend.RentbyHour(currentCustID)

        elif choice == 3:
            Frontend.RentbyDay(currentCustID)

        elif choice == 4:
            Frontend.RentbyWeek(currentCustID)

        elif choice == 5:
            return currentCustID

        else:
            print("Invalid input. Please enter number between 1-5 ")

################################################
# Name: Returning Customer Menu
# Abstract: This method displays and prompts the returning customer menu
################################################
def ReturnCustomerMenu(currentCustID):
    while True:
        print("""
        ----Return Customer Menu----""")
        
        if(int(len(lstCustID)) != 0):
            print("""
        Current Customer: {}""".format(lstCustLName[currentCustID]))
        
        print("""
        1. Returning Customer - Find by ID
        2. Returning Customer - Find by Last Name
        3. Return Bikes
        4. Go to Main Menu""")

        choice = input("""         
        Enter choice: """)

        try:
            choice = int(choice)

        except ValueError:

            print("""
        That's not an int!""")

            continue
        if choice == 1:
            display = Frontend.PullCustID()
            intCustID, strLName = display
            currentCustID = intCustID

        elif choice == 2:
            display = Frontend.PullCustLName()
            intCustID, strLName = display
            
            currentCustID = intCustID

        elif choice == 3:
            Frontend.ReturnBike(currentCustID)
            Frontend.CalculateBills(currentCustID)
            Frontend.PrintInvoice(currentCustID)

        elif choice == 4:
            return currentCustID

        else:
            print("""
        Invalid input. Please enter number between 1-4 """)

################################################
# Name: Main
# Abstract: Main program
################################################

while True:
        
        count += 1

        if(count == 1):
            lstCustID = []
            lstCustLName = []

        print("""
        ====== Bike Rental Shop (Main Menu) =======
        """)
        if(int(len(lstCustID)) != 0):
            print("""
        Current Customer: {}""".format(lstCustLName[currentCustID]))

        print("""
        1. Show Inventory
        2. New Customers 
        3. Returning Customer
        4. Exit
        """)
        
        choice = input("""         
        Enter choice: """)

        try:
            choice = int(choice)

        except ValueError:

            print("""
        That's not an int!""")

            continue

        if choice == 1:
            display = BikeRental.DisplayAllBikeTypes()
            bike1, bike2, bike3 = display
            print('There are {}, {}, and {} bikes available.'.format(bike1, bike2, bike3))

        elif choice == 2:
            currentCustID = NewCustomerMenu()

        elif choice == 3:
            currentCustID = ReturnCustomerMenu(currentCustID)

        elif choice == 4:
            print("""
        Thank you for shopping with us!""")
            time.sleep(3)
            break

        else:
            print("""
        Invalid input. Please enter number between 1-4 """)        
