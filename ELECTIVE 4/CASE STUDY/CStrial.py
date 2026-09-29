while True:

    print("")
    print("=== MAIN MENU ===")
    print("[1] STUDENT FINAL GRADE")
    print("[2] ELECTRICITY BILL")
    print("[3] SECONDS CONVERTION")
    print("[4] NUMBER OF MONEY NOTES")
    print("[5] EXIT")
    print("")

    choice = str(input("Enter a choice: "))
    
    match choice:

        case "1":
            print("")
            print("=== STUDENT FINAL GRADE ===")
            print("")
            
            name = str(input("Enter student name: "))

            print("")
            print("Exam Scores")
            p = int(input("Enter prelimenary score: "))
            m = int(input("Enter midterm score: "))
            f = int(input("Enter finals score: "))

            p1 = p * 0.3
            m1 = m * 0.3
            f1 = f * 0.4

            total = p1 + m1 + f1
            

            print("")
            print("The weighted final grade of ", name , "is", total)

        case "2":
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

            print("")
        case "3":
            print("")
            print("=== SECONDS CONVERTER ===")
            print("")

            sec = int(input("Enter seconds: "))
            days = sec // 86400
            hours = (sec % 86400) // 3600
            minutes = (sec % 3600) // 60
            rsec = sec % 60

            print("")
            print("Days:", days)
            print("Hours:", hours)
            print("Minutes:", minutes)
            print("Remaining seconds:", rsec)

        case "4":
            print("")
            print("=== PESO NOTE COUNTER ===")
            print("")

            amount = int(input("Enter amount in pesos: "))

            p1000 = amount // 1000
            amount = amount % 1000

            p500 = amount // 500
            amount = amount % 500

            p200 = amount // 200
            amount = amount % 200

            p100 = amount // 100
            amount = amount % 100

            p50 = amount // 50
            amount = amount % 50

            p20 = amount // 20
            amount = amount % 20

            p10 = amount // 10
            amount = amount % 10

            p5 = amount // 5
            amount = amount % 5

            p1 = amount

            print("")
            print("1000 pesos -", p1000)
            print("500 pesos  -", p500)
            print("200 pesos  -", p200)
            print("100 pesos  -", p100)
            print("50 pesos   -", p50)
            print("20 pesos   -", p20)
            print("10 pesos   -", p10)
            print("5 pesos    -", p5)
            print("1 peso     -", p1)


            
            

        case _:
            print("")
            print("INVALID CHOICE!")
            
            
