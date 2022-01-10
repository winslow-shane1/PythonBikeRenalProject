from BusinessLogic import BikeRental, Customer
import datetime

class Frontend:

    ################################################################################################
    # Name: Declare Inventory Starting Inventory
    # Desc: Function is called to identify the number of total bike available at store opening
    ################################################################################################
    def DeclareStartingInventory():
        global blnValidate
        strStartingInv = input("Enter the starting inventory for the bike shop: ")
        try:
            intStartingInv = int(strStartingInv)
        except:
            print("Starting Inventory Number must be an Integer")
            blnValidate = False
            return

        if intStartingInv < 1:
            blnValidate = False
            print("Starting Inventory Number must be at least 1")
            return None

        BikeRental(intStartingInv)
   
    ################################################################################################
    # Name: Declare Inventory Type
    # Desc: Function used to identify the number of bikes for the different bike types at bike shop
    ################################################################################################
    def DeclareInvType():
        strBike = ""
        global blnValidate
    
        BikeRental.BikeCode(1)
        strBike = BikeRental.SetBikeName(1)
        strInventoryType1 = input('Enter the number of {} bike(s) available: '.format(strBike))
        try: 
            intInventoryType1 = int(strInventoryType1)
        except:
            print("Inventory Amount for {} bike(s) must be an Integer".format(strBike))
            blnValidate = False
            return None
        if intInventoryType1 < 0:
            print("Inventory Amount for {} bike(s) must be greater than or equal to 0".format(strBike))
            blnValidate = False 
            return None
        if intInventoryType1 > BikeRental.intCurrentInv:
            blnValidate = False
            print("Inventory Type cannot be greater than the Starting Inventory")
            return None

        BikeRental.BikeCode(2)
        strBike = BikeRental.SetBikeName(2)
        strInventoryType2 = input('Enter the number of {} bike(s) available: '.format(strBike))
        try: 
            intInventoryType2 = int(strInventoryType2)
        except:
            print("Inventory Amount for {} bike(s) must be an Integer".format(strBike))
            blnValidate = False
            return None
        if intInventoryType2 < 0:
            print("Inventory Amount for {} bike(s) must be greater than or equal to 0".format(strBike))
            blnValidate = False 
            return None
        if intInventoryType2 > BikeRental.intCurrentInv:
            blnValidate = False
            print("Inventory Type cannot be greater than the Starting Inventory")
            return None

        BikeRental.BikeCode(3)
        strBike = BikeRental.SetBikeName(3)
        strInventoryType3 = input('Enter the number of {} bike(s) available: '.format(strBike))
        try: 
            intInventoryType3 = int(strInventoryType3)
        except:
            print("Inventory Amount for {} bike(s) must be an Integer".format(strBike))
            blnValidate = False
            return None
        if intInventoryType3 < 0:
            print("Inventory Amount for {} bike(s) must be greater than or equal to 0".format(strBike))
            blnValidate = False 
            return None
        if intInventoryType3 > BikeRental.intCurrentInv:
            blnValidate = False
            print("Inventory Type cannot be greater than the Starting Inventory")
            return None

        if intInventoryType1 + intInventoryType2 + intInventoryType3 > BikeRental.intCurrentInv:
            blnValidate = False
            print("Inventory Types cannot have combined value greater than Starting Inventory")
            return None

        BikeRental.TypeInventory(intInventoryType1, intInventoryType2, intInventoryType3)

    ########################################################################################################
    # Name: Declare New Customer
    # Desc: Function to create/record a new customer within the program, and store their first and last name
    #########################################################################################################
    def DeclareNewCustomer():
        global blnValidate
        global lstCustID
        global lstCustLName

        strFname = ""
        strLname = ""
    
        strFname = input("""
                Enter customer first name: """)
        strLname = input("""
                Enter customer last name: """)

        if strFname == "":
            blnValidate = False
            return None

        if strLname == "":
            blnValidate = False
            return None

        intNewID = int(len(lstCustID))

        lstCustID.append(intNewID)
        lstCustLName.append(strLname)

        lstCustID[intNewID] = Customer(strFname, strLname)
        
        print("""
                Thank you, your ID# is {}""".format(intNewID))
        return intNewID, strLname

    ################################################################################################
    # Name: Declare Inventory Type
    # Desc: Function used to identify the number of bikes for the different bike types at bike shop
    ################################################################################################
    def RequestBike(intCurrentCust):
        intBikeCode = 0
        intBikeAmount = 0
        strBikeCode = ""
        strBikeAmount = ""
        request = BikeRental.DisplayAllBikeTypes()
        intType1, intType2, intType3 = request

        strBikeCode = input("""
                Types of Bike(s) Available to Rent:
    
                1. {} bike(s)
                2. {} bike(s)
                3. {} bike(s)
    
                Enter which bike type customer would like: """.format(intType1, intType2, intType3))

        intBikeCode = int(strBikeCode)
        BikeRental.BikeCode(intBikeCode)
    
        strBikeType = BikeRental.SetBikeName()
        strBikeAmount = input("""
                Enter the number of {} bike(s) customer would like to rent:""".format(strBikeType))
        intBikeAmount = int(strBikeAmount)

        lstCustID[intCurrentCust].RequestBike(intBikeCode, intBikeAmount)
    
        print("""
                Thank you for your request""")

    ################################################################################################
    # Name: Rent Bike by Hour 
    # Desc: Function used to rent a bike by the hour with the bike shop
    ################################################################################################
    def RentbyHour(intCurrentCust):
        strHours = ""
        intHours = 0
        strHours = input("""
                Enter the number of hours of rental:""")
        intHours = int(strHours)

        lstCustID[intCurrentCust].intHours = intHours
        
        numBikes = int(input("""
                Enter the number of bikes to rent:"""))
        bikeType = int(input("""
                Enter the bike type code you would like to rent
                
                1. Mountain Bikes
                2. Street Bikes
                3. BMX Bikes
                
                Enter Selection:"""))

        lstCustID[intCurrentCust].RequestBike(bikeType, numBikes)
        BikeRental.RentBike(lstCustID[intCurrentCust])
       
    ################################################################################################
    # Name: Rent Bike by Hour 
    # Desc: Function used to rent a bike by the hour with the bike shop
    ################################################################################################
    def RentbyDay(intCurrentCust):
        strDays = ""
        intDays = 0
        strDays = input("""
                Enter the number of hours of rental:""")
        intDays = int(strDays)

        lstCustID[intCurrentCust].intDays = intDays
        
        numBikes = int(input("""
                Enter the number of bikes to rent:"""))
        bikeType = int(input("""
                Enter the bike type code you would like to rent
                
                1. Mountain Bikes
                2. Street Bikes
                3. BMX Bikes
                
                Enter Selection:"""))

        lstCustID[intCurrentCust].RequestBike(bikeType, numBikes)
        BikeRental.RentBike(lstCustID[intCurrentCust])
    
    ################################################################################################
    # Name: Rent Bike by Week 
    # Desc: Function used to rent a bike by the week with the bike shop
    ################################################################################################
    def RentbyWeek(intCurrentCust):
        strWeeks = ""
        intWeeks = 0
        strWeeks = input("""
                Enter the number of weeks of rental: """)
        intWeeks = int(strWeeks)

        lstCustID[intCurrentCust].intWeeks = intWeeks
        
        numBikes = int(input("""
                Enter the number of bikes to rent:"""))
        bikeType = int(input("""
                Enter the bike type code you would like to rent
                
                1. Mountain Bikes
                2. Street Bikes
                3. BMX Bikes
                
                Enter Selection:"""))

        lstCustID[intCurrentCust].RequestBike(bikeType, numBikes)
        BikeRental.RentBike(lstCustID[intCurrentCust])


    ################################################################################################
    # Name: Return Bike
    # Desc: Function used to Return Bike to the Bike Shop
    ################################################################################################
    def ReturnBike(intCurrentCust):
        print("""
                You are now returning your bike""")
        BikeRental.CalculateRentalPeriod(lstCustID[intCurrentCust])
        
        #FOR BOBS TESTING PURPOSES TO MODIFY TIME PERIOD OF RENTAL
        if lstCustID[intCurrentCust].intHours > 0:
            lstCustID[intCurrentCust].dtmRentalPeriod = lstCustID[intCurrentCust].dtmRentalPeriod + datetime.timedelta(hours=lstCustID[intCurrentCust].intHours)
            lstCustID[intCurrentCust].intHours = 0
        elif lstCustID[intCurrentCust].intDays > 0:
            lstCustID[intCurrentCust].dtmRentalPeriod = lstCustID[intCurrentCust].dtmRentalPeriod + datetime.timedelta(days=lstCustID[intCurrentCust].intDays)
            lstCustID[intCurrentCust].intDays = 0
        elif lstCustID[intCurrentCust].intWeeks > 0:
            lstCustID[intCurrentCust].dtmRentalPeriod = lstCustID[intCurrentCust].dtmRentalPeriod + datetime.timedelta(weeks=lstCustID[intCurrentCust].intWeeks)
            lstCustID[intCurrentCust].intWeeks = 0

        print("""
                Bike(s) have been received""")

    ################################################################################################
    # Name: Calculate Bill
    # Desc: Function used to Calculate the Base Amount, Apply Discounts, and Calculate Final Bill
    ################################################################################################
    def CalculateBills(intCurrentCust):
        BikeRental.CalculateBaseAmount(lstCustID[intCurrentCust])
        BikeRental.ApplyDiscounts(lstCustID[intCurrentCust])
        BikeRental.CalculateFinalBill(lstCustID[intCurrentCust])

        print("""
                Customer Base Amount due is ${:,.2f}""".format(lstCustID[intCurrentCust].dblBaseAmountDue))
        print("""
                Customer Amount of Discount applied is ${:,.2f}""".format(lstCustID[intCurrentCust].dblAmountofDiscount))
        print("""
                Customer Final Amount due, after discounts applied is  ${:,.2f}""".format(lstCustID[intCurrentCust].dblTotalAmountDue))

    ################################################################################################
    # Name: Print Invoice
    # Desc: Function used to print an invoice of the entire transaction for a specific customer
    ################################################################################################
    def PrintInvoice(intCurrentCust):
        request = lstCustID[intCurrentCust].DisplayInvoice()
        strFname, strLname, intBikeCode, intTotalNumBikes, dtmRentalPeriod, dblBaseAmountDue, dblAmountofDiscount, dblTotalAmountDue = request
        print("""
                ----Customer Invoice----
                Customer First Name:   {}
                Customer Last Name:    {}
                Bike Type Rented:      {}
                Total Bikes Rented:    {}
                Total Rental Period:   {}
                Original Amount Due:   ${:,.2f}
                Amount of Discount:    ${:,.2f}
                Final Amount Due:      ${:,.2f}""".format(strFname, strLname, intBikeCode, intTotalNumBikes, dtmRentalPeriod, dblBaseAmountDue, dblAmountofDiscount, dblTotalAmountDue))

    ################################################################################################
    # Name: Pull in Existing Customer by ID
    # Desc: Function used to identify Customer by ID
    ################################################################################################
    def PullCustID():
        global lstCustLName
        intCustID = int(input("""
                Enter Customer ID: """))

        strLastName = lstCustLName[intCustID]

        print("""
                Customer Found!

                Customer Name: {}
                Customer Id:   {}""".format(strLastName, intCustID))

        return intCustID, strLastName

    ################################################################################################
    # Name: Pull in Existing Customer by Last Name
    # Desc: Function used to identify Customer by last name
    ################################################################################################
    def PullCustLName():
        intCustID = 0
        global lstCustLName
        strLastName = input("""
                Enter customer last name to search existing customers: """)

        intCustID = lstCustLName.index(strLastName)
        print("""
                Customer Found!

                Customer Name: {}
                Customer Id:   {}""".format(strLName, intCustID))
        return intCustID, strLastName

##################################################################################################
# MAIN
##################################################################################################
blnValidate = bool(True)
lstCustID = []
lstCustLName = []
    #Instantiate the bike shop inventory
    #DeclareStartingInventory()
    #intInvAmount = BikeRental.DisplayCurrentTotalInv()
    #print(intInvAmount)

    #Identify the differnent quantities of bike types currently at the bike shop
    #DeclareInvType()
    #InvAmounts = BikeRental.DisplayAllInventory()
    #Total, Mountain, Road, Touring = InvAmounts
    #print(Total, Mountain, Road, Touring)

    #Instantiate 2 new customers
    #intCurrentCust = DeclareNewCustomer()
    #Note we will be using the intCurrentCust variable populated with value 1 for the remainder of the transaction
    #intCurrentCust = DeclareNewCustomer()

    #print(lstCustID[0].strLname)
    #print(lstCustID[1].strLname)

    #Associate Existing Customer to program
    #intCurrentCustomer = PullCustID()

    #Search for Existing Custoemer in program
    #intCurrentCustomer = PullCustPullCustLName()

    #Allow intCurrentCust to request a bike
    #RequestBike(intCurrentCust)
    #Allow intCurrentCust to rent a bike the hour
    #RentBikebyHour(intCurrentCust)
    #Allow intCurrentCust to return the bikes
    #ReturnBike(intCurrentCust)

    #illustrate the new Rental period modified by the hours of rent identified by the user previously
    #print(lstCustID[intCurrentCust].dtmRentalPeriod)

    #Ccalculate the Bill for intCurrentCust
    #CalculateBills(intCurrentCust)

    #Print the invoice of intCurrentCust
    #PrintInvoice(intCurrentCust)


