while True:
    print("")
    print("==== MENU ====")
    print(" [1] Area of the rectangle")
    print(" [2] Area of the circle")
    print(" [3] Average of five numbers")
    print(" [4] Exit")
    print("")

    choice = str(input ("Enter your choice: "))

    match choice:

        case "1":
            print("")
            print("==== CALCULATE THE AREA OF RECTANGLE ====")
            print("")

            l = int(input("Enter the length: "))
            w = int(input("Enter the width: "))

            area = l * w

            print("")
            print("The area of rectangle is ", area)
            print("")
            
        case "2":
            print("")
            print("==== CALCULATE THE AREA OF CIRCLE ====")
            print("")

            pi = 3.14
            r = int(input("Enter the radius: "))

            area = ((pi) * (r * r))

            print("")
            print("The area of circle is ", area)
            print("")

        case "3":
            print("")
            print("==== AVERAGE OF FIVE NUMBERS ===")
            print("")

            n1 = int(input("Enter number 1: "))
            n2 = int(input("Enter number 2: "))
            n3 = int(input("Enter number 3: "))
            n4 = int(input("Enter number 4: "))
            n5 = int(input("Enter number 5: "))

            total = n1 + n2 + n3 + n4 + n5
            average = total / 5

            print("")
            print("The average of", total, "is" , average)
            print("")

        case "4":
            print("")
            print("Program ended")
            break

        case _:
            print("")
            print("Invalid Choice!")
             
            
            

            


    
