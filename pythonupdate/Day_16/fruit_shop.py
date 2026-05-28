# fruit_shop.py

customer = input("Enter customer name: ")

fruit = input("Enter fruit name: ")

quantity = int(input("Enter quantity in kg: "))

price_per_kg = 120

total = quantity * price_per_kg

print("Customer Name:", customer)
print("Fruit Name:", fruit)

print("Quantity:", quantity)
print("Price Per KG:", price_per_kg)

print("Total Amount:", total)

if total > 3000:
    print("Free Fruit Basket Added")
else:
    print("Regular Purchase")

payment = input("Enter payment mode: ")

print("Payment Mode:", payment)

for i in range(3):
    print("Fruit Bill Generated")

print("Fruit Shop Billing System")
print("Thank You")