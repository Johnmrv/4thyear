age = 14

if age >= 18:
    print ("legal age")
elif age <18:
    print ("Minor")


grade = 90

if grade >= 95:
    print("Remarks: A")
elif grade >= 85:
    print("Remarks: A")
elif grade >= 75:
    print("Remarks: A")
elif grade >= 65:
    print("Remarks: A")
elif grade >= 55:
    print("Remarks: A")
else:
    print ("Invalid")

grades = 75

if grades >= 95: print("Remarks: A")

print("Remarks A") if grades >=75 else print ("Fail")

number = 95

if number % 3 == 0 and number > 0:
    print ("The number is positive and divisible by 3")

"""
This acts as a multi-line comment block.
Python ignores it as long as it isn't
assigned to a variable.
"""

#Pipe character
day = 7

match day:
    case 1 | 2 | 3 | 4 | 5 :
        print ("Monday")
    case 6 | 7:
        print ("Tuesday")
    case _:
        print ("Invalid day")

num = 7

match num:
    case x if x % 2 == 0:
        print ("Monday")
    case x if x % 3 == 0:
        print ("Monday")
    case x if x % 5 == 0:
        print ("Monday")
    case _:
        print ("Invalid day")







