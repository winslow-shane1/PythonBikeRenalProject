#-----------------------------------------------------------------------------------------------------------------
# Name: Shane Winslow, Caleb Gregory, and Maison Arroyo
# Team: ?
# Project Name: Bike Rental Object Oriented Project
# Project Desc: Collection of Classes and their related business logic methods for the Customer and Bike shop entities 
#-----------------------------------------------------------------------------------------------------------------
#import datetime feature from Python library
import datetime

class BikeRental:

    #---------------------------------------------------------------------------------------------------------------
    # Name: Class level Variables
    # Desc: Class level variables called to within the different methods of the class
    #---------------------------------------------------------------------------------------------------------------

    #Rental Variables
    intCurrentInv = int(0)
    intInventoryBikeType1 = int(0)
    intInventoryBikeType2 = int(0)
    intInventoryBikeType3 = int(0)
    intBikeCode = int(0)
    intRentalNumber = int(0) 
    dblRentalRate = float(0)
    strBikeName = str ("")
    strBikeName1 = str("")
    strBikeName2 = str("")
    strBikeName3 = str("")
    intTotalBikesRented = int(0)
    dblTotalRevenue = float(0)
    intInventoryBikeTotal = int(0)

    #Discount Variable
    dblFamilyDiscount = float(.25)
    dblCouponDiscount = float(0.1)

    #---------------------------------------------------------------------------------------------------------------
    # Name: Bike Rental constructor
    # Desc: Constructor initializes and instantiates the bikeshop object
    #---------------------------------------------------------------------------------------------------------------

    def __init__(self, intCurrentInv):
        self.intCurrentInv = intCurrentInv

        BikeRental.intCurrentInv = self.intCurrentInv


    #Getter to pull the intStartingInventory variable
    @property
    def intCurrentInv(self):
        return self.__intCurrentInv

    #Setter to verify the intStartingInventory variable is numeric
    @intCurrentInv.setter
    def intCurrentInv(self, intCurrentInv):
        #Test whether or not the variable provided is an integer
        try:
          intTest = int(intCurrentInv)
        
        except:
            raise Exception('Inventory variable must be numeric')
        
        #Create integer variable to use to test intStartInv
        intTest = int(intCurrentInv)
        
        #Test whether the Starting Inventory variable is an integer
        if intTest != intCurrentInv:
            raise Exception ('Inventory Variable must be an integer')

        #Check to ensure that the Starting Inventory Variable is at least 1
        elif intCurrentInv < 1:
            raise Exception('Inventory variable must be at least 1')
        
        #assignment the variable supplied by user as inventory instance variable
        else: 
            self.__intCurrentInv = intCurrentInv

    #---------------------------------------------------------------------------------------------------------------
    # Name: Bike Code 
    # Desc: Method is called to integer of Bike Code within the BikeRental Class variables
    #---------------------------------------------------------------------------------------------------------------
    
    def BikeCode(intBikeCode):
        BikeRental.intBikeCode = intBikeCode
        return BikeRental.intBikeCode

    #---------------------------------------------------------------------------------------------------------------
    # Name: Get Number of Bike Types
    # Desc: Gets Number of different bike types for inventory
    #---------------------------------------------------------------------------------------------------------------
    def GetBikeType(intNumBikeTypes):
        count = 0
        count += 1
        BikeRental.strBikeName1 = input("Define Bike Type #{}:".format(count))

        count += 1
        BikeRental.strBikeName2 = input("Define Bike Type #{}:".format(count))

        count += 1
        BikeRental.strBikeName3 = input("Define Bike Type #{}:".format(count))

    #---------------------------------------------------------------------------------------------------------------
    # Name: Set Bike Name  
    # Desc: Method is used to set the name of the bike based with relation to the Bike Code
    #---------------------------------------------------------------------------------------------------------------
    
    def SetBikeName(intBikeCode):
        if BikeRental.intBikeCode == 1:
            BikeRental.strBikeName = BikeRental.strBikeName1
        
        elif BikeRental.intBikeCode == 2:
            BikeRental.strBikeName = BikeRental.strBikeName2

        elif BikeRental.intBikeCode == 3:
            BikeRental.strBikeName = BikeRental.strBikeName3
            
        return BikeRental.strBikeName
    
    #---------------------------------------------------------------------------------------------------------------
    # Name: Bike Inventory by Type 
    # Desc: Method is called to set the inventory for each bike type
    #---------------------------------------------------------------------------------------------------------------
       
    def TypeInventory(intInventoryBikeType1, intInventoryBikeType2, intInventoryBikeType3):
        BikeRental.intInventoryBikeTotal = intInventoryBikeType1 + intInventoryBikeType2 + intInventoryBikeType3
        intTest1 = isinstance(intInventoryBikeType1, int)
        intTest2 = isinstance(intInventoryBikeType2, int)
        intTest3 = isinstance(intInventoryBikeType3, int)

        if BikeRental.intInventoryBikeTotal > BikeRental.intCurrentInv:
            raise Exception('Error: Bike Types cannot sum to larger than current inventory')
        
        if intTest1 == False:
            raise Exception('Inventory variable must be integer')
        elif intInventoryBikeType1 < 0:
            raise Exception('Inventory Bike Type variable must be greater or equal to 0')
        else:
            BikeRental.intInventoryBikeType1 = intInventoryBikeType1
        
        if intTest2 == False:
            raise Exception('Inventory variable must be integer')
        elif intInventoryBikeType2 < 0:
            raise Exception('Inventory Bike Type variable must be greater or equal to 0')
        else:
            BikeRental.intInventoryBikeType2 = intInventoryBikeType2

        if intTest3 == False:
            raise Exception('Inventory variable must be integer')
        elif intInventoryBikeType3 < 0:
            raise Exception('Inventory Bike Type variable must be greater or equal to 0')
        else:
            BikeRental.intInventoryBikeType3 = intInventoryBikeType3
        
        BikeRental.intInventoryBikeType1 = intInventoryBikeType1
        BikeRental.intInventoryBikeType2 = intInventoryBikeType2
        BikeRental.intInventoryBikeType3 = intInventoryBikeType3

    #---------------------------------------------------------------------------------------------------------------
    # Name: Update Inventory
    # Desc: determine current inventory based off number rented
    #---------------------------------------------------------------------------------------------------------------
    def UpdateInventorty_Rental(self,intRentalNumber):
        BikeRental.intCurrentInv -= intRentalNumber
        
        if BikeRental.intBikeCode == 1:
            BikeRental.intInventoryBikeType1 -= intRentalNumber
            return BikeRental.intInventoryBikeType1

        elif BikeRental.intBikeCode == 2:
            BikeRental.intInventoryBikeType2 -= intRentalNumber
            return BikeRental.intInventoryBikeType2

        elif BikeRental.intBikeCode == 3:
            BikeRental.intInventoryBikeType3 -= intRentalNumber
            return BikeRental.intInventoryBikeType3

    #---------------------------------------------------------------------------------------------------------------
    # Name: Display type of bike rented
    # Desc: determine current inventory based off number rented
    #---------------------------------------------------------------------------------------------------------------
    def DisplayBikeType(self):
        return BikeRental.strBikeName

    #---------------------------------------------------------------------------------------------------------------
    # Name: Display All Bike Types
    # Desc: Returns all bike types to the application 
    #--------------------------------------------------------------------------------------------------------------
    def DisplayAllBikeTypes():
        return BikeRental.strBikeName1, BikeRental.strBikeName2, BikeRental.strBikeName3

    #---------------------------------------------------------------------------------------------------------------
    # Name: Display Bike Type Inventory by Bike Type
    # Desc: Displays the type of Bike rented and number
    #---------------------------------------------------------------------------------------------------------------
    def DisplayBikeTypeInventory():
        if BikeRental.intBikeCode == 0:
            raise Exception('Method needs Bike Code to function')
        
        if BikeRental.intBikeCode == 1:
            return BikeRental.strBikeName, BikeRental.intInventoryBikeType1
            
        elif BikeRental.intBikeCode == 2:
            return BikeRental.strBikeName, BikeRental.intInventoryBikeType2
            
        elif BikeRental.intBikeCode == 3:
            return BikeRental.strBikeName, BikeRental.intInventoryBikeType3

    #---------------------------------------------------------------------------------------------------------------
    # Name: Display All Inventory
    # Desc: Displays entire inventory (Total And by Types)
    #---------------------------------------------------------------------------------------------------------------
    def DisplayAllInventory(self):
        return BikeRental.intCurrentInv, BikeRental.intInventoryBikeType1, BikeRental.intInventoryBikeType2, BikeRental.intInventoryBikeType3

    #---------------------------------------------------------------------------------------------------------------
    # Name: Display Current Total Inventory
    # Desc: Displays the total current inventory
    #---------------------------------------------------------------------------------------------------------------
    def DisplayCurrentTotalInv():
        return BikeRental.intCurrentInv

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Rent Bike
    # Desc: Allows shop to rent bike(s), verify their request is possible, set their time of rental, and updates the inventory accordingly
    #----------------------------------------------------------------------------------------------------------------------------------
    def RentBike(customer):
        #Set boolean variable to validate all rental requests can be fulfilled
        blnValidate = bool(True)

      
        if customer.intBikeCode < 1 or customer.intBikeCode > 3:
            return -1

        if customer.intBikeCode == 1:
            if customer.intTotalNumBikes > BikeRental.intInventoryBikeType1:
                raise Exception('Bike request larger than available supply')
                return -2 
            else: 
                BikeRental.intInventoryBikeType1 -= customer.intTotalNumBikes
                BikeRental.intCurrentInv -= customer.intTotalNumBikes
                BikeRental.intTotalBikesRented += customer.intTotalNumBikes
                now = datetime.datetime.now()                      
                customer.dtmRentalStart = now
            
        elif customer.intBikeCode == 2:
            if customer.intTotalNumBikes > BikeRental.intInventoryBikeType2:
                raise Exception('Bike request larger than available supply')
                return -2 
            else:
                BikeRental.intInventoryBikeType2 -= customer.intTotalNumBikes
                BikeRental.intCurrentInv -= customer.intTotalNumBikes
                BikeRental.intTotalBikesRented += customer.intTotalNumBikes
                now = datetime.datetime.now()                      
                customer.dtmRentalStart = now

        elif self.intBikeCode == 3:
            if customer.intTotalNumBikes > BikeRental.intInventoryBikeType3:
                raise Exception('Bike request larger than available supply')
                return -2
            else:
                BikeRental.intInventoryBikeType3 -= customer.intTotalNumBikes
                BikeRental.intCurrentInv -= customer.intTotalNumBikes
                BikeRental.intTotalBikesRented += customer.intTotalNumBikes
                now = datetime.datetime.now()                      
                self.dtmRentalStart = now

    #-----------------------------------------------------------------------------------------------------------------------------
    # Name: Calculate Rental Period
    # Desc: Allows bike shop to calculate the length of time the customer rented the Bike
    #------------------------------------------------------------------------------------------------------------------------------
    def CalculateRentalPeriod(customer):
        if (customer.dtmRentalStart != False) and (0 < customer.intBikeCode < 4) and (customer.intTotalNumBikes > 0):
            # add the returned bikes to the appropriate inventory variable, record time of return, and calculate rental period
            if customer.intBikeCode == 1:
                BikeRental.intInventoryBikeType1 += customer.intTotalNumBikes
            if customer.intBikeCode == 2:
                BikeRental.intInventoryBikeType2 += customer.intTotalNumBikes
            if customer.intBikeCode == 3:
                BikeRental.intInventoryBikeType3 += customer.intTotalNumBikes

            #Record the time of the return
            now = datetime.datetime.now()

            #Calculate the amount of time between rent and return
            customer.dtmRentalPeriod = now - customer.dtmRentalStart

    #-----------------------------------------------------------------------------------------------------------------------------
    # Name: Calculate Base Amount Due
    # Desc: Allows bike shop to calculate the Base Amount due for Customer rental
    #------------------------------------------------------------------------------------------------------------------------------
    def CalculateBaseAmount(customer):
         #declare base total variable
        dblBaseAmountDue = 0.0

        # for testing purposes
        #self.dtmRentalPeriod = self.dtmRentalPeriod + datetime.timedelta(days=2)
            
        # set benchmarks for assigning correct rental basis
        dtmUnder5Hours = datetime.timedelta(0,0,0,0,0,5,0)
        dtmUnder5Days = datetime.timedelta(5,0,0,0,0,0,0)
           
        # assign rental basis (hourly, daily, weekly) according to total time period of rental - modifying hourly or daily basis according to whether customer reached certain limits
        # if customer rental period is less than 5 hours, assign to customer to rental basis hourly, otherwise shift to daily
        if customer.dtmRentalPeriod < dtmUnder5Hours:
            intRentalBasis = 1
        # if customer rental period is less than 5 days, assign customer to rental basis daily, otherwise shift to weekly
        elif customer.dtmRentalPeriod < dtmUnder5Days:
            intRentalBasis = 2
        else:
            intRentalBasis = 3

        # hourly bill calculation
        if intRentalBasis == 1:
            dblBaseAmountDue = round(customer.dtmRentalPeriod.seconds/3600,2) * 5 * customer.intTotalNumBikes
            customer.dblBaseAmountDue = dblBaseAmountDue
        
        # daily bill calculation
        elif intRentalBasis == 2:
            # if rental basis shifted from hourly to daily, it may be less than 1 official day, add 1 day to Rental Period for correct calculation
            if customer.dtmRentalPeriod.days < 1:
                customer.dtmRentalPeriod = customer.dtmRentalPeriod + datetime.timedelta(days=1)
            dblBaseAmountDue = customer.dtmRentalPeriod.days * 20 * customer.intTotalNumBikes
            customer.dblBaseAmountDue = dblBaseAmountDue
        
        # weekly bill calculation
        elif rentalBasis == 3:
            # if rental basis shifted from daily to weekly, it may be less than 1 week can and therefore a fraction when divided by 7 - modify to rental time period to at least 7 days if so 
            if customer.dtmRentalPeriod.days < 7:
                customer.dtmRentalPeriod = datetime.datetime(0,0,7,0,0,0,0)
            dblBaseAmountDue = round(customer.dtmRentalPeriod.weeks) * 60 * customer.intTotalNumBikes
            customer.dblBaseAmountDue = dblBaseAmountDue

        # catch if error with issuing return
        else:
            raise Exception('Necessary variables not set')
            return -1

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Calculate Discounts 
    # Desc: Calculates the amount of discount for customer based on their qualifications
    #----------------------------------------------------------------------------------------------------------------------------------
    def ApplyDiscounts(customer):
        dblAmountofDiscount = 0.0
        if 3 <= customer.intTotalNumBikes <= 5:
            dblAmountofDiscount = customer.dblBaseAmountDue * (BikeRental.dblFamilyDiscount)
        
        strCouponCheck = customer.strCouponCode[-3:]
        if strCouponCheck == "bbp":
            dblAmountofDiscount = customer.dblAmountofDiscount + (customer.dblBaseAmountDue * BikeRental.dblCouponDiscount)

        customer.dblAmountofDiscount = dblAmountofDiscount

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Calculate Final Bill 
    # Desc: Calculates the final bill of customer, with discounts applied
    #----------------------------------------------------------------------------------------------------------------------------------
    def CalculateFinalBill(customer):
        customer.dblTotalAmountDue = customer.dblBaseAmountDue - customer.dblAmountofDiscount

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Display Customer Invoice 
    # Desc: Allows shop to Display Customer Invoice
    #----------------------------------------------------------------------------------------------------------------------------------
    def DisplayInvoice(self):
        return self.strFname, self.strLname, self.intBikeCode, self.intTotalNumBikes, self.dtmRentalPeriod, self.dblBaseAmountDue, self.dblAmountofDiscount, self.dblTotalAmountDue 

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Collect Payment 
    # Desc: Allows the bikeshop to collect payment to add to total daily revenue
    #----------------------------------------------------------------------------------------------------------------------------------
    def CollectPayment(self):
        BikeRental.dblTotalRevenue += self.dblTotalAmountDue

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Display End of Day 
    # Desc: Allows Bikeshop to display End of Day totals
    #----------------------------------------------------------------------------------------------------------------------------------
    def DisplayEndofDay():
        return BikeRental.intTointTotalBikesRented, BikeRental.dblTotalRevenue

class Customer(BikeRental):
    #---------------------------------------------------------------------------------------------------------------
    # Name: Customer constructor
    # Desc: Constructor initializes and instantiates the Customer object
    #---------------------------------------------------------------------------------------------------------------
    def __init__(self, strFname = "", strLname = ""):

        self.strFname = strFname
        self.strLname = strLname
        self.strCouponCode = ""
        self.dtmRentalStart = datetime
        self.dtmRentalPeriod = 0
        self.intHours = 0
        self.intDays = 0
        self.intWeeks = 0
        self.intTotalNumBikes = 0
        self.intBikeCode = 0
        self.dblAmountofDiscount = float(0.0)
        self.dblBaseAmountDue = float(0.0)
        self.dblTotalDue = float(0.0)


    @property
    def strFname(self):
        return self.__strFname

    @property
    def strLname(self):
        return self.__strLname

    @strFname.setter
    def strFname(self, strFname):
        strTest = isinstance(strFname, str)
        if strFname == "":
            raise Exception('No value set for Customer first name variable')
        elif strTest == False:
            raise Exception('First name must be alphanumeric')
        else:
            self.__strFname = strFname

    @strLname.setter
    def strLname(self, strLname):
        strTest = isinstance(strLname, str)
        if strLname == "":
            raise Exception('No value set for Customer last name variable')
        if strTest == False:
            raise Exception('Last name must be alphanumeric')
        else:
            self.__strLname = strLname

    #@strCouponCode.setter
    #def strCouponCode(self, strCouponCode):
     #   strTest = isinstance(strCouponCode, str)
      #  if strCouponCode == "":
      #      raise Exception('No value set for Customer coupon code')
       # if strTest == False:
        #    raise Exception('Coupon must be alphanumeric')
        #else:
         #   self.__strCouponCode = strCouponCode
    
    #---------------------------------------------------------------------------------------------------------------
    # Name: Customer Request
    # Desc: Method takes in a request issued by the customer
    #---------------------------------------------------------------------------------------------------------------
    def RequestBike(self, intBikeCode, intBikeRentalAmount):

        # Checks to make sure the Bike Code provided meets all necessary Parameters 
        try:    
            intBikeCodeTest = int(intBikeCode)
            0 < intBikeCode < 4
        except:
            raise Exception ('Bike Code must be integer greater than 0 and less than 4')
            return -1
        
        try:
            intBikeRentalAmountTest = int(intBikeRentalAmount)
            intBikeRentalAmount > 0
        except ValueError:
            raise Exception ('Bike Rental Amount must be an integer greater than 0')
            return -1

        # if all bikes requests made by customer are valid, it set their instance variable to the desired value
        else:
            self.intTotalNumBikes = intBikeRentalAmount
            self.intBikeCode = intBikeCode





    


           


      

