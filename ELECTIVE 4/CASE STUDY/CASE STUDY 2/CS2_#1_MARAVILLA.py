print("")
print("=== NAME & USERNAME ===")
print("")

fname = str(input("Enter your first name: "))
lname = str(input("Enter your last name: "))

fullname = fname + " " + lname

print("")
print("Full name:", fullname)
print("Uppercase:", fullname.upper())
print("Lowercase:", fullname.lower())
print("First character:", fname[0])
print("First three letters of last name:", lname[:3])
print("Suggested username:", fname[:3].lower() + "_" + lname[:3].lower())
