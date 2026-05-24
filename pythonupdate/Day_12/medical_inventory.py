# medical_inventory.py

medicine = input("Enter medicine name: ")

company = input("Enter company name: ")

stock = int(input("Enter available stock: "))

sold = int(input("Enter sold quantity: "))

remaining = stock - sold

print("Medicine Name:", medicine)
print("Company Name:", company)

print("Available Stock:", stock)
print("Sold Quantity:", sold)

print("Remaining Stock:", remaining)

if remaining < 10:
    print("Restock Required")
else:
    print("Stock Available")

expiry = input("Enter expiry date: ")

print("Expiry Date:", expiry)

for i in range(3):
    print("Inventory Updated")

print("Medical Inventory System")
print("Thank You")