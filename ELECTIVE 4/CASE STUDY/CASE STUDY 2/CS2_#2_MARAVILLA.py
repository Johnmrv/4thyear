print("")
print("=== EMAIL PARSER & ANALYZER ===")
print("")

email = input("Enter your email address: ")

part = email.split("@")
uname = part[0]
domain = part[1]

print("")

print("Email:", email)
print("Username:", uname)
print("Domain:", domain)
print("Number of characters:", len(email))
print("Contains '@':", "@" in email)
