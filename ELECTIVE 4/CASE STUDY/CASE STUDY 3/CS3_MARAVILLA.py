print ("==== ONLINE STORE ====")
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
product = " ".join(product.split()).title()
c_type = customer_t.upper()


#Calculate Product
subtotal = price * quantity

#Customer Category
match c_type:

    case "R":
        custom_type = "Regular Customer"
    case "S":
        custom_type = "Senior Citizen"
    case "M":
        custom_type = "Member"
    case "V":
        custom_type = "VIP Customer"
    case _:
        custom_type = "No user type"


#Customer Discount
if c_type == "S":
    disc = subtotal * 0.20
    disc_num = "20.00%"

elif c_type == "V":
    disc = subtotal * 0.15
    disc_num = "15.00%"

elif c_type == "M":
    disc = subtotal * 0.10
    disc_num = "10.00%"

elif c_type == "R":
    disc = subtotal * 0.05
    disc_num = "5.00%"

else:
    disc = 0
    disc_num = "0%"


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





