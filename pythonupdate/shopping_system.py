# shopping_system.py

customer = input("Enter customer name: ")

product = input("Enter product name: ")

price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

discount = 0

if total > 5000:
    discount = total * 0.10

final_amount = total - discount

print("Customer Name:", customer)
print("Product Name:", product)
print("Total Amount:", total)
print("Discount:", discount)

print("Final Amount:", final_amount)

for i in range(3):
    print("Order Processing")

print("Shopping Menu")
print("1. Buy Product")
print("2. Payment")
print("3. Order Status")

print("Thank You for Shopping")