# inventory_management.py

product = input("Enter product name: ")

stock = int(input("Enter available stock: "))

sold = int(input("Enter sold quantity: "))

remaining = stock - sold

print("Product Name:", product)
print("Available Stock:", stock)

print("Sold Quantity:", sold)
print("Remaining Stock:", remaining)

if remaining < 10:
    print("Low Stock Alert")
else:
    print("Stock Available")

price = int(input("Enter product price: "))

revenue = sold * price

print("Total Revenue:", revenue)

for i in range(3):
    print("Inventory Updated")

print("Inventory Management System")
print("Thank You")