print ("==== ONLINE STORE ACTIVITY====")
print()
print()
print("CUSTOMER DETAILS")
print()
print()
f_name = str(input("Enter first name: "))
l_name = str(input("Enter last name: "))
product = str(input("Enter product name: "))
price = float(input("Enter price: "))
quantity = float(input("Enter quantity: "))
customer_t = str(input("Enter customer type: "))

#String Method
fname = f_name + " " + l_name
fullname = " ".join(fname.split()).title()
c_type = customer_t.upper()


#Calculate Product
subtotal = price * quantity

#Customer Category & Discount
match c_type:

    case "R":
        disc = subtotal * 0.05
        custom_type = "Regular Customer"
        disc_num = "5.00%"
    case "S":
        disc = subtotal * 0.20
        custom_type = "Senior Citizen Customer"
        disc_num = "20.00%"
    case "M":
        disc = subtotal * 0.10
        custom_type = "Member Customer"
        disc_num = "10.00%"
    case "V":
        disc = subtotal * 0.15
        custom_type = "VIP Customer"
        disc_num = "15.00%"
    case _:
        custom_type = "No user type"
        disc_num = "0%"
        disc = 0
        

d_total = subtotal - disc
cu_type = custom_type

print()
print()
print("========= ORDER SUMMARY =========")
print()
print()
print(f"Customer        : {fullname}")
print(f"Product         : {product}")
print(f"Customer Type   : {cu_type}")
print(f"Quantity        : {quantity:.0f}")
print(f"Price           : ₱{price:,.2f}")
print(f"Subtotal        : ₱{subtotal:,.2f}")
print(f"Discount        : {disc_num}")
print(f"Discount Amount : ₱{disc:,.2f}")
print(f"Total Amount    : ₱{d_total:,.2f}")
print()
print()
print("=================================")









