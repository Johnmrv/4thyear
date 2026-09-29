print()
print("====== STUDENT GRADE CALCULATOR ======")
print()
print()

names = ""
grades = ""
remarks = ""
final_grades = ""
count = 0
average = 0
highest = 0
lowest = 0
failed = 0
passed = 0
total = 0
stop = True

while stop:

    stud_num = input("Enter how many students will be processed: ")

    if stud_num.isdigit() and int(stud_num) > 0:
        stud_num = int(stud_num)

        for i in range(stud_num):

            print("\n\n")
            print("===== Enter Student Info =====\n\n")

            #Firstname
            while True:
                fname = " ".join(input("Enter student's first name: ").strip().split()).title()

                if fname.replace(" ", "").isalpha():
                    print()
                    break

                print("Please only enter alphabet characters")
                print()

            #Lastname
            while True:
                lname = " ".join(input("Enter student's last name: ").strip().split()).title()

                if lname.replace(" ", "").isalpha():
                    fullname = fname + " " + lname + "|"
                    names = names + fullname
                    print()
                    break

                print("Please only enter alphabet characters")
                print()

            #Prelim
            while True:
                prelim = input("Enter Prelim Grade: ")
                if prelim.replace(".", "", 1).isdigit():
                    prelim = float(prelim)
                    if prelim < 0 or prelim > 100:
                        print("Please don't enter grade that is less than 0 or greater than 100")
                    else:
                        print()
                        grades = grades + str(prelim) + ","
                        break

                else:
                    print("Please only enter valid number characters")
                    print()

            #Midterm
            while True:
                midterm = input("Enter Midterm Grade: ")
                if midterm.replace(".", "", 1).isdigit():
                    midterm = float(midterm)
                    if midterm < 0 or midterm > 100:
                        print("Please don't enter grade that is less than 0 or greater than 100")
                    else:
                        print()
                        grades = grades + str(midterm) + ","
                        break

                else:
                    print("Please only enter valid number characters")
                    print()

            #Finals
            while True:
                finals = input("Enter Finals Grade: ")
                if finals.replace(".", "", 1).isdigit():
                    finals = float(finals)
                    if finals < 0 or finals > 100:
                        print("Please don't enter grade that is less than 0 or greater than 100")
                    else:
                        print()
                        grades = grades + str(finals) + "|"


                        final_grade = (prelim *0.30) + (midterm * 0.30) + (finals * 0.40)


                        if final_grade >= 90:
                            remark = "Excellent"

                        elif final_grade >= 85:
                            remark = "Very Good"

                        elif final_grade >= 80:
                            remark = "Good"

                        elif final_grade >= 75:
                            remark = "Passed"

                        else:
                            remark = "Failed"

                        remarks = remarks + remark + "|"
                        final_grades = final_grades + str(final_grade) + "|"

                        break

                else:
                    print("Please only enter valid number characters")
                    print()

            print("========================================")
            print("          STUDENT GRADE REPORT")
            print("========================================")
            print(f"Name        : {names.split('|')[i]}")
            splitter = grades.split("|")[i]
            print(f"Prelim      : {float(splitter.split(',')[0]):.2f}")
            print(f"Midterm     : {float(splitter.split(',')[1]):.2f}")
            print(f"Final Exam  : {float(splitter.split(',')[2]):.2f}")
            print(f"Final Grade : {float(final_grades.split('|')[i]):.2f}")
            print(f"Remark      : {remarks.split('|')[i]}")
            print("========================================")

            splits = float(final_grades.split("|")[i])

            total += splits

            if i == 0:
                highest = splits
                lowest = splits
            else:
                if splits > highest:
                    highest = splits

                if splits < lowest:
                    lowest = splits

        stop = False

    else:
        print("Please enter a valid number of students")
        print()


average = total / stud_num
failed = remarks.count("Failed")
passed = stud_num - failed

print("\n\n")
print("========================================")
print("             CLASS SUMMARY")
print("========================================")
print(f"Number of Students : {stud_num}")
print(f"Class Average      : {average:.2f}")
print(f"Highest Grade      : {highest:.2f}")
print(f"Lowest Grade       : {lowest:.2f}")
print(f"Passed             : {passed}")
print(f"Failed             : {failed}")
print("========================================")














