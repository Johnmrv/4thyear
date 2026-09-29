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
