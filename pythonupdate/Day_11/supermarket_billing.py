# supermarket_billing.py

customer = input("Enter customer name: ")

item = input("Enter item name: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter item price: "))

total = quantity * price

discount = 0

if total > 5000:
    discount = total * 0.10

final_bill = total - discount

print("Customer Name:", customer)
print("Item Name:", item)

print("Quantity:", quantity)
print("Total Amount:", total)

print("Discount:", discount)
print("Final Bill:", final_bill)

for i in range(3):
    print("Billing Completed")

print("Supermarket Billing System")
print("Visit Again")