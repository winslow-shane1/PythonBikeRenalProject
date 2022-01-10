from BusinessLogic import BikeRental, Customer
import datetime

shop = BikeRental(35)
#BadCheck shop = BikeRental(5)
shop.TypeInventory(10, 15, 10)

customer1 = Customer('Shane', 'Winslow')

#Function to view all Inventory
request = shop.DisplayAllInventory()
print(request)
intTotal, intType1, intType2, intType3 = request
print("There are a total of {} bike(s), {} Mountain Bike(s), {} Road Bike(s), and {} Touring Bike(s)".format(intTotal, intType1, intType2, intType3))

#Function to view specific bike type
BikeRental.BikeCode(1)
BikeRental.SetBikeName(1)
request = shop.DisplayBikeTypeInventory()
strBikeName, intInventoryBikeType = request
print("There are {} {} Bike(s) avaiable in our inventory".format(strBikeName, intInventoryBikeType))

#Function to Request Bikes 
customer1.RequestBike(1,4)
print(customer1.intTotalNumBikes, customer1.intBikeCode)

#Function for Customer to Rent Bike
customer1.dtmRentalStart = customer1.RentBike()
print(customer1.dtmRentalStart)
print(shop.intInventoryBikeType1)

#Function for Customer to Return Bike
customer1.dtmRentalStart = datetime.datetime.now() - datetime.timedelta(days=3)
customer1.CalculateRentalPeriod()
shop.CalculateBaseAmount(customer1)

#Function to Apply Discounts
shop.ApplyDiscounts(customer1)

#Calculate Final Bill
customer1.CalculateFinalBill()

#Print Invoice
request = customer1.DisplayInvoice()
print(request)
strFname, strLname, intBikeCode, intTotalNumBikes, dtmRentalPeriod, dblBaseAmountDue, dblAmountofDiscount, dblTotalAmountDue = request
print("""----Customer Invoice----
Customer First Name:   {}
Customer Last Name:    {}
Bike Type Rented:      {}
Total Bikes Rented:    {}
Total Rental Period:   {}
Original Amount Due:   {}
Amount of Discount:    {}
Final Amount Due:      {}""".format(strFname, strLname, intBikeCode, intTotalNumBikes, dtmRentalPeriod, dblBaseAmountDue, dblAmountofDiscount, dblTotalAmountDue))
















