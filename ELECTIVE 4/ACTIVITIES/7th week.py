student = {
    "name": "john robert",
    "age": 22,
}

print(len(student))
print(type(student))

info = {}
keys = ["name", "age", "addr"]
values = ["john", 22, "Umingan"]
info = dict.fromkeys(keys, values)
print(info)

info = {
    "name" : "john",
    26 : "age",
    3.12 : "pi",
    True : "isvalid"
}


print(f'{info.get(26)}')
print(f'{info.keys()}')
print(f'{info.values()}')
print()
for key in info:
    print(key)

print()
for key in info.keys():
    print(key)
print()

count = 0
for value in info.values():
    count += 1
    if count == len(info):
        print(value)
    else:
        print(value, end="-")
print()

print (info.items())

for item in info.items():
    print(f"Key: {item[0]} -> Value: {item[1]}")

print()
##Unpacking a tuple
for key, value in info.items():
    print(f"")

myTup = (1, 2, 3)
a = myTup
print(a[0])
print(a[1])
print(a[2])

print()

