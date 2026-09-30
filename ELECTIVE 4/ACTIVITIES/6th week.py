course = "Python Programming"

for char in course:
    print (char, end="")

    
print("========================")

fruits = ["apple", "banana", "cherry"]
print(fruits)
print("========================")

for fruit in fruits:
    print (fruit, end = " ")
    
print()
print("========================")

# for (i = 0; i < 5; i++)

for i in range(0, 5, 1):
    print(i)
print()
for i in range(5, 0, -1):
    print(i)
print()
for i in range(0, 5, 2):
    print(i)

print()
print("========================")
print("Learning Task")
print("========================")
print("Prob 1")

for i in range(1, 26, 2):
    print(i, end=" ")

print()
print("========================")
print("Using if statement")


#rangeOfValue = input("Enter range value: ")
if rangeOfValue.isnumeric():
   rangeOfValue = int(rangeOfValue)
   for i in range(rangeOfValue + 1):
       if i % 2 == 0 and i !=0 :
           print(i, end=" ")

print()
print("========================")
print("Learning Task")
print("========================")
print("Prob 2")
print()

for i in range(1, 11):
   print(i * 5)

print()
print("========================")
print("Learning Task")
print("========================")
print("Prob 3")
print()

inputs = int(input("Enter total number of inputs: "))

count = 0
summ = 0

for _ in range(inputs):
   val = int(input("Enter an integer: "))

   if val <= 0:
       break

   summ += val
   count += 1

if count > 0:
   avr = summ / count
   print(f"\n Sum: {summ}")
   print(f"\n Count: {count}")
   print(f"\n Average: {avr}")
else:
   print("\nNo valid inputs were entered.")



print()
print("========================")
print("While Loop")
print("========================")
print()

##number = 1
##while number <=5:
##    print(number, end = " ")
##    number += 1
##
##print()
##
##numbers = input("Enter 5 numbers: ")
##numbers = numbers.split(" ")
##count = total = 0
##for num in numbers:
##    if num.isnumeric():
##        total += int(num)
##        count += 1
##print(f"\n Sum: {total}")
##print(f"\n Average: {total/count}")
##
##isTrue = True
##while isTrue:
##    num = input("Enter a number between 1 to 10: ")
##    if num.isnumeric():
##        num  = int(num)
##        if num > 1 and num <= 10:
##            print("Valid number")
##            isTrue = False
##        else:
##            print("Invalid Number")
##    else:
##        print("Letters not allowed")

for i in range(3):
    print(i)
else:
    print("Loop finished")
    
print()
print("========================")
print("Control Statements")
print("========================")
print()

##count = 1
##while count <= 5:
##    if count == 3:
##        continue
##    else:
##        print(count)
##        count += 1
##    
##    
##else:
##    print("Loop finished")


print()
print("========================")
print("Nested Loop")
print("========================")
print()

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i  = {i}, j = {j}")
    























