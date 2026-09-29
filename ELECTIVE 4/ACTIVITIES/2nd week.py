while True:
    print("")
    print("=== MENU ===")
    print("[1] Convert Preset String")
    print("[2] Enter and Display Name")
    print("[3] Strip")
    print("[4] Find")
    print("[5] Replace")
    print("[6] Count")
    print("[7] Count")
    print("[8] Checking Strings")
    print("[9] String Lenght")
    print("[Bye] Exit")
    print("")
    choice = str(input("Enter a choice: "))
    print("")

    match choice:
        case "1":
            print("")
            low = "GOoD mOrninG pO."

            print(low.capitalize())
            print(low.casefold())
            print(low.swapcase())
            print(low.title())
            print()
            print("")

        case "2":
            print("")
            name = str(input("Enter your name: ")).title()
            print("Hello,", name.casefold() + "!")
            print("")

        case "3":
            print("")
            name = input("Enter your name: ")
            print(name.strip())
            print(name.lstrip())
            print(name.rstrip())
            print("")
            
        case "4":
            print("")
            text = str(input("ENter text: "))
            findd = str(input("Enter letter to find: "))

            print(text.find(findd))
            print(text.rfind(findd))
            print("")

        case "5":
            print("")

            text = str(input("ENter text: "))
            tor = str(input("Enter a word/letter to replace: "))
            rep = str(input("Enter a replacement word/letter: "))

            replaced = text.replace(tor, rep).title()

            print(replaced)

        case "6":
            print("")

            text = str(input("Enter text: "))
            count = str(input("Enter a word/letter to count: "))


            counted = text.count(count)

            print(counted)

            print(f"Number of" , count , "is", {text.count(count, 3, 9)})

        case "7":
            print("")

            text = input("Enter text: ")
            output = text.title().split(", ", 1)
            counter = output.count("John")
            finder = text.casefold().find("o")

            print("Words:", output)
            print("Occurrences of 'John':", counter)
            print("First index of 'o' in text:", finder)

            
        case "Activity":
            fname = input("Enter your first name: ").strip()
            lname = input("Enter your last name: ").strip()

            full = (f"{fname} {lname}" )
            
            print(f"Hello, {full}!")

            
            print(f"First character: {full[0]}")
            print(f"Last character: {full[-1]}")

            
            nname = fname[:3]
            print(f"Your nickname: {nname}")

            
            counter = full.casefold().count("a")
            print(f"Number of times 'a' appears in your full name: {counter}")

        case "8":
            
            print("")
            text = input("Enter text: ")
            print (text.isalnum())
            print (text.isalpha())
            if text.isnumeric(): print(text)
            else: print("error")
            
            print (text.isnumeric())
            print (text.isspace())

        case "9":
            
            print("")
            text = input("Enter text: ")
            lenght = len(text)
            print (lenght)

            passk = "password123"
            print (passk[0])
            print (passk[-len(passk)])
    
        case "Bye":
            print("")
            print("Goodbye!")
            print("")
            break

        case _:
            print("INVALID CHOICE\n")
