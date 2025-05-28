total_price = 0
items_count = int(input("Number of items: "))
while items_count < 0:
    print("Invalid number of items!")
    items_count = int(input("Number of items: "))
for i in range(items_count):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.90
print(f"Total price of {items_count} items is ${total_price:.2f}")
