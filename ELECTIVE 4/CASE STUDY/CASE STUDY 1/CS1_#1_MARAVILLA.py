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
