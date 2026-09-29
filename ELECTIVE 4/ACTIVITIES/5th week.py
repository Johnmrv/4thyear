print()
print()
print("=== LAB ACTIVITY ===")
print()
print("Enter Details")
print()

stud_n = input("Enter Student's Full name: ")
stud_id = input("Enter Student's ID: ")
course = input("Enter Student's course: ")
stud_pg = float(input("Enter Preliminary Grade: "))
stud_mg = float(input("Enter Midterm Grade: "))
stud_fg = float(input("Enter Finals Grade: "))
units = int(input("Enter Number of Units: "))
stud_tf = float(input("Enter Tuition Fee per Unit: "))

#1. String Processing
stud_name = " ".join(stud_n.split()).title()
ids = stud_id.replace(" ", "")
stud_course = course.strip().upper()

#2. Grade Calculation
if stud_pg < 0 or stud_pg > 100:
    print("\nError: Preliminary Grade must be between 0 and 100")

elif stud_mg < 0 or stud_mg > 100:
    print("\nError: Midterm Grade must be between 0 and 100")

elif stud_fg < 0 or stud_fg > 100:
    print("\nError: Final Grade must be between 0 and 100")

elif units < 0:
    print("\nError: Number of Units cannot be negative")

else:

    avr = (stud_pg + stud_mg + stud_fg) / 3

#3. Academic Evaluation

if avr >= 90:
    performance = "Excellent"
elif avr >= 85:
    performance = "Very Good"
elif avr >= 80:
    performance = "Good"
elif avr >= 75:
    performance = "Passed"
else:
    performance = "Failed"

if avr >= 75:
    status = "PASSED"
else:
    status = "FAILED"

#4. Course Description

match stud_course:

    case "BSIT":
        course_n = "Bachelor of Science in Information Technology"

    case "BSCS":
        course_n = "Bachelor of Science in Computer Science"

    case "BSIS":
        course_n = "Bachelor of Science in Information Systems"

    case _:
        course_n = "Invalid Course Code"

#5. Tuition Fee Calculation

tuition_fee = units * stud_tf

#Student Full Info

print()
print()
print("=== STUDENT FULL INFO ===")
print()
print()

print(f"Student Name: {stud_name}")
print(f"Student ID: {ids}")
print(f"Course Code: {stud_course}")
print(f"Course Description: {course_n}")
print(f"Preliminary Grade: {stud_pg:.2f}")
print(f"Midterm Grade: {stud_mg:.2f}")
print(f"Final Grade: {stud_fg:.2f}")
print(f"Average Grade: {avr:.2f}")
print(f"Performance: {performance}")
print(f"Status: {status}")
print(f"Number of Units: {units}")
print(f"Tuition Fee per Unit: ₱{stud_tf:,.2f}")
print(f"Total Tuition Fee: ₱{tuition_fee:,.2f}")









