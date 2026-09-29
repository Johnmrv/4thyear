while True:
    print()
    print()
    print("==== System Menu ====")
    print()
    print("[1] Employee ID Generator")
    print("[2] Product Code Analyzer")
    print("[3] Student Scholarship Evaluation")
    print("[4] Electricity Billing System")
    print("[5] Online Food Ordering System")
    print("[6] ATM Transaction")
    print("[7] Password and Username Validator")
    print("[8] Hotel Reservation and Billing System")
    print("[9] Exit")
    print()

    choice = input("Enter a Number: ")

    match choice:

        case "1":
            print("==== Employee ID Generator ====")
            print()
            fname = str(input("Enter Employee Firstname: "))
            lname = str(input("Enter Employee Lastname: "))
            code = str(input("Enter Department Code: "))
            e_num = str(input("Enter Employee Number: "))
            print()
            fullname = fname + " " + lname
            fullname = " ".join(fullname.split()).title()
            code = code.upper()
            e_num = e_num.strip().replace(" ","")
            username = fname.strip()[:3].lower() + "_" + lname.strip()[:3].lower()

            match code:

                case "IT":
                    dept = "Information Technology"
                case "HR":
                    dept = "Human Resources"
                case "ACCT":
                    dept = "Accounting"
                case "MKT":
                    dept = "Marketing"
                case _:
                    dept = "Unkown Department"

            print("==== EMPLOYEE INFORMATION ====")
            print()
            print(f"Employee Name   : {fullname}")
            print(f"Employee Number : {e_num}")
            print(f"Username        : {username}")
            print(f"Department Code : {code}")
            print(f"Department      : {dept}")
            print()
            print("==============================")

        case "2":
            print()
            print("==== Product Code Analyzer ====")
            print()
            p_name = str(input("Enter Product Name: "))
            p_code = input("Enter Product Code: ")
            p_price = float(input("Enter Product Price: "))

            #String Processing
            p_name = " ".join(p_name.split()).title()
            p_code = p_code.strip().replace(" ", "").upper()

            #String Code Analysis
            f_code = p_code[:4]
            l_code = p_code[-4:]
            n_char = len(p_code)
            u_char = p_code.count("-")


            print("==== PRODUCT INFORMATION ====")
            print()
            print(f"Product          : {p_name}")
            print(f"Product Code     : {p_code}")
            print(f"First 4          : {f_code}")
            print(f"Last 4           : {l_code}")
            print(f"Code Length      : {n_char}")
            print(f"Dash Count       : {u_char}")
            print(f"Contains 2026    : {("2026" in p_code)}")
            print(f"Price            : ₱{p_price:,.2f}")
            
            
        case "3":
            print()
            print("==== Student Scholarsip Evaluation ====")
            print()
            s_name = input("Enter Student Fullname: ")
            s_id = input("Enter Student ID: ")
            s_course = input("Enter Student Course Code: ")
            s_pg = float(input("Enter Student Preliminary Grade: "))
            s_mg = float(input("Enter Student Midterm Grade: "))
            s_fg = float(input("Enter Student Final Grade: "))
            s_income = float(input("Enter Monthly Family Income: "))
            print()

            #String Processing
            s_name = " ".join(s_name.split()).title()
            s_id = s_id.replace(" ", "")
            s_course = s_course.upper()

            #Grade Calculation
            average = (s_pg + s_mg + s_fg) / 3

            if s_pg and s_mg and s_fg == 0:
                print ("Error: Grades must be between 0 and 100.")
                break

            if average >= 90 and average <=100:
                result = "Outstanding"
            elif average >= 85 and average <= 89.99:
                result = "Very Good"
            elif average >= 80 and average <= 84.99:
                result = "Good"
            elif average >= 75 and average <=79.99:
                result = "Satisfactory"
            elif average > 75:
                result = "Failed"

            #Scholarship Evaluation
            if average >=90 and s_income <= 25000:
                verdict = "Full Scholarship"
            elif average >=85 and s_income <= 40000:
                verdict = "Partial Scholarship"
            else:
                verdict = "Not Qualified"

            match s_course:

                case "BSIT":
                    course = "Bachelor of Science in Information Technology"
                case "BSCS":
                    course = "Bachelor of Science in Computer Science"
                case "BSIS":
                    course = "Bachelor of Science in Information Systems"
            print()
            print("==== SCHOLARSHIP EVALUATION ====")
            print()
            print(f"Student         : {s_name}")
            print(f"Student ID      : {s_id}")
            print(f"Course          : {course}")
            print(f"Average         : {average:.2f}")
            print(f"Performance     : {result}")
            print(f"Family Income   : ₱{s_income:,.2f}")
            print(f"Scholarship     : {verdict}")
            print("================================")
            print()
                
            

        case "4":
            print()
            print("==== Electricity Billing System ====")
            print()
            c_name = input("Enter Customer's Name: ")
            c_type = input("Enter Customer's Type: ")
            c_prev = float(input("Enter Previous Meter Reading: "))
            c_curr = float(input("Enter Current Meter Reading: "))
            c_rate = float(input("Rate per kWh: "))

            #String Processing
            c_name = " ".join(c_name.split()).title()
            c_type = c_type.upper()

            #Consumption
            consumption = c_curr - c_prev

            if c_curr < c_prev:
                print("Error: Current meter reading cannot be lower than previous reading.")
                break

            #Base Bill
            b_bill = consumption * c_rate

            #Consumption Classification
            if consumption >= 0 and consumption <= 100:
                classification = "Low Consumption"
            elif consumption >= 101 and consumption <= 300:
                classification = "Normal Consumption"
            elif consumption >= 301 and consumption <= 500:
                classification = "High Consumption"
            elif consumption > 500:
                classification = "Very High Consumption"

            match c_type:

                case "R":
                    cur_t = "Residential"
                    charge = 0
                case "C":
                    cur_t = "Commercial"
                    charge = 0.10
                case "I":
                    cur_t = "Industrial"
                    charge = 0.15
                case _:
                    print("Invalid Choice!")
                    cur_t = "Unkown Type"
                    charge = 0

            #Additional Charge
            add_charge = b_bill * charge
            total = b_bill + add_charge

            print()
            print("==== ELECTRIC BILL ====")
            print()
            print(f"Customer        : {c_name}")
            print(f"Customer Type   : {c_type}")
            print(f"Consumption     : {consumption}")
            print(f"Classification  : {classification}")
            print(f"Rate            : ₱{c_rate:,.2f}")
            print(f"Base Bill       : ₱{b_bill:,.2f}")
            print(f"Additioal Fee   : ₱{add_charge:,.2f}")
            print(f"Total Bill      : ₱{total:,.2f}")
            print()
            print("======================================")
                    
        
            
        case "5":
            print()
            print("==== Online Food Ordering System ====")
            print()
            fname = input("Customer First Name: ")
            lname = input("Customer Last Name: ")
            food = input("Food Item: ")
            c_code = input("Category Code: ")
            price = float(input("Enter Price: "))
            quantity = float(input("Enter Quantity: "))
            m_type = input("Membership Type: ")
            discount = 0

            #String Processing
            fullname  = fname + " " + lname
            fullname = " ".join(fullname.split()).title()
            food = " ".join(food.split()).title()
            c_code = c_code.upper()
            m_type = m_type.strip().upper()

            #Subtotal
            subtotal = price * quantity

            #Category Description
            match c_code:

                case "M":
                    cat = "Meal"
                case "D":
                    cat = "Drink"
                case "S":
                    cat = "Snack"
                case "DS":
                    cat = "Dessert"
                case _:
                    cat = "No Category!"

            #Membership Discount
            if m_type == "VIP":
                discount = 0.20
            elif m_type == "Student":
                discount = 0.15
            elif m_type == "Member":
                discount = 0.10
            elif m_type == "Regular":
                discount = 0

            #Bulk Discount
            if quantity >=10:
                add_disc = 0.05

            #Calculation
            mem_disc = subtotal * discount
            bulk_disc = subtotal * add_disc
            t_disc = mem_disc + bulk_disc
            t_amount = subtotal - t_disc

            print()
            print("==== OREDER SUMMARY ====")
            print()
            print(f"Customer Name           : {fullname}")
            print(f"Food Item               : {food}")
            print(f"Category                : {cat}")
            print(f"Price                   : ₱{price:,.2f}")
            print(f"Quantity                : {quantity:.0f}")
            print(f"Membership Type         : {m_type}")
            print(f"Membership Discount     : ₱{mem_disc:,.2f}")
            print(f"Bulk Discount           : ₱{bulk_disc:,.2f}")
            print(f"Total Discount          : ₱{t_disc:,.2f}")
            print(f"Total Amount            : ₱{t_amount:,.2f}")
            print("==============================================")
            
            
            
                
                    

        case "6":
            print()
            print("==== ATM Transaction System ====")
            print()
            fullname = input("Enter Fullname: ")
            a_num = input("Enter Account Number: ")
            a_type = input("Enter Account Type: ")
            c_bal = float(input("Enter Current Balance: "))
            t_type = input("Enter Transaction Type: ")
            t_amo = float(input("Enter Transaction Amount: "))
            new_bal = 0
            

            #String Processing
            fullname = " ".join(fullname.split()).title()
            a_num = a_num.replace(" ","")
            a_num = a_num.replace("-","")
            a_type = a_type.strip().upper()
            t_type = t_type.strip().upper()

            match a_type:
                
                case "S":
                    account_type = "Savings"
                case "C":
                    account_type = "Checking"
                case "B":
                    account_type = "Business"

            match t_type:

                case "W":
                    transaction_type = "Withdrawal"
                    #Withdrawal Rules
                    if t_amo <= 0 or t_amo > c_bal:
                        print("Transaction Failed: Unable to process withdrawal.")
                        break
                    else:
                        new_bal = c_bal - t_amo
                case "D":
                    transaction_type = "Deposit"
                    #Deposit Rules
                    if t_amo <= 0:
                        print("Transaction Failed: Unable to process Deposit.")
                    else:
                        new_bal = c_bal + t_amo

            if c_bal >= 100000:
                status = "Premium Balance"
            if c_bal >= 50000 and c_bal <= 99999.99:
                status = "High Balance"
            if c_bal >= 10000 and c_bal <= 49999.99 :
                status = "Normal Balance"
            if c_bal < 10000:
                status = "Low Balance"

            print()
            print("==== ATM RECEIPT ====")
            print()
            print(f"Account Holder      : {fullname} ")
            print(f"Account Number      : {a_num}")
            print(f"Account Type        : {account_type}")
            print(f"Transaction         : {transaction_type}")
            print(f"Old Balance         : ₱{c_bal:,.2f}")
            print(f"Amount              : ₱{t_amo:,.2f}")
            print(f"New Balance         : ₱{new_bal:,.2f}")
            print(f"Balance Status      : {status}")
            print()
            print("================================")
                        

            

            


            
            
            
            


        case "7":
            print()
            print("==== Password and Username Validator ====")
            print()
            fullname = input("Enter Full Name: ")
            username = input("Enter Desired Username: ")
            password = input("Enter Desired Password: ")

            #String Processing
            fullname = " ".join(fullname.split()).title()
            username = username.strip().lower()
            #Username Requirements
            if len(username) >= 6 and username.isalnum():
                print ("Valid Username!")
            else:
                print("Invalid Username!")
            #Password Requirements
            if len(password) >= 8 and password.isalnum() == True:
                print(f"Fullname                    : {fullname}")
                print(f"Username                    : {username}")
                print(f"Password Length             : {len(password)}")
                print(f"Number of time 'a' appears  : {password.count('a')}")
                print(f"Wether @ exist              : {'@' in password}")
                print(f"First Character             : {password[:1]}")
                print(f"Last Character              : {password[-1:]}")
                
            else:
                print("Invalid Password!")  
                    


            
        case "8":
            print()
            print("==== Hotel Reservation And Billing System ====")
            print()
            fullname = input("Enter Fullname: ")
            reservation_id = input("Enter Reservation ID: ")
            room_code = input("Enter Room Code: ")
            number_nights = int(input("Enter Number of Nights: "))
            price_night = int(input("Enter Price per Night: "))
            guest_type = input("Enter Guest Type: ")
            amount_paid = float(input("Enter Amount Paid: "))

            #String Processing
            fullname = " ".join(fullname.split()).title()
            reservation_id = reservation_id.strip()
            room_code = room_code.strip().upper()
            guest_type = guest_type.strip().upper()

            #Room Description
            match "room_code":

                case "S":
                    room_desc = "Standard Room"
                case "D":
                    room_desc = "Deluxe Room"
                case "E":
                    room_desc = "Executive Room"
                case "P":
                    room_desc = "Presidential Room"

            #Accommodation Cost
            if number_nights <= 0 and price_night <= 0:
                print("No Negative numbers!")
            subtotal = number_nights * price_night

            #Discount
            if guest_type == "R":
                guest_type = "Regular Guest"
                discount = 0
            elif guest_type == "M":
                guest_type = "Member Guest"
                discount = 0.10
            elif guest_type == "S":
                guest_type = "Senior Citizen"
                discount = 0.20
            elif guest_type == "V":
                guest_type = "VIP Guest"
                discount = 0.15

            if number_nights >= 7:
                discount_add = 0.05
            else:
                discount_add = 0.0

            t_discount = discount + discount_add
            g_discount = subtotal * discount
            s_discount = subtotal * discount_add
            t_due = subtotal - t_discount
            change = amount_paid - t_due

            print()
            print("==== HOTEL RECEIPT ====")
            print()
            print(f"Fullname            : {fullname}")
            print(f"Reservation ID      : {reservation_id}")
            print(f"Room Code           : {room_code}")
            print(f"Number of Nights    : {number_nights}")
            print(f"Price per night     : {price_night}")
            print(f"Guest Type          : {guest_type}")
            print(f"Amount Paid         : ₱{amount_paid:,.2f}")
            print(f"Guest Discount      : ₱{g_discount:,.2f}")
            print(f"Stay Discount       : ₱{s_discount:,.2f}")
            print(f"Total Discount      : ₱{t_discount:,.2f}")
            print(f"Total Due           : ₱{t_due:,.2f}")
            print(f"Change              : ₱{change:,.2f}")
            
        case "9":
            print("Goodbye")
            break
            
        case _:
            
            print("Invalid")
        
    
