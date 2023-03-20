total = 0

item_number = int(input("Number of items: "))
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items: "))

for i in range(0, item_number, 1):
    price = float(input("Price of item: "))
    total += price

if total >= 100:
    total *= 0.9

print(f"Total price for 3 items is ${total:.2f}")





