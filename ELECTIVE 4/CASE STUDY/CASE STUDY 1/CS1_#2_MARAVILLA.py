print("")
print("=== ELECTRICITY BILL ===")
print("")

name = str(input("Enter customer name: "))
pkWh = float(input("Enter previous meter kWh consumed: "))
kWh = float(input("Enter current meter kWh Consumed: "))
rate = float(input("Enter rate per kWh: "))

consumed = kWh - pkWh 
bill = consumed * rate
            

print("Hello,", name , "your electricity consumed is" , consumed , ". And you bill is ₱", bill)

