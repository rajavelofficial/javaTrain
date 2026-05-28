# textile_shop.py

customer = input("Enter customer name: ")

dress = input("Enter dress type: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter dress price: "))

total = quantity * price

discount = 0

if total > 7000:
    discount = total * 0.15

final_bill = total - discount

print("Customer Name:", customer)
print("Dress Type:", dress)

print("Quantity:", quantity)
print("Total Amount:", total)

print("Discount:", discount)
print("Final Bill:", final_bill)

for i in range(3):
    print("Billing Completed")

print("Textile Shop Billing System")
print("Thank You")