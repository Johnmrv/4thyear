print("")
print("=== PESO NOTE COUNTER ===")
print("")

amount = int(input("Enter amount in pesos: "))

p1000 = amount // 1000
amount = amount % 1000

p500 = amount // 500
amount = amount % 500

p200 = amount // 200
amount = amount % 200

p100 = amount // 100
amount = amount % 100

p50 = amount // 50
amount = amount % 50

p20 = amount // 20
amount = amount % 20

p10 = amount // 10
amount = amount % 10

p5 = amount // 5
amount = amount % 5

p1 = amount

print("")
print("1000 pesos -", p1000)
print("500 pesos  -", p500)
print("200 pesos  -", p200)
print("100 pesos  -", p100)
print("50 pesos   -", p50)
print("20 pesos   -", p20)
print("10 pesos   -", p10)
print("5 pesos    -", p5)
print("1 peso     -", p1)
