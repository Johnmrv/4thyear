
##All variables are placeholders, change them appropriately 

##number 1
##There's only THREE course, ask user three times then typing "next" breaks to the next input 

stud_c_1 = input("Your first cource: ")
stud_c_2 = input("Your second cource (type 'next' if none): ")
stud_c_3 = input("Your first cource (type 'next' if none): ")

##number 4
##there's only THREE course

match stud_c:
    case BSIT:
        stud_c_conv = "Bachelor of Science in Information Technology"
    case BSCS:
        stud_c_conv = "Bachelor of Science in Computer Science"
    case BSIS:
        stud_c_conv = "Bachelor of Science in Information Systems"
    case _:
        print("You entered something wrong")

##num5

total_tui = stud_unit * stud_tui_fee

print(f" Total Tuition: {total_tui:,.2f}")


##check instruction, double check if needed
##Idk if you will display everything after, maybe its like that, or by line. You decide 
